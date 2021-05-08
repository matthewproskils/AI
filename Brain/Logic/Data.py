class Logic:
    types = {
        "greeting": ["hello", "hi"],
        
    }

    def Includes(__self__, list, StrList, type):
        ReturnList = []
        i = 0
        while(i < len(StrList)):
            if(StrList[i] in list):
                ReturnList.append(StrList[i])
            i = i + 1

        return ReturnList

    def StringType(__self__, str):

        StrList = str.split(" ")

        GreetingList = __self__.Includes(
            __self__.types["greeting"], StrList, "greeting")

        return {
            "GreetingList": GreetingList,

        }
