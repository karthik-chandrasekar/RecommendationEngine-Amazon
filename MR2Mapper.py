#! /usr/bin/python
#coding=utf-8

import sys, itertools

class MR2Mapper:
    #Generate item item co-ocurrence matrix

    def __init__(self):
        pass

    def run(self):
        
        for line in sys.stdin:
            try:
                if not line:continue
                items_string = line.split("\t")[1]
                item_string_list = eval(items_string.strip())
                item_string_list = [item.split(":")[0] for item in item_string_list if item]
                if len(item_string_list) == 1:continue
                item_item_perm = itertools.permutations(set(item_string_list), 2)
                for item_item_pair in item_item_perm:
                    print "%s\t%s" % (item_item_pair[0], item_item_pair[1].split(":")[0])

            except:
                continue

if __name__ == "__main__":
    mr2_obj = MR2Mapper()
    mr2_obj.run()

#Note
#Key - <item-id>
#Value - <item-id>
