import os

classes = ["crack", "rust", "scratch", "hole", "normal"]

base_path = "industrial_defect_dataset/val"  
output_labels = "industrial_defect_dataset/labels/val"

os.makedirs(output_labels, exist_ok=True)

for class_id, class_name in enumerate(classes):
    class_folder = os.path.join(base_path, class_name)

    for img_name in os.listdir(class_folder):
        if img_name.endswith((".jpg", ".png")):
            label_name = img_name.replace(".jpg", ".txt").replace(".png", ".txt")
            label_path = os.path.join(output_labels, label_name)

            with open(label_path, "w") as f:
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")