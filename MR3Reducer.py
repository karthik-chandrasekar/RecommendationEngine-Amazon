#! /usr/bin/python
#coding=utf-8

import sys

class MR3Reducer:
    #Generate item-user pairs

    def __init__(self):
        pass

    def run(self):
        cur_item_id = None
        user_string_set = set()        

        for line in sys.stdin:
            try:
                if not line:continue

                item_id, user_string = line.strip().split("\t")
                
                if item_id == cur_item_id or not cur_item_id:
                    user_string_set.add(user_string)
                    cur_item_id = item_id

                else:
                    print "%s\t%s" % (cur_item_id, user_string_set)
                    cur_item_id = item_id
                    user_string_set = set()
                    user_string_set.add(user_string)
    
            except:
                continue

        print "%s\t%s" % (cur_item_id, user_string_set)


if __name__ == "__main__":
    mr_obj = MR3Reducer()
    mr_obj.run()

#Note
#key - <item_id>
#value - set of <user_id:product rating>
