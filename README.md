# Real-time-Emotion-Detection-with-Python-Code
A real-time emotion detection system built using Flask, OpenCV, and FER library.  
The application detects human facial emotions using webcam and stores the results in an Excel file.

---
##  Features

-  Real-time webcam emotion detection
-  Emotion confidence score display
-  Processing time calculation
-  Automatic Excel report generation
-  Downloadable Excel report
-  Web interface using Flask

## 🛠 Technologies Used

- Python
- Flask
- OpenCV
- FER (Facial Emotion Recognition)
- OpenPyXL
- HTML & CSS

##  Project Structure

emotion_project/
│
├── detector.py
├── database.py
├── results.xlsx
├── requirements.txt
│
├── templates/
│      └── index.html
│
└── static/
       └── style.css

## ⚙ Installation

1. Clone the repository:
git clone https://github.com/Poojitha Bhashaveni/emotion-detection.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
python detector.py

4. Open in browser:
http://127.0.0.1:5000
##  Output

The system detects emotions such as:
- Happy
- Sad
- Angry
- Neutral
- Surprise
- Fear
- Disgust

All detected results are stored in an Excel sheet automatically.
##  Author

Poojitha Bhashaveni
MCA Mini Project – 2026  

##  License

This project is licensed under the MIT License.
