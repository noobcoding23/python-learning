import PyPDF2
import os

pdf_path = '004-installment/PDF-directory'
pdf_files = os.listdir(pdf_path) # Storing the list of PDF in a var

# print(pdf_files) # For test
# for pdf in pdf_files: # This path is for test
#     print(pdf)

merger = PyPDF2.PdfWriter() # Making a merger object

for pdf in pdf_files:
    if pdf.endswith('.pdf'): # Checks if the file extension is PDF
        merger.append(f'{pdf_path}/{pdf}')

merger.write(f"{pdf_path}/merged-doc-pdf.pdf")
merger.close()