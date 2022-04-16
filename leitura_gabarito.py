# a) Ler o arquivo gabarito.txt (arquivo fornecido no Moodle) e guardar os seus dados em uma lista;

gabarito = []
def leitura_gabarito():
    #arquivo = input('Digite o nome do arquivo: ')
    #arquivoNome = arquivo + ".txt"
    arquivoNome = "gabarito.txt"
    try:
        with open(arquivoNome, "r") as arquivoLoad:
            for linha in arquivoLoad.readlines():
                gabarito.append(linha.strip())          
    except:
        print("Arquivo não encontrado")
    return gabarito

print(gabarito)



