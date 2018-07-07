# requires the speech_recognition library available from pip
import speech_recognition
import time


# counts down for user to talk
def countdown(n):
    print('Please speak in')
    for i in range(n, 0, -1):
        print(str(i) + '\n')
        time.sleep(.5)


# Creates mic, audio source, then tries to call google voice recognition.
def recognize_speech(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio)
    except speech_recognition.RequestError:
        print("RequestError")
    except speech_recognition.UnknownValueError:
        print('UnknownValueError')
    return response


# create recognizer and microphone , countdown, and listen for voice.
if __name__ == "__main__":
    our_recognizer = speech_recognition.Recognizer()
    our_microphone = speech_recognition.Microphone()
    spoken = 0
    print('Please Speak:\n')
    while not spoken:
        countdown(3)
        spoken = recognize_speech(our_recognizer, our_microphone)
        try:
            print("You said: {}".format(spoken))
        except 'UnknownValueError':
            print("Speech not recognizable or API not available")
        again = input('go again?[Y] / [N]')
        if again.lower() in 'y':
            spoken = 0
