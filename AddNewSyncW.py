from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from UI.ui_AddNewW import Ui_Dialog
from Common import messagebox, get_now_time
import os
from SyncManage import create_sync
from Config import UserData
import traceback


class AddNewSyncWindow(QDialog, Ui_Dialog):
    def __init__(self, cloud_path: str) -> None:
        super().__init__()
        self.cloud_path = cloud_path
        self.userdata = UserData(r"Data\userdata.json")
        self.setupUi(self)
        self.setup_connect()

    def setup_connect(self):
        self.browse_savedata_btn.clicked.connect(self.browse_savedata_func)
        self.ok_btn.clicked.connect(self.ok_func)
        self.cancel_btn.clicked.connect(self.close)

    def browse_savedata_func(self):
        new_path = QFileDialog.getExistingDirectory(self, "打开游戏存档文件夹...")
        if new_path != "":
            self.savedata_edit.setText(new_path)
            # get game name.
            game_name = os.path.basename(os.path.split(new_path)[0])
            self.game_name_edit.setText(game_name)

    def ok_func(self):
        game_name = self.game_name_edit.text().strip()
        if game_name == "":  # check game name.
            messagebox(self, QMessageBox.Critical, "错误", "请输入游戏名称!")
            return
        if not self.userdata.check_game_name(game_name):
            messagebox(self, QMessageBox.Critical, "错误", "该游戏已存在同步链接!")
            return
        local_savepath = self.savedata_edit.text()
        # check local savedata path.
        if os.path.exists(local_savepath):
            local_savepath = os.path.normpath(local_savepath)
        else:
            messagebox(self, QMessageBox.Critical, "错误", "请检查本地存档路径!")
            return
        # need add code for process game icon...
        ncd_datapath = os.path.join(self.cloud_path, game_name)
        result = create_sync(local_savepath, ncd_datapath)
        if result is True:
            sync_info_dict = {
                "game_name": game_name,
                "savedata_path": local_savepath,
                "create_time": get_now_time(),
            }
            # wirte json file.
            self.userdata.create_sync_info(game_name, sync_info_dict)
        else:
            messagebox(self, QMessageBox.Critical, "错误", result)
