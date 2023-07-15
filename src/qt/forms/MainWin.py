from config.config import CLIENTS
from src.models.Dev import Dev
from src.qt.UI.UI_MainWin import Ui_MainWindow


class MainWin(Ui_MainWindow):
    def __init__(self, modules, MainWindow):
        self.modules = modules
        self.change_module = None
        self.MainWindow = MainWindow

    def setupUi(self, window):
        super().setupUi(self.MainWindow)
        self.add_devices(self.modules)

    def add_devices(self, modules):
        self.module_changed(0)
        for module in range(len(modules)):
            self.device_box.addItem(modules[module].get("name"))
        self.device_box.currentIndexChanged.connect(self.module_changed)

    def module_changed(self, module, client=CLIENTS[1]):
        self.change_module = Dev(client, self.modules[module])
        print(self.change_module)
