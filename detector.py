from flask import Flask, render_template, Response, send_file
import cv2
from fer import FER
import time
from database import save_to_excel

app = Flask(__name__)

detector = FER(mtcnn=True)
camera = cv2.VideoCapture(0)

last_saved_time = 0

def generate_frames():
    global last_saved_time

    while True:
        start_time = time.time()

        success, frame = camera.read()
        if not success:
            break

        result = detector.detect_emotions(frame)

        for face in result:
            (x, y, w, h) = face["box"]
            emotions = face["emotions"]

            emotion_name = max(emotions, key=emotions.get)
            confidence = emotions[emotion_name]

            # Calculate processing time
            end_time = time.time()
            processing_time = round(end_time - start_time, 2)

            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame,
                        f"{emotion_name} ({confidence:.2f}) | {processing_time}s",
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0,255,0), 2)

            # Save every 5 seconds
            current_time = time.time()
            if current_time - last_saved_time > 5:
                save_to_excel(emotion_name, confidence)
                last_saved_time = current_time

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# NEW ROUTE → DOWNLOAD EXCEL FILE
@app.route('/download')
def download_file():
    return send_file("results.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

