import random
import matplotlib.pyplot as plt

def sumFun():
    sumList = [0]*1000
    xAxis = [i for i in range(1,1001)]
    for i in range(10000000):
        sumRandom = 0
        for i in range(10):
            sumRandom += random.randint(1,100)
        sumList[sumRandom-1]+=1

    plt.plot(xAxis, sumList)
    plt.xlabel("sum of 10 random no. b/w 1-100")
    plt.ylabel("iterations")
    plt.show()


sumFun()