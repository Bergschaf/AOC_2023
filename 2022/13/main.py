from utils import *
import ast


def compare(left, right):
    print(left, right)
    # True gut, False schlecht, None nächstes
    if type(left) is int and type(right) is int:
        if left == right:
            return None
        return left < right

    if type(left) is list and type(right) is list:
        min_len = min(len(left), len(right))
        for i,j in zip(left[:min_len], right[:min_len]):
            x = compare(i, j)
            if x is not None:
                return x
        if len(left) == len(right):
            return None
        return len(left) < len(right)

    if type(left) is int:
        left = [left]
    if type(right) is int:
        right = [right]
    return compare(left, right)


def main(input: str):
    packets = input.split("\n\n")
    packets = [[ast.literal_eval(x) for x in packet.split("\n")] for packet in packets]
    right_order = []
    for i,packet in enumerate(packets):
        if compare(packet[0], packet[1]):
            right_order.append(i+ 1)
    return sum(right_order)


if __name__ == '__main__':
    example_target = 13
    with open("example.txt", "r") as f:
        example_output = main(f.read())

    if example_target is not None:
        if example_output == example_target:
            print(f"Example Output basst: {example_output}")
        else:
            print(f"example output basst nicht: {example_output} ;Target: {example_target}")
            exit()
    else:
        print(f"Example Output: {example_output}")

    with open("input.txt", "r") as f:
        input_output = main(f.read())

    print(f"Output: {input_output}")
