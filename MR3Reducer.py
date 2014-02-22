#! /usr/bin/python
#coding=utf-8

import sys

class MR3Reducer:
   
     #Generate item - list of users

    def __init__(self):
        pass

    def run(self):
        cur_item_id = None
        user_string_set = set()        

        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line:continue
                item_id, user_string = line.split("\t")
               
                if not cur_item_id:
                    user_string_set.add(user_string)
                    cur_item_id = item_id
 
                elif item_id == cur_item_id:
                    user_string_set.add(user_string)

                elif item_id != cur_item_id:
                    print "%s\t%s" % (cur_item_id, user_string_set)
                    cur_item_id = item_id
                    user_string_set = set()
                    user_string_set.add(user_string)
    
            except:
                print "MR3 - Reducer - Exception"
                continue

        print "%s\t%s" % (cur_item_id, user_string_set)


if __name__ == "__main__":
    mr_obj = MR3Reducer()
    mr_obj.run()

#Note
#key - <item_id>
#value - set of <user_id:product rating>
#Delimiter - key-value - \t
