def getFeels():
    '''
    Gets data from .feels file and returns it in a dictionnary format.
    A .feels file is structured as follows: 
        red;angry;ff0000
        cyan;wide;4080ff
        blue;normal;0000c0
        magenta;wiggle;e040e0
        yellow;excited;fad700
    '''
    with open('feels.txt', 'r') as file:
        feels = file.readlines()
        feels_dict = {}
        for feel in feels:
            name, mood, color = feel.strip().split(';')
            feels_dict[name] = {'mood': mood, 'color': color}
        return feels_dict
