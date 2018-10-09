pip install pdfminer3k

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import re

def readPDF(pdfFile):
    rscrmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rscrmgr, retstr, laparams=laparams)
    process_pdf(rscrmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = open("C:\\Users\\Max\\Desktop\\my_pdf_file.pdf", "rb")

pdf_text = readPDF(pdfFile)
content = re.sub('\n|\x0c', ' ', pdf_text)
