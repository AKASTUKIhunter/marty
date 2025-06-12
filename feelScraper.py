from colorDetection import  marge, get_color

class FeelScraper:
    def __init__(self, calibration, filename: str = "real.feels"):
        self.feels = self.getFeels(filename)
        self.calibration = calibration
        self.marge = marge

    def getFeels(self, filename: str) -> dict:
        '''
        Gets data from .feels file and returns it in a dictionnary format.
        A .feels file is structured as follows: 
            red;angry;ff0000
            cyan;wide;4080ff
            blue;normal;0000c0
            magenta;wiggle;e040e0
            yellow;excited;fad700
        '''
        with open(filename, 'r') as file:
            feels = file.readlines()
            feels_dict = {}
            for feel in feels:
                name, mood, color = feel.strip().split(';')
                feels_dict[name] = {'mood': mood, 'color': hexToRGB(color)}
            return feels_dict
        

def hexToRGB(color: str) -> tuple:
    """
    Converts a color from hex format to RGB format.
    :param color: Color in hex format (RRGGBB)
    :return: RGB tuple in format (R, G, B)
    """
    color = color.lstrip('#')
    return (int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))

