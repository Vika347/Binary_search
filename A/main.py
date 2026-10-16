
import sys
from commands import BinarySearchTree

def main():
    sys.setrecursionlimit(10000)

    q = int(sys.stdin.readline())
    tree = BinarySearchTree()
    output = []

    for _ in range(q):
        command = sys.stdin.readline().split()
        operation = command[0]

        if operation == "add":
            tree.add(int(command[1]))

        elif operation == "del":
            tree.delete(int(command[1]))

        elif operation == "exists":
            if tree.exists(int(command[1])):
                output.append("YES")
            else:
                output.append("NO")

        elif operation == "height":
            output.append(str(tree.tree_height()))

        elif operation == "print":
            output.append(tree.print_tree())

    print("\n".join(output))


if __name__ == "__main__":
    main()
