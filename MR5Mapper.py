#! /usr/bin/python/
#coding=utf-8

import sys

class MR5Mapper:
    def __init__(self):
        pass

    def run(self):
        for line in sys.stdin:
            try:
                line  = line and line.strip()
                if not line:continue
                print line        

            except:
                print "MR5-Mapper- Exception"            

if __name__ == "__main__":
    mr_obj = MR5Mapper()
    mr_obj.run()
