#! /usr/bin/python
#coding=utf-8

import sys

class MR3Mapper:
    
    #Generating item-user pair
    def __init__(self):
        pass

    def run(self):
        
        for line in sys.stdin:
            try:
                line = line and line.strip()
                if not line:continue
                
                user_id, item_string = line.split("\t")
                
                #Performance trick
                eval_call = eval('lambda: ' + item_string)
                item_list = eval_call()              
 
                for item_rating in item_list:
                    print "%s\t%s:%s$%s" % (item_rating.split(":")[0], user_id, item_rating.split(":")[1], 'U') 

            except:
                print "MR3-Mapper-Exception"

if __name__ == "__main__":
    mr_obj = MR3Mapper()
    mr_obj.run()

#Note
#key - <item_id>
#value - <user_id:item_rating>
#Delimiter - key-value - \t
#Delimiter - itemid-userid - :
#Delimiter - userid-flag - $
