import PyPDF2

#Abrir o arquivo em modo leitura e lendo em binário
pdf_file = open('C:\\Users\\jpiau\\Documents\\GitHub\\LeitorDePDF\\TestePDFTabela.pdf','rb')

#Pegar os dados do PDF do binário
dados_pdf =  PyPDF2.PdfFileReader(pdf_file)

