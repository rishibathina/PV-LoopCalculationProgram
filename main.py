import matplotlib.pyplot as plt
import seaborn as sns
import json
import numpy as np

# xpoints = np.array([0,5])
# ypoints = np.array([0,250])
#
# plt.plot(xpoints, ypoints)
# plt.show()

 # open json file
 # pre: file name (in json)
def loadJson(jsonFile):
    with open(jsonFile, 'r') as fileData:
        data = fileData.read()

    obj = json.loads(data)

def createDic(volume, time, volTime):
    if volume.length == time.length :
        for x in range(0, volume.length - 1):
            volTime[x] = volume[x], time[x]

# Residual volume is for Flow V Volume
# pre: a NumPy array (x axis) of Volume(t)
#      a NumPy array (y-axis) of Flow
def residualVolume(volume, flow):
    for (x, y) in zip(volume, flow):
        if x != 0 and y == 0 :
            return x

    return "no data found"

def totalLungCapacity(volume, time):
    pass

# pressure volume code

# Testing

volume = np.array([0,1,2,3,4,5])
flow = np.array([0,1,3,5,6,0])
time = np.array([1,2,3,4,5,6])
volTime = {}



cock = residualVolume(volume, flow)
print(cock)

#given volume(t), pressure(t), and flow(t)
# need to create flow(volume)