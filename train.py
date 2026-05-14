from ultralytics import YOLO

def main():
    # Load a better model (more accurate than yolov8n)
    model = YOLO("yolov8s.pt")

    # Train the model
    model.train(
        data="dataset/data.yaml",   # your dataset path
        epochs=100,                # more training
        imgsz=640,                 # image size
        batch=8,                   # safe for your laptop
        device="cpu",              # since no GPU

        # 🔥 Optimization settings
        lr0=0.001,                 # lower learning rate (stable learning)
        patience=20,               # early stopping
        optimizer="AdamW",         # better optimizer

        # 🔥 Augmentation (extra boost)
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        fliplr=0.5,
        mosaic=1.0,

        # 🔥 Save best results
        save=True,
        plots=True
    )

if __name__ == "__main__":
    main()