import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]
    a = emotions['emotion']
    dominant_emotion = max(zip(a.values(), a.keys()))[1]

    return {'anger' : emotions['emotion']['anger'] ,
            'disgust' : emotions['emotion']['disgust'],
            'fear' : emotions['emotion']['fear'],
            'joy' : emotions['emotion']['joy'],
            'sadness' : emotions['emotion']['sadness'],
            'dominant_emotion': dominant_emotion
            }

   