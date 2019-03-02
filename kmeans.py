import math
import random

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

def initCentroids():
    centroids = []
    for i in range(10):
        rands = []
        for j in range(64):
            rands.append(random.randint(0,16))
        centroids.append(rands)
    return centroids

#TODO sum the lists together into a new list
def updateCenters(index, images, clusterList ):
    count = 0
    temp = [0]*64
    for i in range(len(images)):
        if index == clusterList[i]:
            count += 1
            [x + y for x, y in zip(first, second)]#fix this

if __name__ == "__main__":
    centroids = initCentroids()
    images = preprocess("optdigits/optdigits.train")
    labels = images[1]
    images = images[0]
    distances = iterate(images, centroids)
    print(clusterMembers(distances))
