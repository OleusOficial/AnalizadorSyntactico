class syntax:

    def countLI(self,content):
        counter = 0
        for x in content:
            if x == "{":
                counter+=1
        return counter

    def countLD(self,content):
        counter = 0
        for x in content:
            if x == "}":
                counter+=1
        return counter

    def countCI(self,content):
        counter = 0
        for x in content:
            if x == "[":
                counter+=1
        return counter

    def countCD(self,content):
        counter = 0
        for x in content:
            if x == "]":
                counter+=1
        return counter

    def countPI(self,content):
        counter = 0
        for x in content:
            if x == "(":
                counter+=1
        return counter

    def countPD(self,content):
        counter = 0
        for x in content:
            if x == ")":
                counter+=1
        return counter