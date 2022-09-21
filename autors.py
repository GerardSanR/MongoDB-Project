# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:42:26 2021

@author: gerardsantacatalina (1534002) 
"""

import pymongo 

def get_autors(wb_obj, sheet_name, db):
    data = wb_obj[sheet_name[0]]
    cont = 0
    d_autors = {}   
    header = ['Autor', 'Alias', 'Extranjero', 'Contes']
    
    doc_temp = {}
    M = []
    data_variantes = wb_obj[sheet_name[1]]
    
    for row in data_variantes:
        if row[0].value != None:
            M.append([row[0].value, row[1].value])
        
    
        
    for row in data:
        if row[0].value == None:
            break
        if cont == 0:
            cont += 1
            pass
        
        else:
            
            if (row[0].value) not in doc_temp.keys():
                if row[1].value != None:
                    doc_temp[(row[0].value)] = [row[1].value]
                else:
                    doc_temp[(row[0].value)] = None 
                    
            elif row[1].value != None:
                if row[1].value not in doc_temp[(row[0].value)]:
                    doc_temp[(row[0].value)].append(row[1].value)
                    
    
    
    cont = 0
    
    try:
        coll = db.create_collection('autors')
        
    except:
        coll = db.autors
    
    db.autors.create_index([("Autor", pymongo.ASCENDING)], unique=True)
        
    
    
 
    for row in data.iter_rows():
        if row[0].value==None:
            break
        
        if cont == 0:
            cont += 1
            pass
        
        else:
            
            for x, cell in enumerate(row):
                if x == 0:
                    if cell.value not in d_autors.keys():
                        d_autors[cell.value] = [None, False, []]
                
                elif x == 1 and cell.value is not None:
                    d_autors[row[0].value][0] = cell.value
                
                elif x == 2:
                    d_autors[row[0].value][1] = bool(cell.value)
                
                else:
                    if cell.value == None:
                        pass
                    else:
                        d_autors[row[0].value][2].append(cell.value)
    
    
        
        
            
            
                
    
    for key in d_autors.keys():
        doc = {}
        
        for x, head in enumerate(header):
            if x == 0:
                
                doc[head] = key
                continue
            
            if x == 1:
                if key in doc_temp.keys():
                    doc[head] = doc_temp[key]
            
            else:
                doc[head] = d_autors[key][x - 1]
                
        try:
            coll.insert(doc)
        except:
            continue 
              
    

