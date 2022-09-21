#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:04:34 2021
@author: gerardsantacatalina (1534002) 
"""

import rom_to_int as rti
from comprovar_dates import comp_revistes
import pymongo 



def get_revistes(wb_obj, sheet_name, db):
    
    dades = wb_obj[sheet_name]
    dic_total = {}
    cont = 0
    
    try:
        coll = db.create_collection('revistes')
        
    except:
        coll = db.revistes
        
    db.revistes.create_index([("titol", pymongo.ASCENDING)], unique=True)
        
    for row in dades.iter_rows():
        if row[0].value == None:
            break
        
        if cont==0:
            cont+=1
            pass
        
        else:
            dic = {}
            titol_l = ((row[0].value).title()).split(' ')
            str_tit = ''
            
            for paraula in titol_l:
                if paraula == '':
                    continue
                
                else:
                    str_tit = str_tit + ' ' + paraula
            
            if (str_tit) not in dic_total.keys():
                dic_total[str_tit] = []
                
            
            try:
                dic = comp_revistes(row, dic)
            
            except ValueError:
                continue
                
            try:
                int(row[2].value)
                dic['numero'] = row[2].value
            except:
                dic['numero'] = None
            
            try:
                volum = rti.roman_to_int(row[3].value)
                dic['volum'] = volum
            
            except:
                dic['volum'] = None
            
            
            dic_total[str_tit].append(dic)
            


    for key, value in dic_total.items():
        if len(value) > 0:
            doc = {'titol': key[1::] if key[0]==" " else key, 'exemplars': value}
            
            try:
                coll.insert_one(doc)
            except:
                continue 
