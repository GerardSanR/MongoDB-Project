# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:55:18 2021

@author: gerardsantacatalina (1534002) 
"""

from datetime import datetime
import rom_to_int as rti

def separa(ll):
    l_ret = [ll[0]]
    
    str_temp1 = ll[1][:3]
    l_ret.append(str_temp1)
    str_temp2 = ll[1][3:]
    l_ret.append(str_temp2)
    
    return l_ret

def comp_contes(row, dic):
    
    
    if type(row[1].value) == datetime:
        data_obj_temp = row[1].value
        data_str = ''
                    
                
        if data_obj_temp.year > 1899:
            data_str = str(data_obj_temp.day) + '/' + str(data_obj_temp.month) + '/' + str(data_obj_temp.year - 100)
            data_obj = datetime.strptime(data_str + ' 10:00:00', '%d/%m/%Y %H:%M:%S')
                    
        else:
            data_obj = data_obj_temp
            
            dic['data'] = data_obj
        
    else:            
        data = str(row[1].value).replace(" ","").split('/')
        
        try:
            if len(data[1]) > 2:
                data = separa(data)
        except:
            raise ValueError
        
        if len(data)>=3:
            
            try:
                e=0
                for i in data:
                    int(i)
                    e+=1
                    
            except ValueError:
                num = rti.roman_to_int(data[e])
                data[e] = num
                e=0
                
            if len(str(data[0]))>3:
                data = data[::-1]
                
            if int(data[0])==0:
                data[0]='01'
            
            if int(data[1])==0:
                data[1]='01'
            
            
            str_temp = str(data[0])+'/'+str(data[1])+'/'+str(data[2])
                
        else:
            if len(data[0])==4:
                str_temp = '01/01/'+str(data[0])
            data = data[::-1]
    
    

        try:
            data_obj = datetime.strptime(str_temp + ' 10:00:00', '%d/%m/%Y %H:%M:%S')
            str_temp = ''
            dic['data'] = data_obj
            
        except:
            raise ValueError


    return dic


def comp_revistes(row, dic):
    if type(row[1].value) == datetime:
        data_obj_temp = row[1].value
        data_str = ''
        
    
        if data_obj_temp.year > 1899:
            data_str = str(data_obj_temp.day) + '/' + str(data_obj_temp.month) + '/' + str(data_obj_temp.year - 100)
            data_obj = datetime.strptime(data_str + ' 10:00:00', '%d/%m/%Y %H:%M:%S')
        
        else:
            data_obj = data_obj_temp
        
        dic['data'] = data_obj
             

    else:            
        data = str(row[1].value).replace(" ","").split('/')
        
        try:
            if len(data[1]) > 2:
                data = separa(data)
        except:
            raise ValueError
        
        if len(data)>=3:
        
            try:
                e=0
                for i in data:
                    int(i)
                    e+=1
                    
            except ValueError:
                num = rti.roman_to_int(data[e])
                data[e] = num
                e=0
                
            if len(str(data[0]))>3:
                data = data[::-1]
                
            if int(data[0])==0:
                data[0]='01'
            
            if int(data[1])==0:
                data[1]='01'
            
            
            str_temp = str(data[0])+'/'+str(data[1])+'/'+str(data[2])
                
        else:
            if len(data[0])==4:
                str_temp = '01/01/'+str(data[0])
            data = data[::-1]
        
        
    
        try:
            data_obj = datetime.strptime(str_temp + ' 10:00:00', '%d/%m/%Y %H:%M:%S')
            str_temp = ''
            dic['data'] = data_obj
            
        except:
            raise ValueError
    
    return dic









    
