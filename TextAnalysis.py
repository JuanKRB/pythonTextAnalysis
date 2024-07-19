
givenstrin =("Lorem ipsum dolor! diam amet, consetetur Lorem magna. "
             "sed diam nonumy eirmod tempor. diam et labore? et diam "
             "magna. et diam amet.")

class TextAnalyzer(object):
    def __init__(self, text):
        self.text = text

    def ToLowerCase(self):
        self.text.lower()

    def freqAll(self):
        wordList = self.text.split(' ')
        dict = {}
        for word in set(wordList): # use set to remove duplicates in list
            dict[word] = wordList.count(word)

        return dict

    def freqOf(self, word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0

Object = TextAnalyzer(givenstrin)
print(Object.freqAll())

print("It appears ", Object.freqOf("Lorem"))

