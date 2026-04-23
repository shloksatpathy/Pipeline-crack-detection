from ultralytics import YOLO

def main():
    # Load model nano for raspiiiii
    model = YOLO("yolov8n.pt")

    #Train
    model.train(
        data = "data.yaml",
        epochs = 50,
        batch = 8,
        imgsz = 320,
        workers=2,
        device=0,
        project="runs",
        name="pipeline_defect_model"

    )


if __name__ == "__main__":
    main()