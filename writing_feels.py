

def NewScript(cellcolor,mood,color_eyes):
    script = open("script.feels", 'wt')
    line = cellcolor + ";" + mood + ";" + color_eyes
    script.write(line + "\n")
    return script.name

def Addline(script, cellcolor,mood,color_eyes):
    script = open(script, "a")
    line = cellcolor + ";" + mood + ";" + color_eyes
    script.write(line + "\n")
    script.close()


#test
fichier = NewScript("blue","angry","ff0000")
Addline(fichier,"blue", "wide", "4080ff")
Addline(fichier,"red", "wide", "4080ff")