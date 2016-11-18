import os
import stat


def walktree(root):
    for file in os.listdir(root):
        path = os.path.join(root, file)
        mode = os.stat(path).st_mode

        if stat.S_ISDIR(mode):
            walktree(path)
        elif stat.S_ISREG(mode):
            print(file)
        else:
            print("unknown file type")


if __name__ == "__main__":
    walktree(os.getcwd())
