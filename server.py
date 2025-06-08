from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    result_lines = [f"{emotion}: {score}" for emotion, score in result.items()]
    return result_lines 

@app.route("/")
def render_index_page():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(host="localhost", port=5001)
