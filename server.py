'''Server Funtions'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    '''Return the emotion values.'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    msg1 = f"For the given statement, the system response is 'anger' : {anger} ,"
    msg2 = f"'disgust' : {disgust} , 'fear' : {fear} , 'joy' : {joy} , "
    msg3 = f"'sadness' : {sadness} . The dominant emotion is {dominant_emotion}"
    msg = msg1 + msg2 + msg3
    return  msg

@app.route("/")
def render_index_page():
    '''Render index.html'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
