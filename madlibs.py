#CMPT 120L 113
#Mad Libs exercise
#Author: D. Stern
#6 September 2018

def promptForWords():
    global x,y,z,a
    
    x = input("Enter a noun: ")
    y = input("Enter a verb: ")
    z = input("Enter an adjective: ")
    a = input("Enter a place: ")

def makeAndPrintSentence():
    print("Take your " + z + " " + x + " and " + y + " it at the " + a + "!")

def main():
    promptForWords()
    makeAndPrintSentence()

main()
