
#Fonction création de script
def NewScript(move):
    script = open("scriptSEQ.dance", 'wt')
    line = move
    script.write("SEQ 3" + "\n" + line + "\n")
    script.close()
    return script.name

#Fonction rajouter des lignes dans un script
def Addline(script, move):
    script = open(script, "a")
    line = move
    script.write(line + "\n")



#test
fichier = NewScript("4U")
Addline(fichier, "4U")
