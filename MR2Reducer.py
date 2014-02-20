#! /usr/bin/python
#coding=utf-8

import sys

class MR2Reducer:
   
    #Generate item-item vector
      
    def __init__(self):
        pass

    def run(self):
        
        cur_key_item_id = None
        cur_val_item_id = None
        pair_count  = 1
        item_string_set = set()

        for line in sys.stdin:
           
            try: 
                if not line:continue

                key_item_id, val_item_id = line.strip().split("\t")
                
                if key_item_id == cur_key_item_id or not cur_key_item_id:
                    
                    cur_key_item_id = key_item_id
                    if cur_val_item_id == val_item_id or not cur_val_item_id:
                        if cur_val_item_id:pair_count += 1
                        cur_val_item_id = val_item_id
                        item_string_set.add("%s:%s" % (cur_val_item_id, pair_count))

                    else:
                        cur_val_item_id = val_item_id
                        pair_count = 1
                                           
                else:
                    item_string_set.add("%s:%s" % (cur_val_item_id, pair_count))
                    print "%s\t%s" % (cur_key_item_id, item_string_set)
                    cur_key_item_id = key_item_id
                    cur_val_item_id = val_item_id
                    item_string_set = set()
                    item_string_set.add("%s:%s" % (cur_val_item_id, pair_count))
                    pair_count = 1

            except:
                continue    

        item_string_set.add("%s:%s" % (cur_val_item_id, pair_count))
        print "%s\t%s" % (cur_key_item_id, item_string_set)
            

if __name__ == "__main__":
    mr2_obj = MR2Reducer()
    mr2_obj.run()


#Note
#Key - <item-id>
#value - list of <item-id:pair_count> 
