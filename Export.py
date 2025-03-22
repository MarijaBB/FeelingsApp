# export to pdf 
from fpdf import FPDF

#1. history
def txt_to_pdf(txt_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(txt_file, "r", encoding="utf-8") as file:
        for line in file:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
    pdf_file = 'export.pdf'
    pdf.output(pdf_file)

txt_to_pdf("history.txt")

#2. charts
def charts_to_pdf(txt_file):
    pass
#download pdf
def download_pdf(pdf_file):
    pass