# b) Ler o arquivo provas.txt (arquivo fornecido no Moodle) e guardar os seus dados em uma lista;

provas = []
def leitura_provas():
    #arquivo = input('Digite o nome do arquivo: ')
    #arquivoNome = arquivo + ".txt"
    arquivoNome = "provas.txt"
    try:
        with open(arquivoNome, "r") as arquivoLoad:
            for linha in arquivoLoad.readlines():
                provas.append(linha.strip().split(";"))         
    except:
        print("Arquivo não encontrado")
    return provas




