#!/usr/bin/python
#coding=utf-8

import sys

class MR4Mapper:
    def __init__(self):
        pass

    def run(self):
        for line in sys.stdin:
            if not line:continue
            print line

if __name__ == "__main__":
    mr_obj = MR4Mapper()
    mr_obj.run()
