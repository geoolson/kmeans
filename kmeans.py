import math
import random
import numpy as np
import matplotlib.pyplot as plt
    
centerChanging = [False,False,False,False,False,False,False,False,False,False]

# checks if all the cluster centers have stopped training
def areTrained():
    global centerChanging
    for i in centerChanging:
        if i == False:
            return False
    return True

# returns true if there is no difference between the objects
def diff(x,y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True

def preprocess(filename):
    f = open(filename, 'r')
    f = f.read().splitlines()
    images = []
    labels = []
    for i in f:
        temp = [int(j) for j in i.split(',')]
        labels.append(temp.pop())
        images.append(temp)
    return (images, labels)

def kdistance(image, centroid):
    f = lambda x, y : (x-y)**2
    sum = 0
    for (i,j) in zip(image, centroid):
        sum += f(i,j)
    return math.sqrt(sum)

def iterate(images, centroids):
    distances = []
    for i in images:
        centroidDist = []
        for j in centroids:
            centroidDist.append(kdistance(i, j))
        distances.append(centroidDist)
    return distances

def clusterMembers(distances):
    members = []
    for i in distances:
        members.append(i.index(min(i)))
    return members

# k being the number of centroids
def initCentroids(k=10):
    centroids = []
    for i in range(k):
        centroids.append(initCentroid())
    return centroids

# create a centroid of random values
def initCentroid():
    centroid = []
    for j in range(64):
        centroid.append(random.randint(0,16))
    return centroid

def updateCenter(index, images, clusterList, centroid):
    global centerChanging
    if centerChanging[index] == True:
        return centroid
    count = 0
    listSums = [0]*64
    for i in range(len(images)):
        if index == clusterList[i]:
            count += 1
            listSums = [x + y for x, y in zip(listSums, images[i])]
    try:
        updatedCenter = [ x/count for x in listSums]
        if diff(updatedCenter, centroid):
            centerChanging[index] = True
            print(centerChanging)
            return centroid
        else:
            return updatedCenter
    except:
        return initCentroid()

def episdode(images, centroids):
    distances = iterate(images, centroids)
    members = clusterMembers(distances)
    for i in range(len(centroids)):
        centroids[i] = updateCenter(i, images, members, centroids[i])
    return centroids

def train(centroids, images, labels):
    while areTrained() == False:
        centroids = episdode(images, centroids)
    return centroids

def display(centroids):
    imgArrays = []
    for i in range(10):
        imgArrays.append(np.zeros((8,8)))
    index = 0
    for center in centroids:
        numpyarray = imgArrays[index]
        for i in range(8):
            for j in range(8):
                numpyarray[i][j] = math.floor(center[i*8+j])
        imgArrays[index] = numpyarray.astype(int)
        index += 1
    print(imgArrays[0])
    for i in range(10):
        arr = np.asarray(imgArrays[i])
        plt.imshow(arr, cmap='gray')
        plt.show()

if __name__ == "__main__":
    centroids = initCentroids()
    images = preprocess("optdigits/optdigits.train")
    labels = images[1]
    images = images[0]
    display(train(centroids, images, labels))
