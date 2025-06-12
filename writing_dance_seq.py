

def CreateDanceScript():
    script = open("scriptSEQ.dance", 'wt')
    return script

def Addline(script, nb_steps, direct):

    line = nb_steps+direct
    script.writelines(line + "\n")


#test
fichier = CreateDanceScript()
Addline(fichier, "3","U")
Addline(fichier, "1","B")