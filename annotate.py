from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Text
import os

RESOURCE_ROOT = os.path.dirname(__file__)

# Fill the writer with the pages you want
pdf_path = os.path.join(RESOURCE_ROOT, "E1.62.pdf")
reader = PdfReader(pdf_path)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Create the annotation and add it
annotation = Text(
    text="Hello World\nThis is the second line!",
    rect=(50, 550, 200, 650),
)

# Set annotation flags to 4 for printable annotations.
# See "AnnotationFlag" for other options, e.g. hidden etc.
annotation.flags = 4

writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)