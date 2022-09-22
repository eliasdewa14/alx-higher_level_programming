#!/user/bin/python3
import sys
import hidden_4

if __name__ == "__main__":
    for name in dir(hidden_4):
        if name[:1] != "_":
            print(name)
