import numpy as np
import pandas as pd
from interface import interface
from extractor import get_carga_ONS
from cleaner import transforma_carga_em_numero
from loader import grava_csv
import sys





def main():
    # Interface de administração
    intervalo = interface()

    # Leitura de dados
    print("\nColetando os dados.  Aguarde...")

    carga = get_carga_ONS(intervalo[0], intervalo[1])
    #ena = get_ena_ONS(intervalo[0], intervalo[1])
    #ear = get_ear_ONS(intervalo[0], intervalo[1])
    print("\nDados de carga diária coletados.  Iniciando a limpeza...")
    
    
    
    # Limpeza de dados
    carga_limpa = transforma_carga_em_numero(carga)
    print("Dados limpos.  Salvando arquivo de dados.")
    
    
    


    
    
    # Escrita de dados 
    try:
        grava_csv(carga_limpa)
        print("\nArquivo 'dados_higienizados.csv' foi gravado com sucesso.")
        print("\nObrigado por utilizar o EletroTempo.")
        print("\nFim da execução.")
        
    except:
        print("Houve erro de gravação")
    finally:
        sys.exit()
        
    
    
    
    

if __name__ == "__main__":
    main()
    
    