#! /usr/bin/python
#coding=utf-8

import sys

class MR1Reducer:
    def __init__(self):
        pass

    def run(self):
        
        item_list = []
        cur_user_id = None
 
        for line in sys.stdin:
            try:
                if not line:continue
                user_id, item_string = line.split("\t")
                
                if cur_user_id == user_id or not cur_user_id:
                    cur_user_id = user_id
                    item_list.append(item_string)
                
                elif cur_user_id != user_id:
                    print "%s\t%s" % (user_id, item_list)
                    item_list = [item_string]
                    cur_user_id = user_id           

       
            except:
                continue            

        print "%s\t%s" % (user_id, item_list)
            


if __name__ == "__main__":
    mr_obj = MR1Reducer()
    mr_obj.run()
