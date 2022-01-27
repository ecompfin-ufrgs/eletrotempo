import datetime
ano_atual = datetime.date.today().year # Capta o ano atual.
ano_base = 2000
def interface():
    print("\nBenvindo ao EletroTempo: sistema de pré-processamento de dados do ONS do Brasil.")
    print(f'\nExistem dados disponíveis a partir de {ano_base}.')
    a = True
    while a:
        try:
            ano_inicial_extracao = int(input("\nDigite o ano inicial da amostra: "))
            ano_final_extracao = int(input("\nDigite o ano final da amostra: "))
            if ano_inicial_extracao < 2003 or ano_final_extracao > ano_atual + 1:
                raise ValueError(f'\nSó existem dados entre {ano_base} e o {ano_atual + 1}.')
        except TypeError:
            print('\nO ano inicial e o ano final devem ser números inteiros.  Tente novamente.')
        a = False
    lista = [ano_inicial_extracao, ano_final_extracao]
    return lista
