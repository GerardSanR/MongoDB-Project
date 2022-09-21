# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:35:09 2021

@author: jsole & gerardsantacatalina (1531139 - 1534002)
"""


def delete_all(db):
    
    for col_key in db.list_collection_names():
        coll = db[col_key]
        
        coll.remove()
    
