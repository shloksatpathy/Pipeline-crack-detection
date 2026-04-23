# 🔍 Pipeline Crack Detection

A deep-learning-based system for detecting **metal surface defects** such as cracks, corrosion/rust, scratches, and holes on industrial pipelines. Built using **YOLOv8 Nano** for real-time, lightweight inference — optimized for edge deployment on devices like the **Raspberry Pi**.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Defect Classes](#defect-classes)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Label Generation](#label-generation)
  - [Training](#training)
- [Model Details](#model-details)
- [Future Scope](#future-scope)
- [License](#license)

---

## Overview

Industrial pipelines are critical infrastructure assets that require regular inspection to prevent catastrophic failures. Manual inspection is time-consuming, expensive, and error-prone. This project automates the detection of surface-level defects using computer vision, enabling faster and more reliable pipeline health assessments.

The system trains a **YOLOv8 Nano** object-detection model on labeled images of metal surfaces and is designed to run efficiently on resource-constrained hardware for in-field deployment.

---

## Features

- **Multi-class defect detection** — identifies cracks, rust, scratches, holes, and normal surfaces.
- **Lightweight model** — YOLOv8 Nano architecture for fast inference on edge devices.
- **Edge-ready** — optimized image size (320×320) and small batch training for Raspberry Pi deployment.
- **Automated labelling** — utility script to generate YOLO-format labels from class-organized image folders.
- **Roboflow integration** — supplementary crack-detection dataset sourced from Roboflow.

---

## Defect Classes

| Class ID | Defect Type | Description                              |
|----------|-------------|------------------------------------------|
| 0        | Crack       | Fractures or fissures on the surface     |
| 1        | Hole        | Punctures or perforations in the metal   |
| 2        | Rust        | Corrosion or oxidation patches           |
| 3        | Scratch     | Surface abrasions or score marks         |
| 4        | Normal      | Defect-free surface (healthy baseline)   |

---

## Dataset

The project uses a combination of:

1. **Custom industrial defect dataset** — images organized by class into `train/` and `val/` splits with YOLO-format bounding-box labels.
2. **Roboflow crack dataset** — 1,551 annotated crack images exported in YOLOv8 format (no augmentation applied).

### Directory Layout

```
dataset/
├── images/
│   ├── train/       # Training images
│   └── val/         # Validation images
├── labels/
│   ├── train/       # Training labels (YOLO format)
│   └── val/         # Validation labels (YOLO format)
└── runs/            # Dataset-level experiment runs
```

> **Label format (YOLO):** `<class_id> <x_center> <y_center> <width> <height>` (normalized 0–1)

---

## Project Structure

```
Pipeline crack detection/
│
├── dataset/              # Images and labels (train/val splits)
├── roboflow_data/        # Supplementary Roboflow crack dataset
├── runs/                 # Training run outputs (weights, metrics)
│   └── detect/
│       ├── train/        # First training run
│       └── train-2/      # Second training run
│
├── labelling.py          # Auto-generates YOLO labels from folder structure
├── train.py              # Model training script
├── data.yaml             # Dataset configuration for YOLO
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── readme.md             # This file
```

---

## Installation

### Prerequisites

- Python 3.8+
- NVIDIA GPU with CUDA support (recommended for training)
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/Pipeline-crack-detection.git
cd Pipeline-crack-detection

# Create and activate a virtual environment
python -m venv yoloenv
# Windows
yoloenv\Scripts\activate
# Linux / macOS
source yoloenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Label Generation

If your images are organized by class in a folder structure, use `labelling.py` to auto-generate YOLO-format label files:

```bash
python labelling.py
```

> **Note:** By default, the script processes images in `industrial_defect_dataset/val/` and writes labels to `industrial_defect_dataset/labels/val/`. Update the `base_path` and `output_labels` variables in the script for your specific paths.

### Training

Train the YOLOv8 Nano model using the configured dataset:

```bash
python train.py
```

**Default training configuration:**

| Parameter  | Value                    |
|------------|--------------------------|
| Base model | `yolov8n.pt`             |
| Epochs     | 50                       |
| Batch size | 8                        |
| Image size | 320 × 320               |
| Workers    | 2                        |
| Device     | GPU (`device=0`)         |
| Output     | `runs/pipeline_defect_model` |

Trained weights are saved to `runs/detect/pipeline_defect_model/weights/`.

---

## Model Details

| Property          | Value                                         |
|-------------------|-----------------------------------------------|
| Architecture      | YOLOv8 Nano (`yolov8n`)                       |
| Task              | Object Detection                              |
| Input resolution  | 320 × 320 px                                  |
| Number of classes | 5                                             |
| Framework         | [Ultralytics](https://github.com/ultralytics/ultralytics) |
| Target hardware   | Raspberry Pi / edge devices                   |

---

## Future Scope

- 🎥 **Real-time video inference** — integrate with a live camera feed for on-site pipeline inspection.
- 📊 **Performance benchmarking** — evaluate mAP, precision, recall, and inference latency across hardware.
- 🔄 **Data augmentation** — apply mosaic, mixup, and geometric transforms to improve robustness.
- 🚀 **Model export** — convert to ONNX / TensorRT / TFLite for accelerated edge inference.
- 🤖 **Drone / robot integration** — mount the inference pipeline on autonomous inspection platforms.
- 📈 **Active learning** — iteratively improve the model with newly collected field data.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

> **Note:** The supplementary Roboflow dataset component is under a separate **Private** license as specified by Roboflow.

---

<p align="center">
  <i>Built with ❤️ using <a href="https://github.com/ultralytics/ultralytics">Ultralytics YOLOv8</a></i>
</p>
