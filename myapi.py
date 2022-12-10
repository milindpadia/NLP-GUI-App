# Import
import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key('USCFgcLQl29gXwxLTmdWsSt7rH8PQAtbG0TFKfQlblM')

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response
    
    def named_entity_recognition(self, text):
        response = paralleldots.ner(text)
        return response
    
    def emotion_prediction(self, text):
        response = paralleldots.emotion(text)
        return response