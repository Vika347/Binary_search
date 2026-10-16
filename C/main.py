import sys
from avl_tree import AVLTree


def main():
    q = int(sys.stdin.readline())
    tree = AVLTree()
    output = []

    for _ in range(q):
        command = sys.stdin.readline().split()
        operation = command[0]

        if operation == "add":
            tree.add(int(command[1]))

        elif operation == "exists":
            if tree.exists(int(command[1])):
                output.append("YES")
            else:
                output.append("NO")

        elif operation == "root":
            output.append(tree.get_root())

        elif operation == "height":
            output.append(str(tree.tree_height()))

        elif operation == "print":
            output.append(tree.print_tree())

    print("\n".join(output))


if __name__ == "__main__":
    main()
