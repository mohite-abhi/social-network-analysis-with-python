from comparisonMyopicOptimal import *
import numpy
import time

def aveMyopicTime(n, nodes, G, H):
    myopicPathfindTime = []
    
    before = time.time()
    myopicSearch(G, H, 0, nodes/2)
    after = time.time()
    # myopicPathfindTime.append(after-before)

    return (after-before)
  

def timeComparisonBwMyopicOptimal():
    x1 = [i*100 for i in range(1,11)]
    y1 = []
    for i in x1:
        G = makeRingGraph(i)
        H = G.copy()
        G = addLongLinks(G, int(i/10))
        aveTime = aveMyopicTime(10, i, G, H)
        y1.append(aveTime)
        print(i,aveTime)
    plt.plot(x1,y1)
    plt.show()

timeComparisonBwMyopicOptimal()