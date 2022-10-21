from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from UI.ui_AddNewW import Ui_Dialog
from Common import messagebox
import os
from SyncManage import create_sync
from Config import UserData


class AddNewSyncWindow(QDialog, Ui_Dialog):
    def __init__(self, cloud_path: str) -> None:
        super().__init__()
        self.cloud_path = cloud_path
        self.userdata = UserData(r"Data\userdata.json")
        self.setupUi(self)

    def setup_connect(self):
        self.ok_btn.clicked.connect(self.ok_func)

    def ok_func(self):
        game_name = self.game_name_edit.text().strip()
        if game_name == "":
            return
        if not self.userdata.check_game_name(game_name):
            # this game alreay sync..
            return
        local_savepath = self.savedata_edit.text()
        if os.path.exists(local_savepath):
            local_savepath = os.path.normpath(local_savepath)
        else:
            return
        # need add code for process game icon...
        ncd_datapath = os.path.join(self.cloud_path, game_name)
        result = create_sync(local_savepath, ncd_datapath)
        if result:  # need get now time code...
            sync_info_dict = {
                "game_name": game_name,
                "savedata_path": local_savepath,
                "create_time": "time str",
            }
            # wirte json file
            self.userdata.create_sync_info(game_name, sync_info_dict)
        else:
            messagebox(self, QMessageBox.Critical, "错误", result)
