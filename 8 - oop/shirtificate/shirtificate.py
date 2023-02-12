from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 10, 70, 190)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 50)
        # Moving cursor to the right:
        self.cell(180)


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.text(35,40,"CS50 Shirtificate")
pdf.set_font(size=25)
pdf.set_text_color(r=255,g=255,b=255)
pdf.text(70,140, input("Name: ")+" took CS50")
pdf.output("shirtificate.pdf")