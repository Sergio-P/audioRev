import speech_recognition as sr


# obtain audio from the microphone
def record_and_transcript(verbose=True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if verbose:
            print "Grabando..."
        audio = r.listen(source)

    if verbose:
        print "Reconociendo..."

    text = ""

    try:
        text = r.recognize_google(audio, language="es-CL")
    except sr.UnknownValueError:
        print "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Google Speech Recognition service; {0}".format(e)

    if verbose and text != "":
        print "Transcripcion: " + text

    return text