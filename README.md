# Face & Eye Detection System with Smart Image Capture

A real-time computer vision project built using **Python** and **OpenCV** that detects faces and eyes from a webcam feed, displays face count, and intelligently saves face images.

---

## 🚀 Features
- Real-time face detection using Haar Cascade
- Eye detection within detected face regions
- Live face count overlay
- Smart image saving (only when eyes are detected)
- Time-controlled capture to avoid duplicate images
- Optimized for Windows webcam handling

---

## 🛠️ Technologies Used
- Python 3.11
- OpenCV

---

## 📁 Project Structure

```
face-eye-detection-opencv/
│
├── faces/                     # Saved face images (auto-generated)
│   └── .gitkeep
│
├── face_detection.py          # Main application script
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Ignored files & folders
└── LICENSE                    # MIT License
```



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SHASHANK-CODING/face-eye-detection-opencv.git
cd face-eye-detection-opencv
```
## 2️⃣ (Optional) Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
## ▶️ Run the Application
```
python face_detection.py
```

- Press **q** to exit the application  
- Captured face images will be saved in the `faces/` directory  

## 🧠 How It Works

1. Captures a live video stream from the webcam using OpenCV.

2. Converts each video frame to grayscale to improve processing speed and detection performance.

3. Detects human faces in the frame using a Haar Cascade classifier.

4. Detects eyes within each detected face region to improve accuracy and reduce false positives.

5. Displays the real-time count of detected faces on the video screen.

6. Saves face images intelligently only when:
   - Eyes are detected  
   - A fixed time interval has passed  

7. This approach ensures clean, meaningful, and non-redundant image capture.

## 📸 Output Details

1. 🟩 Green rectangles → Detected faces  
2. 🔵 Blue rectangles → Detected eyes  
3. 🔢 Text overlay → Number of faces detected  
4. 📁 Saved images → Stored inside the `faces/` folder  

## 📌 Use Cases

1. Learning computer vision with OpenCV  
2. Building datasets for Machine Learning / AI projects  
3. Attendance or surveillance systems (base logic)  
4. Resume and interview project showcase  

## 📜 License

This project is licensed under the MIT License

## 👤 Author

- Shashank Raj
- GitHub: https://github.com/SHASHANK-CODING
