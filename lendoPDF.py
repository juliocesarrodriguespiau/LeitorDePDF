import PyPDF2

#Abrir o arquivo em modo leitura e lendo em binário
pdf_file = open('C:\\Users\\jpiau\\Documents\\GitHub\\LeitorDePDF\\TestePDFTexto1.pdf','rb')

#Pegar os dados do PDF do binário
dados_do_pdf =  PyPDF2.PdfFileReader(pdf_file)

#Contar o número de páginas no PDF
print('Número de páginas: ' + str(dados_do_pdf.numPages))

pagina1 = dados_do_pdf.getPage(0)

texto_da_pagina1 = pagina1.extractText()

print(texto_da_pagina1)

