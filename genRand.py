import random

def generateRandom(num):
    arr = []
    for i in range(0, num):
        arr.append(random.randint(0, 20))
    return arr