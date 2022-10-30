# Создать программу, которая создает pdf файл 3 страница произвольного текста
import os
import importlib.util
import sys

name = 'fpdf'

if name in sys.modules:
    pass
elif (spec := importlib.util.find_spec(name)) is not None:
    pass
else:
    os.system('python -m pip install fpdf')

from fpdf import FPDF

pdf = FPDF()
for _ in range(3):
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
pdf.output("simple_demo.pdf")
