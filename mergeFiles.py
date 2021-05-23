import PyPDF2

#Abrindo os arquivos pdf em binário
arq1 = open('C:\\Users\\jpiau\\Documents\\GitHub\\LeitorDePDF\\TestePDFTexto1.pdf','rb')
arq2 = open('C:\\Users\\jpiau\\Documents\\GitHub\\LeitorDePDF\\TestePDFTabela.pdf','rb')

#lendo os dados binários
dados_arq1 = PyPDF2.PdfFileReader(arq1)
dados_arq2 = PyPDF2.PdfFileReader(arq2)

#declarando objeto tipo merge
merge = PyPDF2.PdfFileMerger()

#dando append no merge dos dados do pdf
merge.append(dados_arq1)
merge.append(dados_arq2)

#escrevendo o novo arquivo pdf
merge.write('C:\\Users\\jpiau\\Documents\\GitHub\\LeitorDePDF\\TestePDFMergeado.pdf')




