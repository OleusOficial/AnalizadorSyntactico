from files import files
from validator import validator

file = files()
validator = validator()

file.openDoc("C:\Users\GO\Documents\Test.java")
content = file.readDoc()
validation = validator.validate(content)

if validation:
    print "La sintaxis es correcta"
else:
    print "La sintaxis es incorrecta"
