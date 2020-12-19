import argparse
import tensorflow as tf
from collections import defaultdict





def main():
    # Defining a dict
    d = defaultdict(set)

    for i in range(5):
        d[i].add(i*2)

    print("Dictionary with values as list:")
    print(d)
#    print(d[2])
#    print(d[8])
    d[(2)].add(9)
    print(d)



if __name__ == "__main__":
    main()
