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
from SyncManage import check_sync_status


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, config: Config, userdata: UserData) -> None:
        super().__init__()
        self.config_obj = config
        self.userdata_obj = userdata
        self.setupUi(self)
        self.setup_connect()
        self.init_config()
        self.init_cloudata()

    def setup_connect(self):
        self.sync_listwidget.currentItemChanged.connect(self.change_current_item)
        self.open_cloudata_btn.clicked.connect(self.open_cloudata_path)
        # self.gamelist_widget.itemDoubleClicked.connect(self.attributes)
        # self.add_game_btn.clicked.connect(self.add_game)

    def init_config(self):
        """load config.json data."""
        config_dict = self.config_obj.get_config_dict()
        self.cloud_path = config_dict["cloud_path"]
        self.cloud_path_label.setText(self.cloud_path)

    def init_cloudata(self):
        """scan cloud_path dir,and add item to listwidget."""
        for i in os.scandir(self.cloud_path):
            if i.is_dir():
                item = QListWidgetItem()
                item.setText(i.name)
                path = os.path.normpath(i.path)
                item.setData(Qt.UserRole, path)
                self.sync_listwidget.addItem(item)
        self.sync_listwidget.setCurrentRow(0)

    def change_current_item(self, item: QListWidgetItem):
        """when change select item this func will be run.
        read game sync info and update some label text."""
        game_name = item.text()
        cloudata_path = item.data(Qt.UserRole)
        for i in os.scandir(cloudata_path):
            if i.is_dir():
                self.cloudata_path_label.setText(i.path)
        self.load_sync_info(self.userdata_obj.get_savedata_sync_info(game_name))

    def load_sync_info(self, sync_info: dict):
        """read game sync info from userdata.json and set this in label text."""
        if sync_info is None:
            self.gamename_label.setText("未找到该云存档对应的信息")
            self.savepath_label.setText("未找到该云存档对应的信息")
        else:
            # set text in label
            game_name = sync_info["game_name"]
            self.gamename_label.setText(game_name)
            savedata_path = os.path.normpath(sync_info["savedata_path"])
            self.savepath_label.setText(savedata_path)
            create_time = sync_info["create_time"]
            self.create_time_label.setText(create_time)
            # check sync status
            cloudata_path = self.cloudata_path_label.text()
            result = check_sync_status(savedata_path, cloudata_path)
            if isinstance(result, dict):
                stuts_str = result["status"] + " " + result["time"]
            elif result is False:
                # savedata path is not sym link.
                stuts_str = ""
            elif result is None:
                # savedata path not exists.
                # savedata path is a file.
                # error path.
                stuts_str = ""
            self.sync_status_label.setText(stuts_str)

    def open_cloudata_path(self):
        """open cloudata path with explorer."""
        path = self.cloudata_path_label.text()
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox(self, QMessageBox.Critical, "错误!", "该文件夹不存在!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = Config(r"Data\config.json")
    userdata = UserData(r"Data\userdata.json")
    main_window = MainWindow(config, userdata)
    main_window.show()
    app.exec()
