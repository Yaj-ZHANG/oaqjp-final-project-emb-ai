import requests 
import json 

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    inputJson = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = inputJson, headers=header)

    if response.status_code == 400:
        emotion_scores = dict.fromkeys(['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'], None)
    elif response.status_code != 200:
        emotion_scores = dict.fromkeys(['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'], None)
    else:
        formatted_response = json.loads(response.text)
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores
