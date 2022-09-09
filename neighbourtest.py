import matplotlib.pyplot as plt
import time
from Neighbours import badneighbours, neighbours, recNeighbors

k = 20
seqList = ["A"]
for i in range(1, k):
    seqList.append(seqList[i-1] + "A")


print(seqList)

d = 3

fast = []
slow = []
x = list(range(len(seqList)))

for seq in seqList:
    start = time.process_time()
    neighbours(seq, d)
    fast.append(time.process_time() - start)
    print("Done f")

for seq in seqList:
    start = time.process_time()
    recNeighbors(seq, d)
    slow.append(time.process_time() - start)
    print("Done s")

plt.plot(x, fast, label="Iterative")
plt.plot(x, slow, label="Recursive")
plt.legend()
plt.ylabel("Time (s)")
plt.xlabel("k")

plt.show()
