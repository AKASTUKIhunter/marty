from colorDetection import calibration, marge, get_color

class FeelScraper:
    def __init__(self, filename: str = "real.feels"):
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
                feels_dict[name] = {'mood': mood, 'color': color}
            return feels_dict