import speech_recognition as sr

r = sr.Recognizer()

class NewSpeechListener:
    AllText = []

    def InitSpeech(__self__, OnSpeech):
        print("Mic Input Starting")
        while(True):
            with sr.Microphone() as source:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print("Says {}".format(text))
                    __self__.AllText.append(text)
                    OnSpeech(text)
                except:
                    print("Sorry could not recognize what you said")