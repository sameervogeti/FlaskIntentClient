from kaggle import getPredictions
from kaggle import encode_sentences

def getPrediction(text):
    input=encode_sentences(text)
    result=getPredictions('/home/svogeti/PycharmProjects/SMS-Message-Spam-Detector/finalized_model.sav', input)
    return result


