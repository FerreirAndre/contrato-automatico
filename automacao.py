from docx import Document

def substituicao(lista):
  documento = Document("Contrato.docx")
  
  lacunas = ['AAAAA','BBBBB','CCCCC','DDDDD','EEEEE','FFFFF','GGGGG','HHHHH','IIIII', 'JJJJJ','LLLLL','MMMMM','NNNNN', 'OOOOO']

  for linha in documento.paragraphs:
    for i in range(len(lacunas)):
      linha.text = linha.text.replace(lacunas[i], lista[i])

  documento.save(f"contrato_{lista[0]}.docx")