
#Fonction création de script
def NewScript(coordinates):
    script = open("scriptABS.dance", 'wt')
    line = coordinates
    script.write("ABS 3" + "\n" + line + "\n")
    script.close()
    return script.name

#Fonction rajouter des lignes dans un script
def Addline(script, coordinates):
    script = open(script, "a")
    line = coordinates
    script.write(line + "\n")



#test
fichier = NewScript("01")
Addline(fichier, "02")
Addline(fichier, "22")




