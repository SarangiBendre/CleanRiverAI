from flask import Flask, render_template, request, redirect, flash, session
import sqlite3
import os
from datetime import datetime
from ultralytics import YOLO
import cv2

# EMAIL
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# LOAD MODEL
model = YOLO("model/best.pt")

# ================= DATABASE =================
def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        river TEXT,
        location TEXT,
        count INTEGER,
        level TEXT,
        image TEXT,
        output TEXT,
        date TEXT,
        time TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# ================= EMAIL FUNCTION =================
def send_email_alert(to_email, river, location, count, level, image_path):
    msg = EmailMessage()
    msg['Subject'] = f'🚨 HIGH Pollution Alert | {river} - {location}'
    msg['From'] = 'sarangibendre04@gmail.com'   # 🔴 CHANGE
    msg['To'] = to_email

    msg.set_content(f"""
River: {river}
Location: {location}
Pollution Level: {level}
Plastic Count: {count}

Immediate action required!
""")

    with open(image_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename='result.jpg')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('digital.postboxverse@gmail.com', 'ngvv izss zoth zvyw')  # 🔴 CHANGE
        smtp.send_message(msg)

# ================= HOME =================
@app.route('/')
def home():
    if "user" not in session:
        return redirect('/login')
    return render_template('index.html')

# ================= REGISTER =================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if cur.fetchone():
            flash("User already exists ❌")
            return redirect('/register')

        cur.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, password)
        )

        conn.commit()
        conn.close()

        flash("Registration Successful ✅")
        return redirect('/login')

    return render_template('register.html')

# ================= LOGIN =================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = username
            flash("Login Successful ✅")
            return redirect('/')
        else:
            flash("Invalid Username or Password ❌")
            return redirect('/login')

    return render_template('login.html')

# ================= LOGOUT =================
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/login')

# ================= PREDICT =================
@app.route('/predict', methods=['POST'])
def predict():
    if "user" not in session:
        return redirect('/login')

    file = request.files['image']

    if file.filename == "":
        return "No image ❌"

    filename = file.filename.replace(" ", "_")
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    if img is None:
        return "Invalid image ❌"

    results = model.predict(filepath, conf=0.4)

    count = sum(len(r.boxes) for r in results)

    if count == 0:
        level = "NOT POLLUTED"
    elif count <= 5:
        level = "LOW"
    elif count <= 15:
        level = "MEDIUM"
    else:
        level = "HIGH"

    output_path = os.path.join(OUTPUT_FOLDER, "out_" + filename)
    results[0].save(filename=output_path)

    river = request.form['river']
    location = request.form['location']

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # 🚨 EMAIL ALERT
    if level == "HIGH":
        send_email_alert(
            to_email="sarangibendre04@gmail.com",   # 🔴 CHANGE
            river=river,
            location=location,
            count=count,
            level=level,
            image_path=output_path
        )

    # SAVE HISTORY
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO history (username, river, location, count, level, image, output, date, time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user"], river, location, count, level,
        filepath, output_path, date, time
    ))

    conn.commit()
    conn.close()

    return render_template("result.html",
                           count=count,
                           level=level,
                           image=filepath,
                           output=output_path,
                           river=river,
                           location=location,
                           date=date,
                           time=time)

# ================= HISTORY =================
@app.route('/history')
def history():
    if "user" not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM history WHERE username=?", (session["user"],))
    data = cur.fetchall()

    conn.close()

    return render_template('history.html', data=data)

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)