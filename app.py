from files import files
from syntax import syntax

file = files()
syn = syntax()

file.openDoc(r"C:\Users\PC19\Desktop\DemoPython\analizador\bye.java")
content = file.readDoc()

validation2 = syn.reservedWordsValidator(content)
validation = syn.validateSyntax(content)

if validation and validation2:
    print "La sintaxis es correcta"
else:
    print "La sintaxis es incorrecta"

