# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:32:29 2021

@author: jsole & gerardsantacatalina (1531139 - 1534002)
"""

import openpyxl
from pymongo import MongoClient
import traduccio
import delete_cols
import autors
import editorials
import volumenes
import cuentos
import colaboraciones
import revistes
import sys



def main(file = 'dadesGICESXIX.xlsx'):
    Host = 'localhost'
    Port = 27017
    DSN = "mongodb://{}:{}".format(Host,Port)
    
    conn = MongoClient(DSN)
     
    db = conn['dadesGICES']
    
    wb_obj = openpyxl.load_workbook(file)
    
    traduccio.get_traduccio(wb_obj, 'traducciones', db)
    
    autors.get_autors(wb_obj, ['autores', 'Variantes autores'], db)
    
    editorials.get_editorials(wb_obj, 'volumenes_cuentos', db)
    
    volumenes.get_volumen(wb_obj, 'volumenes_cuentos', db)
    
    cuentos.get_cuentos(wb_obj, ['Cuentos', 'temas', 'Genero', 'autores'], db)
    
    colaboraciones.get_colab(wb_obj, 'colaboraciones', db)
    
    revistes.get_revistes(wb_obj, 'numeros_revistes', db)

    
def delete_all(db_name):
    
    Host = 'localhost'
    Port = 27017
    DSN = "mongodb://{}:{}".format(Host,Port)
    
    conn = MongoClient(DSN)
     
    db = conn[db_name]
    
    delete_cols.delete_all(db)




if __name__ == '__main__':
    
    if sys.argv[1] == '-f':
        main(sys.argv[2])
    
    elif sys.argv[1] == '--delete_all' and sys.argv[2] == '--bd':
        delete_all(sys.argv[3])
    
    else:
        raise ValueError("Error amb els paràmetres d'execució introduïts")
        
        
        
