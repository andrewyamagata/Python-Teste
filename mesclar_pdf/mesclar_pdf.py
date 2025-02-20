import PyPDF2
import os

merger = PyPDF2.PdfMerger()

pasta = "arquivos"
arquivos_pdf = sorted([f for f in os.listdir(pasta) if f.lower().endswith(".pdf")])

for arquivo in arquivos_pdf:
    caminho_completo = os.path.join(pasta, arquivo)
    merger.append(caminho_completo)

merger.write("PDFCompleto.pdf")
merger.close()

print("PDF mesclado com sucesso!")
