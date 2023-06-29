import matplotlib.pyplot as plt
import numpy as np

def main(): 
    startNum = int(input("Enter starting number: "))
    endNum = int(input("Enter ending number: "))
    numList = []
    randomNumber = 12

    while startNum <= endNum:
        sqr = startNum * startNum
        print(sqr)
        startNum += 1
        numList.append(sqr)

    print(numList)
    highest = max(numList)
    print(highest)

    xaxis = list(range(1, len(numList) + 1))  # Generate x-axis values based on the length of numList
    yaxis = numList

    x = np.array(xaxis)
    y = np.array(yaxis)

    plt.plot(x, y)
    plt.show()


