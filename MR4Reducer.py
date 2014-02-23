#! /usr/bin/python
#coding=utf-8

import sys

class MR4Reducer:
    def __init__(self):
        pass

    def run(self):
        
        cur_item_id = None
        cur_val_set = None
        user_item_set = set()
                    
        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line :continue
                item_id, value = line.split("\t")
                    
                #Performance trick
                eval_call = eval('lambda: ' + value)
                value_list = list(eval_call())            

                if not cur_item_id:
                    cur_item_id = item_id
                    cur_val_set = value_list                

                elif  item_id == cur_item_id:
                    if value_list[0].split("$")[1] == 'U':
                        for user in value_list:
                            user_id, rating = user.split("$")[0].split(":")
                            for item in cur_val_set:
                                item_id, pair_count = item.split("$")[0].split(":")
                                user_item_set.add("%s:%s" % (item_id, float(rating)*float(pair_count)))
                            print "%s\t%s" % (user_id, user_item_set)
                            user_item_set = set()                           
                      
                    elif value_list[0].split("$")[1] == 'P':
                        for user in cur_val_set:
                            user_id, rating = user.split("$")[0].split(":") 
                            for item in value_list:           
                                item_id, pair_count = item.split("$")[0].split(":")
                                user_item_set.add("%s:%s" % (item_id, float(rating)*float(pair_count)))
                            print "%s\t%s" % (user_id, user_item_set)
                            user_item_set = set()

                    cur_item_id = None
                    user_item_set = set() 

                elif item_id != cur_item_id:
                    cur_item_id = item_id
                    cur_val_set = value_list
                    user_item_set = set()
            
            except:
                print "MR4-Reducer- Exception"


if __name__ == "__main__":
    mr_obj = MR4Reducer()
    mr_obj.run()

#Note
#Key - user id
#Value - weighted item ids
#Delimiter - key - value - \t
#Delimiter - item id - weight - ":"
