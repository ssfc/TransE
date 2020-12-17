import argparse
import tensorflow as tf


def training_data_batch():  # generate positive triples and negative triples;
    start = 0
    end = 5

    n_triple = 4

    while start < n_triple:
        train_triple_positive = [2, 4, 6]
        train_triple_negative = []
        for t in train_triple_positive:  # this loop procedure is to create negative samples;
            train_triple_negative.append(t*3)

        start = start + 1  # add a batch size;
        prepare_t = 88  # calculate time;

        yield train_triple_positive, train_triple_negative, prepare_t






def main():
    for tp, tn, t in training_data_batch():
        print(tp)
        print(tn)
        print(t)


if __name__ == "__main__":
    main()
