# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:20:42 2021

@author: gerardsantacatalina (1534002) 
"""

import pymongo 

def get_editorials(wb_obj, sheet_name, db):
    data = wb_obj[sheet_name]
    cont = 0
    d_edit = {}
    
    try:
        coll = db.create_collection('editorials')
    
    except:
        coll = db.editorials
        
    db.editorials.create_index([("Ciutat", pymongo.ASCENDING)], unique=True)
    
    for row in data.iter_rows():
    
        if cont == 0:
            cont += 1
            pass
        
        else:
            if row[3].value not in d_edit.keys():
                d_edit[row[3].value] =  [row[2].value]
            
            else:
                if row[2].value in d_edit[row[3].value]:
                    pass
                elif row[2].value!=None:
                    d_edit[row[3].value].append(row[2].value)
    
    for key, value in d_edit.items():
        try:
            coll.insert({"Ciutat":key, "Editorials": value})
        
        except:
            continue 
            
            

