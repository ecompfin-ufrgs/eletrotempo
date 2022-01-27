
"""
Módulo cleaner.py
Autor: Nelson S. dos Santos
Descrição: Este módulo é composto por funções que limpam os dados
Data: 27/01/2022
Versão 0.0.1
"""

# 
def  transforma_carga_em_numero(carga):
    carga['val_cargaenergiamwmed'] = carga['val_cargaenergiamwmed'].map(float)
    return carga


