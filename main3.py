from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QFileDialog, QMessageBox, 
    QComboBox, QRadioButton, QButtonGroup, QHBoxLayout
)
import sys
import fitz  # PyMuPDF
import time
# Add this import to use your Modbus reading function
from clienttest import read_first_six_3000_parameters


class PDFTemplateApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AVL Load Tester")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # create input fields
        self.modbus_ip = QLineEdit(text="192.168.13.51")
        self.tester_input = QLineEdit()
        self.owner_input = QLineEdit()
        self.address_input = QLineEdit()
        self.hoist_desc_input = QLineEdit()
        self.manufacturer_input = QLineEdit()
        self.model_input = QLineEdit()
        self.serial_no_input = QLineEdit()
        self.power_supply_input = QLineEdit()
        self.load_test_spec_input = QLineEdit()
        self.pounds_input = QLineEdit()
        self.man_spec_i_input = QLineEdit()
        self.actual_i_p1_input = QLineEdit()
        self.actual_i_p2_input = QLineEdit()
        self.actual_i_p3_input = QLineEdit()
        self.comments_input = QLineEdit()

        # dropdown list for rated capacity field
        self.rated_cap_dropdown = QComboBox()
        self.rated_cap_dropdown.addItems(["1/4 ton", "1/2 ton", "1 ton", "2 ton"])

        # create radio button option for overload
        self.overload_yes = QRadioButton("Yes")
        self.overload_no = QRadioButton("No")
        self.overload_group = QButtonGroup()
        self.overload_group.addButton(self.overload_yes)
        self.overload_group.addButton(self.overload_no)
        overload_layout = QHBoxLayout()
        overload_layout.addWidget(self.overload_yes)
        overload_layout.addWidget(self.overload_no)


        # Add input fields to the layout with labels
        form_layout.addRow("Modbus IP:", self.modbus_ip)
        form_layout.addRow("Tester:", self.tester_input)
        form_layout.addRow("Owner:", self.owner_input)
        form_layout.addRow("Address:", self.address_input)
        form_layout.addRow("Hoist Description:", self.hoist_desc_input)
        form_layout.addRow("Manufacturer:", self.manufacturer_input)
        form_layout.addRow("Model:", self.model_input)
        form_layout.addRow("Serial No.:", self.serial_no_input)
        form_layout.addRow("Power Supply:", self.power_supply_input)
        form_layout.addRow("Rated Capacity:", self.rated_cap_dropdown)
        form_layout.addRow("Load Test (Spec. 100-125%):", self.load_test_spec_input)
        form_layout.addRow("Pounds:", self.pounds_input)
        form_layout.addRow("Did Overload Protector Reject 230%?:", overload_layout)
        form_layout.addRow("Manufacturer's Spec - Current Draw:", self.man_spec_i_input)
        form_layout.addRow("Actual Current - Phase 1:", self.actual_i_p1_input)
        form_layout.addRow("Actual Current - Phase 2:", self.actual_i_p2_input)
        form_layout.addRow("Actual Current - Phase 3:", self.actual_i_p3_input)
        form_layout.addRow("Comments:", self.comments_input)

        layout.addLayout(form_layout)

        self.run_test_btn = QPushButton("Run Load Test")
        self.run_test_btn.clicked.connect(self.test_load)
        layout.addWidget(self.run_test_btn)

        self.generate_btn = QPushButton("Generate Report")
        self.generate_btn.clicked.connect(self.fill_pdf_template)
        layout.addWidget(self.generate_btn)

        self.setLayout(layout)

    # connect to modbus and write values to form
    def test_load(self):
        print("Test Running")

        params = read_first_six_3000_parameters(self.modbus_ip.text())
        
        if params:
            self.actual_i_p1_input.setText("{:.2f}".format(params.get("current_1")))
            self.actual_i_p2_input.setText("{:.2f}".format(params.get("current_2")))
            self.actual_i_p3_input.setText("{:.2f}".format(params.get("current_3")))

        else:
            QMessageBox.warning(self, "Modbus Error", "Could not read all parameters or no Modbus connection.")


    def fill_pdf_template(self):
        owner = self.owner_input.text()
        tester = self.tester_input.text()
        address = self.address_input.text()
        hoist_desc = self.hoist_desc_input.text()
        manufacturer = self.manufacturer_input.text()
        model = self.model_input.text()
        serial_no = self.serial_no_input.text()
        power_supply = self.power_supply_input.text()
        rated_cap = self.rated_cap_dropdown.currentText()
        load_test_spec = self.load_test_spec_input.text()
        pounds = self.pounds_input.text()
        overload = "Yes" if self.overload_yes.isChecked() else "No"
        man_spec_i = self.man_spec_i_input.text()
        actual_i_p1 = self.actual_i_p1_input.text()
        actual_i_p2 = self.actual_i_p2_input.text()
        actual_i_p3 = self.actual_i_p3_input.text()
        comments = self.comments_input.text()
        cur_date = time.strftime("%d-%B-%Y")
        time_split = cur_date.split("-")

        if not owner or not hoist_desc or not address:
            QMessageBox.warning(self, "Missing Data", "Please fill in all fields.")
            return

        # Select PDF template
        template_path, _ = QFileDialog.getOpenFileName(self, "Open PDF Template", "", "PDF Files (*.pdf)")
        if not template_path:
            return

        # Select save location
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Filled PDF", f"{serial_no}_load_test_report.pdf", "PDF Files (*.pdf)")
        if not save_path:
            return

        try:
            doc = fitz.open(template_path)

            # Fill form fields (AcroForms)
            for page in doc:
                for field in page.widgets():
                    if field.field_name == "owner":
                        field.field_value = owner
                    elif field.field_name == "tester":
                        field.field_value = tester
                    elif field.field_name == "address":
                        field.field_value = address
                    elif field.field_name == "hoist_desc":
                        field.field_value = hoist_desc
                    elif field.field_name == "manufacturer":
                        field.field_value = manufacturer
                    elif field.field_name == "model":
                        field.field_value = model
                    elif field.field_name == "serial_no":
                        field.field_value = serial_no
                    elif field.field_name == "power_supply":
                        field.field_value = power_supply
                    elif field.field_name == "rated_cap":
                        field.field_value = rated_cap
                    elif field.field_name == "load_test_spec":
                        field.field_value = load_test_spec
                    elif field.field_name == "pounds":
                        field.field_value = pounds
                    elif field.field_name == "overload":
                        if field.field_type == fitz.PDF_WIDGET_TYPE_RADIOBUTTON:
                            if field.field_value != overload:
                                field.field_value = overload
                    elif field.field_name == "man_spec_i":
                        field.field_value = man_spec_i
                    elif field.field_name == "actual_i_p1":
                        field.field_value = actual_i_p1
                    elif field.field_name == "actual_i_p2":
                        field.field_value = actual_i_p2
                    elif field.field_name == "actual_i_p3":
                        field.field_value = actual_i_p3
                    elif field.field_name == "comments":
                        field.field_value = comments
                    elif field.field_name == "date":
                        field.field_value = time_split[0]
                    elif field.field_name == "month":
                        field.field_value = time_split[1]
                    elif field.field_name == "year":
                        field.field_value = time_split[2]
                    elif field.field_name == "full_date":
                        field.field_value = cur_date

                    field.update()

            doc.save(save_path)
            QMessageBox.information(self, "Success", f"PDF saved to:\n{save_path}")

            # Clear fields after save
            self.owner_input.clear()
            self.tester_input.clear()
            self.address_input.clear()
            self.hoist_desc_input.clear()
            self.manufacturer_input.clear()
            self.model_input.clear()
            self.serial_no_input.clear()
            self.power_supply_input.clear()
            self.load_test_spec_input.clear()
            self.pounds_input.clear()
            self.man_spec_i_input.clear()
            self.actual_i_p1_input.clear()
            self.actual_i_p2_input.clear()
            self.actual_i_p3_input.clear()
            self.comments_input.clear()

            # set dropdown list to 1st entry
            self.rated_cap_dropdown.setCurrentIndex(0)

            # reset radio buttons
            self.overload_group.setExclusive(False)
            self.overload_yes.setChecked(False)
            self.overload_no.setChecked(False)
            self.overload_group.setExclusive(True)



        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate PDF:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFTemplateApp()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
