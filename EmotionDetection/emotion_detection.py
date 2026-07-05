# Importiamo la libreria requests.
# Serve per inviare richieste HTTP, in questo caso una richiesta POST al servizio Watson NLP.
import requests

# Importiamo la libreria json.
# Serve per convertire una stringa JSON in un dizionario Python.
import json


# Definiamo la funzione emotion_detector.
# Questa funzione riceve come parametro il testo da analizzare.
def emotion_detector(text_to_analyze):

    # Salviamo nella variabile url l'indirizzo del servizio Watson NLP
    # che esegue il riconoscimento delle emozioni.
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Creiamo gli headers richiesti dal servizio.
    # Questo header indica quale modello Watson NLP deve essere usato.
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Creiamo il corpo della richiesta in formato dizionario Python.
    # Il servizio si aspetta il testo dentro questa struttura:
    # {
    #     "raw_document": {
    #         "text": testo_da_analizzare
    #     }
    # }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Inviamo una richiesta POST al servizio Watson NLP.
    # Passiamo:
    # - l'URL del servizio
    # - il JSON con il testo da analizzare
    # - gli headers con il modello da usare
    response = requests.post(url, json=input_json, headers=headers)

    # La risposta arriva come testo JSON.
    # json.loads converte response.text da stringa JSON a dizionario Python.
    formatted_response = json.loads(response.text)

    # Dal dizionario ottenuto, estraiamo la parte che contiene i punteggi delle emozioni.
    # La struttura della risposta è:
    # formatted_response["emotionPredictions"][0]["emotion"]
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Estraiamo singolarmente il punteggio di ogni emozione richiesta.
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Troviamo l'emozione dominante.
    # max controlla quale chiave del dizionario emotions ha il valore più alto.
    # Per esempio, se joy ha il punteggio più alto, dominant_emotion sarà "joy".
    dominant_emotion = max(emotions, key=emotions.get)

    # Restituiamo il risultato finale nel formato richiesto dal progetto.
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }