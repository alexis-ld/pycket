from PyQt4 import QtGui
import addIPDialog
import validate


class AddIPGUI(QtGui.QDialog, addIPDialog.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

    def accept(self):
        errors = []
        if self.line_edit_add_ip.text():
            if not validate.ip_address(str(self.line_edit_add_ip.text())):
                errors.append("IP : invalid IP")
        if self.text_edit_add_ip.toPlainText():
            if not validate.multiple_ip_addresses(str(self.text_edit_add_ip.toPlainText())):
                errors.append("IP : invalid IPs")
        if len(errors):
            error_message = "Validation errors:\n"
            for error in errors:
                error_message = error_message + error + '\n'
                QtGui.QMessageBox.information(self, "Error", error_message)
        else:
            try:
                f = open('watchlist.txt', 'a')
                if self.line_edit_add_ip.text():
                    f.write(self.line_edit_add_ip.text() + '\n')
                if self.text_edit_add_ip:
                    f.write(self.text_edit_add_ip.toPlainText() + '\n')
                f.close()
            except:
                print 'File error:', sys.exc_info()[0]
            super(AddIPGUI, self).accept()
