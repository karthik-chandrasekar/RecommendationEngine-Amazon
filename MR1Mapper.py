#! /usr/bin/python
#coding=utf-8

import sys

class MR1Mapper:
    def __init__(self):
        pass

    def run(self):
        product_id = None
        user_id = None
        user_rating = None

        for line in sys.stdin:
            try:
                if 'productId' in line:
                    prodcut_id = line.split(":")[1].strip()
       
                elif 'userId' in line:
                    item_id = line.split(":")[1].strip()    

                elif 'score' in line:
                    user_rating = line.split(":")[1].strip()
                    
                    if product_id and user_id and user_rating:
                        print "%s\t%s:%s" % (user_id, product_id, user_rating)
      
                    product_id = None
                    user_id = None
                    user_rating = None  

                else:
                    continue
            except:
                continue

if __name__ == "__main__":
    mr_obj = MR1Mapper()
    mr_obj.run()

#Note
#key - user_id
#value - product_id:user_rating

#trap:
#1) How to ensure input split does not split a single record which consists of multiple lines
