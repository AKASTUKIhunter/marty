

def NewScript(coordinates):
    script = open("scriptABS.dance", 'wt')
    line = coordinates
    script.write(line + "\n")
    script.close()
    return script.name

def Addline(script, coordinates):
    script = open(script, "a")
    line = coordinates
    script.write(line + "\n")



#test
fichier = NewScript("01")
Addline(fichier, "02")
Addline(fichier, "22")




