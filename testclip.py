import argparse
import tensorflow as tf


def main():
#    print("hello")

#    __relation_property_head = {x: [] for x in range(5)}
#    print(__relation_property_head)

    parser = argparse.ArgumentParser(description='命令行中传入一个数字')
    # type是要传入的参数的数据类型  help是该参数的提示信息
    parser.add_argument('integers', type=str, help='传入的数字')
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
