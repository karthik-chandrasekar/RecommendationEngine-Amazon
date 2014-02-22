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
                line = line and line.strip()
                if not line:continue
                if 'productId' in line:
                    product_id = line.split(":")[1]
       
                elif 'userId' in line:
                    user_id = line.split(":")[1]   

                elif 'score' in line:
                    user_rating = line.split(":")[1]
                    
                    if product_id and user_id and user_rating:
                        print "%s\t%s:%s" % (user_id, product_id, user_rating)
      
                    product_id = None
                    user_id = None
                    user_rating = None  

                else:
                    continue
            except:
                print "MR1- Mapper - Exception"
                continue

if __name__ == "__main__":
    mr_obj = MR1Mapper()
    mr_obj.run()

#Note
#key - user_id
#value - product_id:user_rating
#Delimiter - key, value - \t
#Delimiter - Inside value - :

#trap:
#1) How to ensure input split does not split a single record which consists of multiple lines
