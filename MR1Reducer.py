#! /usr/bin/python
#coding=utf-8

import sys

class MR1Reducer:
    
    #Generates user - all items are product he has rated

    def __init__(self):
        pass

    def run(self):
        
        item_list = []
        cur_user_id = None
 
        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line:continue
                user_id, item_string = line.split("\t")
 
                if not cur_user_id:        
                    cur_user_id = user_id
                    item_list = [item_string]
    
                elif cur_user_id == user_id:
                    item_list.append(item_string)
                
                elif cur_user_id != user_id:
                    print "%s\t%s" % (cur_user_id, list(set(item_list)))
                    item_list = [item_string]
                    cur_user_id = user_id           
       
            except:
                print "MR1-Reducer-Exception"
          
        print "%s\t%s" % (cur_user_id, list(set(item_list)))

            
if __name__ == "__main__":
    mr_obj = MR1Reducer()
    mr_obj.run()

#Note
#key - user-id
#value - list of itemid:itemrating
#delimiter - key - value - \t
#delimiter - itemid - itemrating - :
