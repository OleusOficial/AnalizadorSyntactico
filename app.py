from files import files
from syntax import syntax

file = files()
syn = syntax()

file.openDoc("C:\Users\GO\Documents\Test.java")
content = file.readDoc()
validation = syn.validateSyntax(content)

if validation:
    print "La sintaxis es correcta"
else:
    print "La sintaxis es incorrecta"
