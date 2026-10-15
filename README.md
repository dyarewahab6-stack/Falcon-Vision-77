# 🦅 Falcon-Vision-77

> Next-Gen Edge-Optimized C-UAS Vision Framework designed for real-time aerial threat detection, classification, and tracking on resource-constrained edge hardware.

---

### 📑 Technical Architecture & Execution Overview

| 📌 Section | 💡 Description & Technical Specifications |
| :--- | :--- |
| **System Philosophy** | Operational edge computer vision framework designed to detect, classify, and track fast-moving aerial threats (drones) with ultra-low latency without relying on cloud connectivity. |
| **System Architecture** | Custom-trained YOLO deep learning models optimized for ARM-based processors and mobile NPU acceleration for real-time threat acquisition. |
| **Inference Performance** | **~45 - 60 FPS** on mobile/edge NPUs with high precision (`mAP@0.5`) for multi-class target tracking under diverse environmental conditions. |
| **Tech Stack & Environment** | Python, PyTorch, OpenCV, YOLO Frameworks, NPU Acceleration, ARM/Android Processor Integration. |
| **Training & Dataset** | Custom-annotated aerial imagery dataset with specialized anchor-box optimization and edge-tailored transfer learning pipelines. |
| **Execution: Clone Repo** | `git clone https://github.com/dyarewahab6-stack/Falcon-Vision-77.git` <br> `cd Falcon-Vision-77` |
| **Execution: Install Setup** | `pip install -r requirements.txt` |
| **Execution: Run Inference**| `python detect.py --weights weights/falcon_v77_best.pt --source 0 --conf 0.45` |

---

