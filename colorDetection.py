calibration = {
    "green":[26,170],
    "pink":[75,177],
    "cyan":[40,179],
    "red":[65,173],
    "blue":[18,159],
    "yellow":[149,180],
    "black":[13,31],
    "ground":[80,98],
}

marge = 4

def get_color(color,IR):
    c="green"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="pink"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="cyan"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="red"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="blue"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="yellow"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="black"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    
    c="ground"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c

