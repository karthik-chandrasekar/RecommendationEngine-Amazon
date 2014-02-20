#! /usr/bin/python
#coding=utf-8

import sys

class MR2Reducer:
    def __init__(self):
        pass

    def run(self):
        
        cur_key_item_id = None
        cur_val_item_id = None
        pair_count  = 0
        item_string_list = []

        for line in sys.stdin:
           
            try: 
                if not line:continue

                key_item_id, val_item_id = line.split("\t")
                
                if key_item_id == cur_key_item_id or not cur_key_item_id:
                    
                    cur_key_item_id = key_item_id
                    if cur_val_item_id == val_item_id or not cur_val_item_id:
                        cur_val_item_id = val_item_id
                        pair_count += 1

                    else:
                        item_string_list.append("%s\t%s:%s" % (cur_key_item_id, cur_val_item_id, pair_count))
                        cur_val_item_id = val_item_id
                        pair_count = 0
                                           
                else:
                    print item_string_list
                    cur_key_item_id = key_item_id
                    cur_val_item_id = val_item_id
                    item_string_list = []
                    pair_count = 0

            except:
                continue    

        print item_string_list
            

if __name__ == "__main__":
    mr2_obj = MR2Reducer()
    mr2_obj.run()
