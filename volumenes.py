# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:42:04 2021

@author: gerardsantacatalina (1534002) 
"""

from rom_to_int import roman_to_int
from datetime import datetime
import pymongo 

def get_volumen(wb_obj, sheet_name, db):
    data = wb_obj[sheet_name]
    cont = 0
    d_volum = {}
    header = []
    
    try:
        coll = db.create_collection('volums')
    
    except:
        coll = db.volums
        
    db.volums.create_index([("titulo_volumen", pymongo.DESCENDING),("Editorial", pymongo.ASCENDING)], unique=True)
        
    for row in data.iter_rows():
        
        if cont == 0:
            cont += 1
            
            for cell in row:
                header.append(cell.value)
            
            pass
        
        else:
            if row[1].value == 's.a.':     #Aquí els volumenes que no tenen la data definida simplement no els afegim, mirar el cas que això ens porti errors
                pass
            
            else:
                l = []
                
                data_temp = '01/01/' + str(row[1].value)
                
                try:
                    data_obj = datetime.strptime(data_temp + ' 10:00:00', '%d/%m/%Y %H:%M:%S')
                                            
                except:
                    data_obj = None
                
                
                tup = (row[0].value, row[2].value, data_obj)
                
                try:
                    pg_temp = row[4].value.split(',')
                
                except:
                    pass
                
                else:
                
                    for value in pg_temp:
                        if '-' not in value:        #Preguntar si el valor en nombre romans que hi ha abans de les pàgines s'ha de tenir en compte o no
                            pass
                        
                        else:
                            act = value
                    
                                    
                    try:
                        act_spl = act.split('-')
                    
                    except:
                        pass
                    
                    else:
                             
                        for value in act_spl:
                            try:
                                l.append(roman_to_int(value))
                            
                            except:
                                l.append(int(value))
                
                if tup not in d_volum.keys():
                    d_volum[tup] = {row[7].value: [l, row[5].value]}
                
                else:
                    d_volum[tup][row[7].value] = [l, row[5].value]
    
    
    for key, value in d_volum.items():
        doc = {}
        d_temp = {}
        d_temp['cuentos'] = []
        
        # S'ha de mirar la manera de convertir els anys (que entren com un enter on només es mostra l'any) a una data
        
        doc = {header[0]: key[0], header[2]: key[1], header[1]: key[2]}
        
        for key2, value2 in value.items():
            d_temp2 = {}
            
            d_temp2['cuento'] = key2
            d_temp2['paginas'] = value2[0]
            d_temp2['fiabilidad'] = bool(value2[1])
            
            d_temp['cuentos'].append(d_temp2)
        
        doc['cuentos'] = d_temp['cuentos']
        
        try:
            coll.insert(doc)
        
        except:
            continue 
