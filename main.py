import events
import sys
import var
from ventana import *


class Main(QtWidgets.QMainWindow):
    """Clase principal del programa"""

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        var.ui.pushButton_descargar.clicked.connect(events.Eventos.web_download)

        var.ui.statusbar.addPermanentWidget(var.ui.labelstatusbar, 1)


if __name__ == '__main__':
    '''Ejecución del programa'''
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
