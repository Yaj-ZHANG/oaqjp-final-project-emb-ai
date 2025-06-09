'''
This file is used to run as a web app server 
for emotion_detection application with flask
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''
    main process of emotion_detection application server
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result_lines = [f"{emotion}: {score}" for emotion, score in result.items()]
    return result_lines

@app.route("/")
def render_index_page():
    '''
    render the emotion_detection web application with index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
