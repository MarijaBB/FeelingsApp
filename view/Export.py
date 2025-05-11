# not finished

# export to pdf 
from fpdf import FPDF
from controller.HistoryController import read_formatted_history
#1. history
def to_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    text = read_formatted_history(6)
    history_formatted = read_formatted_history(text)
    print(history_formatted)
    for sentence in history_formatted:
        pdf.cell(40,10,sentence)
        pdf.ln()
    pdf_file = 'export.pdf'
    pdf.output(pdf_file,'F')

to_pdf()

#2. charts
def charts_to_pdf():
    pass
