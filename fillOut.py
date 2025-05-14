from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Text
import os

RESOURCE_ROOT = os.path.dirname(__file__)

# Fill the writer with the pages you want
pdf_path = os.path.join(RESOURCE_ROOT, "E1.62.pdf") #consider making this a variable in the configuration options
reader = PdfReader(pdf_path)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)
writer.reattach_fields()

fields = reader.get_fields()
print("these are the available fields", fields)
# Fill the form fields
for field in fields:
    print(field)
    if field.get("/FT") == "/Btn":
        # Check if the field is a button
        print("Button field found:", field.get("/T"))
    else:
        # Handle other types of fields (e.g., text fields)
        print("Text field found:", field.get("/T"))

writer.append(reader)

writer.update_page_form_field_values(
    writer.pages[0],
    {"fieldname": "some filled in text"},
    auto_regenerate=False,
)

with open("filled-out.pdf", "wb") as output_stream:
    writer.write(output_stream)