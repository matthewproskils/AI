import SpeechListener

from Brain.Logic import Data

class NewBrain:
    Listener = SpeechListener.NewSpeechListener()
    AllText = []

    logic = Data.Logic()

    def InitBrain(__self__):
        __self__.Listener.InitSpeech(__self__.Eval)
        AllText = __self__.Listener.AllText

    def Eval(__self__, text):
        types = __self__.logic.StringType(text)
        print(types)
