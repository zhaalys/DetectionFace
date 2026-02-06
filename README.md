#  Face Detection with MediaPipe

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face_Detection-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green)

A simple, fast, and robust real-time face detection application using Google's **MediaPipe** framework and **OpenCV**. This tool detects faces from your webcam feed and displays the detection confidence score in real-time.

##  Features

- **Real-time Detection**: Uses your webcam to detect faces instantly.
- **High Accuracy**: Powered by MediaPipe's lightweight and accurate face detection model.
- **Confidence Score**: Displays how confident the model is about each detected face (e.g., "98.5%").
- **Lightweight**: Minimal dependencies, easy to run on most machines.

##  Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher installed.
- A webcam connected to your computer.

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/zhaalys/DetectionFace.git
    cd DetectionFace
    ```

2.  **Create a virtual environment (Optional but Recommended)**

    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

##  Usage

Simply run the main script:

```bash
python main.py
```

- A window will open showing your webcam feed.
- Detected faces will have a **green bounding box** and a **confidence percentage**.
- Press **`q`** on your keyboard to exit the application.

##  Built With

- [Python](https://www.python.org/)
- [MediaPipe](https://developers.google.com/mediapipe)
- [OpenCV](https://opencv.org/)

##  Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
