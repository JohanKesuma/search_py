

from sys import path
path.append('.')
from model.search import Search

if __name__ == "__main__":
    data = [20, 32, 54, 12, 11, 51, 21, 4, 22]
    data.sort()
    print(data)

    pos = Search.binarySearch(data, 21)
    print(pos)
