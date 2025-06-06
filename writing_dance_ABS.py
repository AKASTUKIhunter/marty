



def CreateDanceScriptABS():
    script = open("scriptABS.dance", 'wt')
    return script

def Addline(script, coordinate_x, coordinate_y):

    line = coordinate_x + coordinate_y
    script.writelines(line)


#test
fichier = CreateDanceScriptABS()
Addline(fichier, "0","1")