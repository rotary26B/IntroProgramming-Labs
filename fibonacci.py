#CMPT 120L 113
#Fibonacci exercise
#D.Stern
#20 Sept 2018

def fibonacci(x):
    fibOne = 1
    fibTwo = 2
    for i in range(x):
        if x < 3:
            return 1
        else:
            return fibonacci(x-fibOne) + fibonacci(x-fibTwo)

print(fibonacci(6))

#i tried my best, but i fell to the author's solutions in the end. RIP.
