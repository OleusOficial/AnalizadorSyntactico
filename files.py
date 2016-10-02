class files:

    def openDoc(self,path):
        self.file = open(path,"r")

    def readDoc(self):
        content = ""
        for line in self.file:
            content += line
        self.file.close()
        return content


