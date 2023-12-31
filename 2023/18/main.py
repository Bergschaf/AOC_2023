from utils import *
import numpy as np

DIRECTIONS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}
def main(input: str):
    input = [x.split() for x in input.split("\n") if x != ""]
    input = [(x[0],int(x[1])) for x in input]
    points = [(0,0)]
    boundary = 0
    for direction, distance in input:
        points.append((points[-1][0] + DIRECTIONS[direction][0] * distance, points[-1][1] + DIRECTIONS[direction][1] * distance))
        boundary += distance

    print(points)

    left = sum(points[i][0] * points[i+1][1] for i in range(len(points)-1))
    right = sum(points[i][1] * points[i+1][0] for i in range(len(points)-1))
    return 0.5 * abs(left - right) + boundary // 2 + 1



if __name__ == '__main__':
    example_target = 62
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
