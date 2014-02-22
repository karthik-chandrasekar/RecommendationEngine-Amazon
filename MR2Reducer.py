#! /usr/bin/python
#coding=utf-8

import sys

class MR2Reducer:
   
    #Generate item - list of co-occurrence items
      
    def __init__(self):
        pass

    def run(self):
        
        cur_key_item_id = None
        cur_val_item_id = None
        pair_count  = 1
        item_string_set = set()

        for line in sys.stdin:
           
            try: 
                line = line and line.strip()
                if not line:continue
                key_item_id, val_item_id = line.split("\t")
               
                if not cur_key_item_id:
                    cur_key_item_id = key_item_id
                    cur_val_item_id = val_item_id
 
                elif key_item_id == cur_key_item_id:

                    if cur_val_item_id == val_item_id:pair_count += 1

                    elif cur_val_item_id != val_item_id:
                        item_string_set.add("%s:%s$%s" % (cur_val_item_id, pair_count, 'P'))
                        cur_val_item_id = val_item_id
                        pair_count = 1
                                           
                elif key_item_id != cur_key_item_id:
                    item_string_set.add("%s:%s$%s" % (cur_val_item_id, pair_count, 'P'))
                    print "%s\t%s" % (cur_key_item_id, item_string_set)
                    cur_key_item_id = key_item_id
                    cur_val_item_id = val_item_id
                    item_string_set = set()
                    pair_count = 1

            except:
                print "MR2-Reducer - Exception"
                continue    

        item_string_set.add("%s:%s$%s" % (cur_val_item_id, pair_count, 'P'))
        print "%s\t%s" % (cur_key_item_id, item_string_set)
            

if __name__ == "__main__":
    mr2_obj = MR2Reducer()
    mr2_obj.run()


#Note
#Key - <item-id>
#value - list of <item-id:pair_count> 
#Delimiter - key-value - \t
#Delimiter - itemid-paircount - :
#Delimiter - Paircount-flag - $
