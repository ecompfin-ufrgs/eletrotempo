# Importação de módulos
import numpy as np
import pandas as pd
import sqlite3



# Leitores de dados

def get_carga_ONS(inicio: int, fim: int):
    """ 
    Função para pegar as cargas por região
    """
    fonte = 'https://ons-dl-prod-opendata.s3.amazonaws.com/dataset/carga_energia_di'
    carga_anual = pd.read_csv(
        f'{fonte}/CARGA_ENERGIA_{inicio}.csv', sep = ';', dtype=str)
    anos = list(range(inicio + 1, fim + 1))
    for ano in anos:
        variavel = pd.read_csv(
            f'{fonte}/CARGA_ENERGIA_{ano}.csv', sep = ';', dtype=str)
        carga_consolidada = pd.concat([carga_anual, variavel], axis = 0)
    return carga_consolidada




def get_ena_diario_ONS(inicio: int, fim: int):
    """
    Função para pegar as energia natural afluente diário por reservatório
    """
    fonte = 'https://ons-dl-prod-opendata.s3.amazonaws.com/dataset/ena_reservatorio_di'
    ena_anual = pd.read_csv(
        f'{fonte}/ENA_DIARIO_RESERVATORIOS_{inicio}.csv', sep = ';', dtype=str)
    anos = list(range(inicio + 1, fim + 1))
    for ano in anos:
        variavel = pd.read_csv(
            f'{fonte}/ENA_DIARIO_RESERVATORIOS_{ano}.csv', sep = ';', dtype=str)
        ena_consolidada = pd.concat([ena_anual, variavel], axis = 0)
    return ena_consolidada


def get_ear_diario_ONS(inicio: int, fim: int):
    """
    Função para pegar as energia armazenada diário por reservatório
    """
    fonte = 'https://ons-dl-prod-opendata.s3.amazonaws.com/dataset/ear_ree_di'
    ear_anual = pd.read_csv(
        f'{fonte}/EAR_DIARIO_REE_{inicio}.csv', sep = ';', dtype=str)
    anos = list(range(inicio + 1, fim + 1))
    for ano in anos:
        variavel = pd.read_csv(
            f'{fonte}/EAR_DIARIO_REE_{ano}.csv', sep = ';', dtype=str)
        ear_consolidada = pd.concat([ear_anual, variavel], axis = 0)
    return ear_consolidada


def cria_banco(nome_banco: str):
    """
    Esta função cria um banco sqlite cujo nome
    será seu parâmetro.
    """
    try:
        conn = sqlite3.connect(f'{nome_banco}.db')
        carga.to_sql("carga", conn)
        ear.to_sql('ear', conn)
        ena.to_sql('ena', conn)
    except:
        print("Deu problema")
    finally:
        conn.close()
    
