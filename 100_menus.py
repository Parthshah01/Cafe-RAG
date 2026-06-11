from reportlab.pdfgen import canvas

for i in range(1, 101):

    pdf = canvas.Canvas(f"pdfs/menu_{i}.pdf")

    pdf.drawString(100, 750, f"Cafe Menu {i}")
    pdf.drawString(100, 720, f"Espresso - ₹{100+i}")
    pdf.drawString(100, 700, f"Cappuccino - ₹{150+i}")
    pdf.drawString(100, 680, f"Latte - ₹{180+i}")

    pdf.save()

print("100 PDFs created")