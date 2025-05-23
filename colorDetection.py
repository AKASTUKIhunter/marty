calibration = {
    "vert":[26,170],
    "rose":[75,177],
    "bleu":[40,179],
    "rouge":[65,173],
    "bleu_f":[18,159],
    "jaune":[149,180],
    "noir":[13,31],
    "sol":[80,98],
}

marge = 4

def get_couleur(color,IR):
    c="vert"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="rose"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="bleu"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="rouge"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="bleu_f"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="jaune"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="noir"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    
    c="sol"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    
