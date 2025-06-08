from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if not text_to_analyze:
        return "Please provide text using the 'textToAnalyze' query parameter.", 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Emotion detection failed. Please try again later.", 500

    result_lines = [f"{emotion}: {score}" for emotion, score in result.items()]
    return result_lines 

@app.route("/")
def render_index_page():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
    