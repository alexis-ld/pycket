from PyQt4 import QtGui
import forgingDialog
import validate
from packet import Packet


class ForgingGUI(QtGui.QDialog, forgingDialog.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.combo_box_transport.currentIndexChanged.connect(self.transport_layer_changed)

    def transport_layer_changed(self, index):
        self.stacked_widget_transport.setCurrentIndex(index)

    def accept(self):
        errors = []
        if not validate.mac_address(str(self.line_edit_source_mac.text())):
            errors.append("Ethernet : invalid source MAC")
        if not validate.mac_address(str(self.line_edit_destination_mac.text())):
            errors.append("Ethernet : invalid destination MAC")
        if not validate.ip_address(str(self.line_edit_source_ip.text())):
            errors.append("IP : invalid source IP")
        if not validate.ip_address(str(self.line_edit_destination_ip.text())):
            errors.append("IP : invalid destination IP")
        if len(errors):
            error_message = "Validation errors:\n"
            for error in errors:
                error_message = error_message + error + '\n'
            QtGui.QMessageBox.information(self, "Error", error_message)
        else:
            super(ForgingGUI, self).accept()

    def get_packet(self):
        selected_transport_layer = self.combo_box_transport.currentIndex()
        packet = Packet()
        eth_layer = {}
        eth_layer["LayerType"] = "Ethernet"
        eth_layer["Source MAC"] = str(self.line_edit_source_mac.text())
        eth_layer["Destination MAC"] = str(self.line_edit_destination_mac.text())
        eth_layer["Type"] = 8
        ip_layer = {}
        ip_layer["LayerType"] = "IP"
        ip_layer["Source Address"] = str(self.line_edit_source_ip.text())
        ip_layer["Destination Address"] = str(self.line_edit_destination_ip.text())
        ip_layer["TTL"] = self.spin_box_ttl.value()
        ip_layer["Version"] = 4
        transport_layer = {}
        if selected_transport_layer == 0:
            ip_layer["Protocol"] = 6
            transport_layer["LayerType"] = "TCP"
            transport_layer["Source port"] = self.spin_box_tcp_source_port.value()
            transport_layer["Destination port"] = self.spin_box_tcp_destination_port.value()
            transport_layer["Sequence"] = self.spin_box_tcp_sequence.value()
            transport_layer["Acknowledgement"] = self.spin_box_tcp_acknowledgement.value()
            transport_layer["Data"] = str(self.line_edit_tcp_data.text())
        elif selected_transport_layer == 1:
            ip_layer["Protocol"] = 1
            transport_layer["LayerType"] = "ICMP"
            transport_layer["Type"] = self.spin_box_icmp_type.value()
            transport_layer["Code"] = self.spin_box_icmp_code.value()
            transport_layer["Data"] = str(self.line_edit_icmp_data.text())
        else:
            ip_layer["Protocol"] = 17
            transport_layer["LayerType"] = "UDP"
            transport_layer["Source port"] = self.spin_box_udp_source_port.value()
            transport_layer["Destination port"] = self.spin_box_udp_destination_port.value()
            transport_layer["Data"] = str(self.line_edit_udp_data.text())
        packet.add_layer(eth_layer)
        packet.add_layer(ip_layer)
        packet.add_layer(transport_layer)
        return packet
