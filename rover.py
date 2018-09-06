#CMPT 120L 113
#Mars Rover Program
# 6 September 2018
# Author: David Stern

def TimeCalculation():
    light = 186000
    distance = 34000000
    time = distance/light

    print("It will take " + str(time) + " seconds to receive an image from Curiosity.")


TimeCalculation()
 
