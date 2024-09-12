from PyPDF2 import PdfReader
from PyPDF2.generic import AnnotationBuilder
from PyPDF2 import PdfWriter

with open("file.pdf", "rb") as pdf_file:
    pdf_reader = PdfReader(pdf_file)
    page_number = 0  
    page = pdf_reader.pages[page_number]
    output_pdf = PdfWriter()
    output_pdf.add_page(page)
    
    x, y = 50, 640 

    hyperlink = AnnotationBuilder.link(
        url="https://", 
        rect=[x, y, x + 120, y + 20],
    )

    hyperlink_2 = AnnotationBuilder.link(
        url = "https://",
        rect = [x, y-23, x+100, y-3]
    )
    output_pdf.add_annotation(page_number=0, annotation = hyperlink)
    output_pdf.add_annotation(page_number=0, annotation = hyperlink_2)

    with open("output.pdf", "wb") as output_file:
        output_pdf.write(output_file)
