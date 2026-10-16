import sys
from commands import BinarySearchTree


def main():
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))

    tree = BinarySearchTree()

    for x in numbers:
        tree.add(x)

    m = int(sys.stdin.readline())
    output = []

    for _ in range(m):
        command = sys.stdin.readline().split()
        direction = command[0]
        x = int(command[1])

        tree.rotate(x, direction)
        output.append(tree.print_tree())

    print("\n".join(output))


if __name__ == "__main__":
    main()
