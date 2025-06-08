import requests 
import json 

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    inputJson = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = inputJson, headers=header)

    formatted_response = json.loads(response.text)

    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores['dominant_emotion'] = dominant_emotion

    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    if response.status_code != 200:
        return emotion_scores
    
    return emotion_scores
