#!/usr/bin/env python3
import sys
import random


def load_list(path):
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def pair(names, roles, rng=random):
    return list(zip(names, rng.sample(roles, len(names))))


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <names_file> <roles_file>")
        sys.exit(1)

    names = load_list(sys.argv[1])
    roles = load_list(sys.argv[2])

    if len(roles) < len(names):
        print("Error: roles list must be at least as long as names list")
        sys.exit(1)

    for name, role in pair(names, roles):
        print(f"{name} -> {role}")


if __name__ == "__main__":
    main()
