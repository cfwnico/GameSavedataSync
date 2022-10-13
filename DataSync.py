# cfw
# 2022.10.13
import os
import sys
import time
from glob import glob

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Common import messagebox
from Config import Config, UserData
from UI.ui_MainW import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, config: Config, gamedata: UserData) -> None:
        super().__init__()
        self.config_obj = config
        self.game_data_obj = gamedata
        self.setupUi(self)
        # self.setup_connect()
        self.init_config()

    def setup_connect(self):
        self.gamelist_widget.currentItemChanged.connect(self.load_game_info)
        self.gamelist_widget.itemDoubleClicked.connect(self.attributes)
        self.add_game_btn.clicked.connect(self.add_game)

    def init_config(self):
        # get config
        config_dict = self.config_obj.get_config_dict()
        cloud_path = config_dict["cloud_path"]
        self.cloud_path_label.setText(cloud_path)

    def init_userdata(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = Config(r"Data\config.json")
    userdata = UserData(r"Data\userdata.json")
    main_window = MainWindow(config, userdata)
    main_window.show()
    app.exec()
