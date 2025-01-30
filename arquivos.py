#Abre o arquivo.txt
arquivo = open('arquivo.txt', 'w')
#Escreve os textos
arquivo.write('Curso de Python Iniciante Fundação Bradesco')
arquivo.write('\nAula prática do sexto módulo')
#Fecha o arquivo.txt
arquivo.close()

#Lê o conteúdo do arquivo.txt
lerArquivo = open('arquivo.txt', 'r')
print(lerArquivo.read())
#Fecha a leitura dele
lerArquivo.close()