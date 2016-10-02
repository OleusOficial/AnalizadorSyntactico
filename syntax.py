class syntax:

    OPENINGS = ["{","(","["]
    CLOSURES = ["}",")","}"]
    foundOpenings = []
    foundClosures = []

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
                    elif self.OPENINGS[0] != i and self.CLOSURES[0] == z:
                        return False
                    elif self.OPENINGS[0] != i and self.CLOSURES[0] == z:
                        return False
        if len(self.foundOpenings) == 0 and len(self.foundClosures) == 0:
            return True
        else:
            print "Aperturas sin cierre: " + str(len(self.foundOpenings))
            print self.foundOpenings
            print "Cierres sin apertura: " + str(len(self.foundClosures))
            print self.foundClosures
            return False


