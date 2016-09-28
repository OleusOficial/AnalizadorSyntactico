class files:

    def openDoc(self,path):
        self.file = open(path,"r")

    def readDoc(self):
        content = ""
        for line in self.file:
            content += line
        return content

    def closeDoc(self):
        self.file.close()
