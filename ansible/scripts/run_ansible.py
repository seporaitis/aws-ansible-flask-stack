#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    os.execlp("ansible-playbook", "ansible-playbook", *sys.argv[1:])
