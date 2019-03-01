
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

if __name__ == "__main__":
    images = preprocess("optdigits/optdigits.train")
    for i in images[1]:
        print(i)
