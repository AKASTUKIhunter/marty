

def CreateDanceScript():
    script = open("script.dance", 'wt')
    return script

def Addline(script, nb_steps, direct):

    line = nb_steps+direct
    script.writelines(line)


#test
fichier = CreateDanceScript()
Addline(fichier, "3","U")