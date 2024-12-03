def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    response= response.text
    emotion_data = json.loads(response)
    emotion_data = emotion_data['emotionPredictions'][0]
    emotions = emotion_data['emotion']
    print(emotions)
    dominant_emotion = max(emotions, key=emotions.get)
    emotions.update({'domimant emotion': dominant_emotion})

    return emotions  # Return the response text from the API

    
