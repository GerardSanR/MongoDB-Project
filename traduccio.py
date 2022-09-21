# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:06:08 2021

@author: jsole & gerardsantacatalina (1531139 - 1534002)
"""

import pymongo 

def get_traduccio(wb_obj, sheet_name, db):
    data = wb_obj[sheet_name]
    cont = 0
    
    try:
        coll = db.create_collection('traduccions')    
        
    except:
        coll = db.traduccions
        
    db.traduccions.create_index([("titulo", pymongo.ASCENDING), ("Traductor", pymongo.DESCENDING)], unique=True)
    
    
    for row in data.iter_rows():
        doc = {}
        
        if cont == 0:
            header = []
            
            for cell in row:
                header.append(cell.value)       #Pensar si aquí posar el nom de la columna o directament Titol i Autor
            
            cont+= 1
        
        else:
            l = []
            
            for cell in row:
                l.append(cell.value)
                
            for i in range(len(header)):
                doc[header[i]] = l[i]
                
            try:
                coll.insert(doc)
            
            except:
                continue 
            
            
