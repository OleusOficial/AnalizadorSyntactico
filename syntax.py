class syntax:

    validCaracters = ["a","b","c","d","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",
                        "x","y","z"]
    RESERVED_WORDS = ["abstract","continue","for","new","switch","assert","default","goto","package","synchronized",
                      "boolean","do","if","private","this","break","double","implements","protected","throw",
                      "byte","else","import","public","throws","case","enum","instanceof","return","transient","catch",
                      "extends","int","short","try","char","final","interface","static","void","class","finally",
                      "long","strictfp","volatile","native","float","while","super","const","String"]

    SampleText = "string"

    OPENINGS = ["{","(","["]
    CLOSURES = ["}",")","]"]
    foundOpenings = []
    foundClosures = []

    def __init__(self):
        tempList = []
        for x in self.validCaracters:
            var = str(x).upper()
            tempList.append(var)
        self.validCaracters+= tempList

    def reservedWordsValidator(self, content):
        wordsCodeList = self.wordCutter(content)
        for x in wordsCodeList:
            for i in self.RESERVED_WORDS:
                if str(x).upper() == str(i).upper():
                    if not x in self.RESERVED_WORDS:
                        return False
        return True

    def validateSyntax(self, content):
        i = ""
        z = ""
        for x in content:
            if x in self.OPENINGS:
                self.foundOpenings.append(x)
            elif x in self.CLOSURES:
                self.foundClosures.append(x)
                if len(self.foundOpenings) > 0:
                    i = self.foundOpenings.pop()
                    z = self.foundClosures.pop()
                    if self.OPENINGS[0] != i and self.CLOSURES[0] == z:
                        return False
                    elif self.OPENINGS[1] != i and self.CLOSURES[1] == z:
                        return False
                    elif self.OPENINGS[2] != i and self.CLOSURES[2] == z:
                        return False
        if len(self.foundOpenings) == 0 and len(self.foundClosures) == 0:
            return True
        else:
            return False

    def wordCutter(self,text):
        wordStorage = ""
        tempList = []
        for x in text:
            if x in self.validCaracters:
                wordStorage+=x
            else:
                if wordStorage != "":
                    tempList.append(wordStorage)
                    wordStorage = ""
        return tempList
