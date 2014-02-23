#! /usr/bin/python
#coding=utf-8

import sys

class MR5Reducer:
    #Generate final recommendation vector for every user
    
    def __init__(self):
        pass

    def run(self):
        
        itemid_rating_map  = {}      
        cur_user_id = None

        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line:continue
                
                user_id, item_set = line.split("\t")
                
                #Performance trick  
                eval_call = eval('lambda: '+ item_set)
                item_set = eval_call()

                if not cur_user_id:
                    cur_user_id = user_id
                    self.add_in_map(item_set, itemid_rating_map)

                elif cur_user_id == user_id:
                    self.add_in_map(item_set, itemid_rating_map)
                                    
                elif cur_user_id != user_id:
                    print "%s\t%s" % (cur_user_id, itemid_rating_map)
                    cur_user_id = user_id
                    itemid_rating_map = {}
                    self.add_in_map(item_set, itemid_rating_map)

            except:
                print "MR5-Reducer-Exception"

        print "%s\t%s" % (cur_user_id, itemid_rating_map)


    def add_in_map(self, item_set, itemid_rating_map):
        
        for item in item_set:
            item_id, rating = item.split(":")
            cur_rating = itemid_rating_map.setdefault(item_id, 0)
            itemid_rating_map[item_id] = cur_rating + float(rating)

if __name__ == "__main__":
    mr_obj = MR5Reducer()
    mr_obj.run()

#Note
#Key - user id
#Value - weighted item ids
#Delimiter - key-value \t
#Delimiter - item  id - weight - :
