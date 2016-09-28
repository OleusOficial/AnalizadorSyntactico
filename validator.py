from syntax import syntax
class validator:

    def validate(self,content):
        syn = syntax()
        aperturas = [syn.countLI(content),syn.countCI(content),syn.countPI(content)]
        cierres = [syn.countLD(content),syn.countCD(content),syn.countPD(content)]
        if aperturas == cierres:
            return True
        else:
            return False
        
