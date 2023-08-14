from docx import Document

def substituicao(lista):
  documento = Document("Contrato.docx")

  # nome = input("nome: ")
  # cpf = input("cpf: ")
  # rg = input("rg: ")
  # rua = input("rua: ")
  # bairro = input("bairro: ")
  # cidade = input("cidade: ")
  # estado = input("estado: ")
  # telefone = input("telefone: ")
  # email = input("email: ")
  # preco = input('preco: ')

  # informacoes = [nome,cpf,rg,rua,bairro,cidade,estado,telefone,email,preco]
  lacunas = ['AAAAA','BBBBB','CCCCC','DDDDD','EEEEE','FFFFF','GGGGG','HHHHH','IIIII', 'JJJJJ','LLLLL','MMMMM','NNNNN', 'OOOOO']

  for linha in documento.paragraphs:
    for i in range(len(lacunas)):
      linha.text = linha.text.replace(lacunas[i], lista[i])

  documento.save(f"contrato_{lista[0]}.docx")