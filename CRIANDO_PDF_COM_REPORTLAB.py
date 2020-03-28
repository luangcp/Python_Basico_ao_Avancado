"""
Criando PDF com reportlab
"""
# -*- coding: UTF-8 -*-
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("documento.pdf")
pdf.drawString(200, 300, "Teste de pdf")
pdf.save()