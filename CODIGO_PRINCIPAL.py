# Após a leitura dos arquivos, o programa deverá analisar as provas dos alunos e gerar um arquivo de
# saída (resultado.txt), contendo os dados existentes no arquivos provas.txt, porém deverá conter no
# final de cada linha a quantidade de acertos de cada prova. Esse arquivo deverá ser ordenando da
# maior para a menor nota. Lembre-se de salvá-lo na mesma pasta/diretório do arquivo .py.

import leitura_gabarito as gb
import leitura_provas as pv
import os

matriz = []
provas = pv.leitura_provas().copy()
gabarito = gb.leitura_gabarito().copy()
#contagem de questões corretas
l = 0
i = 0
while i < 100:
    corretas = 0
    l=0
    while l < 10:
        if str(provas[i][l+1]) == str(gabarito[l]):
            corretas +=1
        l +=1
    provas[i].append(corretas) #criação de nova coluna para armazenamento de notas
    i +=1
#ordenação dos alunos por nota descrescente
while True:
  completo=True
  i=1
  while i-1<100:
    if i<100:
      if provas[i-1][11]<provas[i][11]:
        provas[i],provas[i-1]=provas[i-1],provas[i]
        completo=False
    i+=1
  if completo==True:
    break
#leitura dos nomes dos alunos e questoes acertadas
i=0
while i<100:
    print(provas[i][0]," acertou ",provas[i][11]," questões")
    i+=1

# Obtendo o diretório (caminho) do arquivo .py
diretorio = os.path.dirname(os.path.realpath(__file__))

# Montando o nome do arquivo
nome_arquivo_output = diretorio + '\\resultado.txt'

# Salvar a lista Ordenada em arquivo
    # TODO: Implementar
arquivo_output = open(nome_arquivo_output, "w" , encoding = "utf-8")
for valor in provas:
    arquivo_output.write(str(valor) + "\n")
arquivo_output.close()
  