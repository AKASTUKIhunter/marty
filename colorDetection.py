# calibration = {
#     "green":[26,170],
#     "pink":[75,177],
#     "cyan":[40,179],
#     "red":[65,173],
#     "blue":[18,159],
#     "yellow":[149,180],
#     "black":[13,31],
# }

marge = 10

def get_color(color,IR, calibration):
    for c in calibration.keys():
        if ((color <= calibration[c][0] + marge and color >= calibration[c][0] - marge) and (IR <= calibration[c][1] + marge and IR >= calibration[c][1] - marge)):
            return c