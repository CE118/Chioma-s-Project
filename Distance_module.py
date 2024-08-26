#!/usr/bin/env python
# coding: utf-8

# In[7]:

import math
import Dataset_module as dset

data = dset.dataset()

def distance1(data, input_user, input_trans, input_trans2):
    try:
        id_list = list(data.keys())
        if input_user in id_list:
            if input_user not in id_list:
                raise KeyError("User ID is invalid")
            id_trans = list(data[input_user].keys())

            if input_trans not in id_trans and input_trans2 not in id_trans:
                raise KeyError("Transaction ID is invalid")
            if input_trans in id_trans and input_trans2 not in id_trans:
                print(f"{input_trans} transaction exist but {input_trans2} does not exist in given user id")
            if input_trans not in id_trans and input_trans2 in id_trans:
                print(f"{input_trans2} transaction exist but {input_trans} does not exist in given user id")

            if input_trans not in id_trans and input_trans2 not in id_trans:
                print("Both transactions do not exist")

            lat1 = data[input_user][input_trans]["lat"]
            lon1 = data[input_user][input_trans]["long"]
            lat2 = data[input_user][input_trans2]["lat"]
            lon2 = data[input_user][input_trans2]["long"]
            dist = round(math.sqrt((lon2-lon1)**2 + (lat2-lat1)**2),2)
            return f"The distance between transactions {input_trans} and {input_trans2} of user {input_user} is {dist}KM"
        
    except KeyError as e:
        print("Error:", e)

# In[ ]:
def distance2(data, input_user1, input_user2, input_trans1, input_trans2):
    try:
        id_list = list(data.keys())

        if input_user1 != input_user2:
        
            if input_user1 not in id_list and input_user2 not in id_list:
                raise KeyError("User ID is invalid")  
            
            id_trans1 = list(data[input_user1].keys()) 
            id_trans2 = list(data[input_user2].keys())  
            if input_trans1 not in id_trans1 and input_trans2 not in id_trans2:
                raise KeyError("Transaction ID is invalid") 
            if input_trans1 in id_trans1 and input_trans2 not in id_trans2:
                print(f"{input_trans1} is valid but {input_trans2} is not valid")
            if input_trans1 not in id_trans1 and input_trans2 in id_trans2:
                print(f"{input_trans2} is valid but {input_trans1} is not valid")
            if input_trans1 not in id_trans1 and input_trans2 not in id_trans2:
                print("Both transactions do not exist")

            lat1 = data[input_user1][input_trans1]["lat"]
            lon1 = data[input_user1][input_trans1]["long"]
            lat2 = data[input_user2][input_trans2]["lat"]
            lon2 = data[input_user2][input_trans2]["long"]
            dist = round(math.sqrt((lon2-lon1)**2 + (lat2-lat1)**2),2)
            return f"The distance between transaction {input_trans1} of user {input_user1} and transaction {input_trans2} of user {input_user2} is {dist}KM"
                
        else:
            print("user id's are the same")

    except KeyError as e:
        print("Error:", e)

