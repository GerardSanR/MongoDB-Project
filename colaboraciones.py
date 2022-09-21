# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:19:09 2021

@author: jsole & gerardsantacatalina (1531139 - 1534002)
"""

from rom_to_int import roman_to_int
from datetime import datetime
import pymongo 

def get_colab(wb_obj, sheet_name, db):
    data = wb_obj[sheet_name]
    dic = {}
    cont = 0
    header = []
    
    
    
    
    try:
        coll = db.create_collection('colaboracions')
    
    except:
        coll = db.colaboracions
        
    db.colaboracions.create_index([("titulo", pymongo.ASCENDING)], unique=True)
     
    
    for row in data:
        if cont == 0:
            cont += 1
            
            for cell in row:
                header.append(cell.value)
                
            pass
        
        else:
            try:
                data2 = row[3].value[:10]
                data_obj = datetime.strptime(data2 + ' 10:00:00', '%Y-%m-%d %H:%M:%S')
            
            except:
                data_obj = None
                
            try:
                pin = int(row[9].value)
            
            except:
                pin = None
            
            try:
                pfin = int(row[10].value)
            
            except:
                pfin = None
            
            paginas = [pin, pfin]
            
            try:
                tomo = roman_to_int(row[1].value)
            
            except:
                tomo = None
            
            try:
                num = int(row[2].value)
            
            except:
                num = None
                
            if row[8].value not in dic.keys():
                notas = row[12].value
                if notas is not None:
                    notas = notas[3:-3]
                
                versos = row[13].value
                if versos is not None:
                    versos = versos[3:-3]
                dic[row[8].value] = [{'revista': row[0].value, 'tomo': tomo, 'numero': num, 'fecha': data_obj, 'autor': row[4].value, 'traducido': row[5].value, 'firmado': row[6].value, 'seudonimo': row[7].value, 'paginas': paginas, 'clasificacion': row[11].value, 'notas': notas, 'versos': versos}]
            
            else:
                dic[row[8].value].append({'revista': row[0].value, 'tomo': tomo, 'numero': num, 'fecha': data_obj, 'autor': row[4].value, 'traducido': row[5].value, 'firmado': row[6].value, 'seudonimo': row[7].value, 'paginas': paginas, 'clasificacion': row[11].value, 'notas': notas, 'versos': versos})
    
    for key, value in dic.items():
        d_temp = {'titulo': key, 'apariciones': value}
        
        try:
            coll.insert(d_temp)
        except:
            continue 
        
