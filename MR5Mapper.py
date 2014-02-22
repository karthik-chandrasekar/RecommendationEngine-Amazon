#! /usr/bin/python/
#coding=utf-8

import sys

class MR5Mapper:
    def __init__(self):
        pass

    def run(self):
        for line in sys.stdin:
            if not line:continue
            print line        

if __name__ == "__main__":
    mr_obj = MR5Mapper()
    mr_obj.run()
