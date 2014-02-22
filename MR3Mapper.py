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
                if not line:continue
                
                user_id, item_string = line.strip().split("\t")
                item_list = eval(item_string)
               
                for item_rating in item_list:
                    print "%s\t%s:%s$%s" % (item_rating.split(":")[0], user_id, item_rating.split(":")[1], 'U') 

            except:
                continue

if __name__ == "__main__":
    mr_obj = MR3Mapper()
    mr_obj.run()

#Note
#key - <item_id>
#value - <user_id:item_rating>
