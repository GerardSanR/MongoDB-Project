# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:30:00 2021

@author: gerardsantacatalina (1534002) 
"""

from comprovar_dates import comp_contes
import pymongo 

def get_cuentos(wb_obj, sheet_names, db):
    dades = wb_obj[sheet_names[0]]
    dic_total = {}
    cont = 0
    
    
    
    
    try:
        coll = db.create_collection('contes')
    
    except:
        coll = db.contes
    
    db.contes.create_index([("titulo", pymongo.ASCENDING)], unique=True)
    
    
    for row in dades.iter_rows():
        if row[2].value == None:
            break
        
        if cont == 0:
            cont += 1
            pass
        
        else:    
            dic = {}
            
            if (row[2].value) not in dic_total.keys():
                dic_total[(row[2].value)] = [None, None, row[5].value, []]
                
                dic['revista'] = row[0].value
                
                try:
                    dic = comp_contes(row, dic)
                
                except ValueError:
                    continue
                
                
                
                l = []
                
                try:
                    temp = row[3].value.split('-')
                
                except:
                    dic['pagines'] = None
                
                else:
                    for value in temp:
                        try:
                            l.append(int(value))
                        
                        except ValueError:
                            pass
                    
                    dic['pagines'] = l
                
                dic['fiabilitat'] = bool(row[4].value)
                
                dic_total[(row[2].value)][3].append(dic)
            
            else:
                dic['revista'] = row[0].value
                
                try:
                    dic = comp_contes(row, dic)
                
                except ValueError:
                    continue
                               
                
                l = []
                
                try:
                    temp = row[3].value.split('-')
                
                except:
                    dic['pagines'] = None
                
                else:
                    for value in temp:
                        try:
                            l.append(int(value))
                        
                        except ValueError:
                            pass
                    dic['pagines'] = l
                
                dic['fiabilitat'] = bool(row[4].value)
                
                dic_total[(row[2].value)][3].append(dic)
        
        
        
    data = wb_obj[sheet_names[3]]
    
    for row in data:
        if row[3].value not in dic_total.keys():
            dic_total[row[3].value] = [None, None, None, []]
    
    d_temes = {}
    d_generes = {}
    
    dades = wb_obj[sheet_names[1]]
    
    cont = 0
    
    for row in dades:
        if cont == 0:
            cont += 1
            pass
        
        else:
            if row[0].value in d_temes.keys():
                d_temes[row[0].value].append(row[1].value)
            
            else:
                d_temes[row[0].value] = [row[1].value]
    
    for key in d_temes.keys():                      #Preguntar què fer quan un conte se sap el tema o el genere però no hi és a cap revista. De moment no es tenen en compte els que pateixen això
        try:
            dic_total[key][0] = d_temes[key]
        except:
            pass
        
    
    dades = wb_obj[sheet_names[2]]
    
    cont = 0
    
    for row in dades:
        if cont == 0:
            cont += 1
            pass
        
        else:
            if row[0].value in d_generes.keys():
                d_generes[row[0].value].append(row[1].value)
            
            else:
                d_generes[row[0].value] = [row[1].value]
    
    for key in d_generes.keys():
        try:
            dic_total[key][1] = d_generes[key]
        except:
            pass
    
    
    for key, value in dic_total.items():
        
        d_temp = {'titulo': key, 'titulo_alternativo': value[2], 'temas': value[0], 'generos': value[1], 'publicaciones': None if len(value[3]) == 0 else value[3]}
        try:
            coll.insert(d_temp)
        except:
            continue 
        
        
              
            
        
    
