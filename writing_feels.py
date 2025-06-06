

def CreateFeelsScript():
    script = open("script.feels", 'wt')
    return script

def Addline(script, cellcolor,mood,color_eyes):

    line = cellcolor+";"+mood+";"+color_eyes
    script.writelines(line)


fichier = CreateFeelsScript()

Addline(fichier,"blue", "wide", "4080ff" "\n")