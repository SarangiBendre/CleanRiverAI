from ultralytics import YOLO

model = YOLO("model/best.pt")

results = model.predict(
    source="D:/CleanRiverAI/dataset/test/images/",
    conf=0.4,
    save=True
)

print("\n===== Clean River AI Output =====\n")

for i, result in enumerate(results):
    count = len(result.boxes)

    # Pollution logic
    if count <= 5:
        level = "LOW"
    elif count <= 15:
        level = "MEDIUM"
    else:
        level = "HIGH"

    print(f"Image {i+1}:")
    print(f"Plastic Waste Count: {count}")
    print(f"Pollution Level: {level}\n")

print("===============================")