# Importiamo Flask.
# Flask serve per creare il server web dell'applicazione.
from flask import Flask, render_template, request

# Importiamo la funzione emotion_detector dal package EmotionDetection.
# Questa funzione analizza il testo e restituisce le emozioni.
from EmotionDetection import emotion_detector


# Creiamo l'applicazione Flask.
app = Flask(__name__)


# Questa route mostra la pagina principale dell'app.
# Flask cercherà il file index.html dentro la cartella templates.
@app.route("/")
def index():
    return render_template("index.html")


# Questa route viene chiamata dal file JavaScript mywebscript.js.
# La traccia richiede esattamente il decorator /emotionDetector.
@app.route("/emotionDetector")
def emotion_detector_route():

    # Prendiamo il testo inserito dall'utente dalla richiesta HTTP.
    # Di solito il parametro si chiama "textToAnalyze" nel file JS fornito.
    text_to_analyze = request.args.get("textToAnalyze")

    # Passiamo il testo alla funzione emotion_detector.
    # Il risultato sarà un dizionario con anger, disgust, fear, joy, sadness e dominant_emotion.
    response = emotion_detector(text_to_analyze)

    # Creiamo la frase di output nel formato richiesto dal progetto.
    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    # Restituiamo la frase al browser.
    return formatted_response


# Avviamo l'applicazione Flask su localhost:5000.
# host="0.0.0.0" permette al Cloud IDE di esporre l'applicazione.
# port=5000 è richiesto dalla traccia.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)