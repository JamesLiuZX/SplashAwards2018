import random
import time
from gtts import gTTS
import speech_recognition as sr
import os
passengersdatabase = {"Alice":"Boarding Gate is A12, Timing is 3:15pm", "Bob":"Boarding Gate is A23, Timing is 12.50pm", "Catherine":"Boarding Gate is A23, Timing is 6.00pm"}
locationdatabase ={ "Coffee Shop" : "Terminal 3 Level One S1-03", "Wine House" : "Terminal 1 Level 3 S2-02"}

def recognize_speech_from_mic(recognizer, microphone):

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response["transcription"]
def activate():
    if __name__ == "__main__":
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        language = "en"
        print ("Hi, may I know your name please?")
        text = recognize_speech_from_mic(recognizer, microphone)
        print(text)
        try:
            if passengersdatabase[text]:
                output = (passengersdatabase[text])
                myobj = gTTS(text=output, lang=language, slow=False)
                myobj.save("boardinginfo.mp3")
                os.system("boardinginfo.mp3")
            else:
                print ("I couldn't hear that, please try again")
                myobj = gTTS(text="Speech unclear, please try again", lang=language, slow=False)
                myobj.save("unclear.mp3")
                os.system("unclear.mp3")
                return activate()
        except KeyError:
                print ("Name not found in database")
                myobj = gTTS(text="No name found in database", lang=language, slow=False)
                myobj.save("noinfo.mp3")
                os.system("noinfo.mp3")

def location():
    if __name__ == "__main__":
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        language = "en"
        print ("Which location do you want to go?")
        text = recognize_speech_from_mic(recognizer, microphone)
        try:
            if locationdatabase[text]:
                output = (locationdatabase[text])
                myobj = gTTS(text=output, lang=language, slow=False)
                myobj.save("shop.mp3")
                os.system("shop.mp3")
            else:
                print ("I couldn't hear that, please try again")
                myobj = gTTS(text="Speech unclear, please try again", lang=language, slow=False)
                myobj.save("unclear.mp3")
                os.system("unclear.mp3")
                return activate()            
        except KeyError:
                print ("Shop not found in database")
                myobj = gTTS(text="Shop not found in database", lang=language, slow=False)
                myobj.save("noshop.mp3")
                os.system("noshop.mp3")        
            
activate()
