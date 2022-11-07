# cfw
# 2022.10.13
import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from AddNewSyncW import AddNewSyncWindow
from Common import messagebox
from Config import Config, UserData
from SyncManage import check_sync_status, del_sync
from UI.ui_MainW import Ui_MainWindow


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
        # self.gamelist_widget.itemDoubleClicked.connect(self.attributes)
        self.create_sync_btn.clicked.connect(self.create_sync_func)
        self.fix_sync_btn.clicked.connect(self.fix_sync_func)
        self.del_sync_btn.clicked.connect(self.del_sync_func)
        self.check_sync_btn.clicked.connect(self.check_sync_func)
        self.open_cloud_btn.clicked.connect(self.open_cloud_func)
        self.edit_cloud_btn.clicked.connect(self.edit_cloud_func)
        self.open_cloudata_btn.clicked.connect(self.open_cloudata_path_func)
        self.edit_savedata_btn.clicked.connect(self.edit_savedata_func)
        self.about_btn.clicked.connect(self.about_func)

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
        re = self.load_sync_info(self.userdata_obj.get_savedata_sync_info(game_name))
        if re is False:
            item.setForeground(Qt.red)

    def load_sync_info(self, sync_info: dict):
        """read game sync info from userdata.json and set this in label text."""
        if sync_info is None:
            self.gamename_label.setText("未找到该云存档对应的信息")
            self.savepath_label.setText("未找到该云存档对应的信息")
            return False
        else:
            # set text in label.
            # set game name.
            game_name = sync_info["game_name"]
            self.gamename_label.setText(game_name)
            # set game icon.
            icon_path = "Image/" + game_name
            if os.path.exists(icon_path):
                self.icon_label.setPixmap(QPixmap(icon_path))
            # set savedata path text.
            savedata_path = os.path.normpath(sync_info["savedata_path"])
            self.savepath_label.setText(savedata_path)
            # set create time text.
            create_time = sync_info["create_time"]
            self.create_time_label.setText(create_time)
            # check sync status and set text.
            cloudata_path = self.cloudata_path_label.text()
            result = check_sync_status(savedata_path, cloudata_path)
            if isinstance(result, dict):
                stuts_str = result["status"] + "\n" + result["time"]
            elif result is False:
                # savedata path is not sym link.
                stuts_str = "本地存档未与云存档建立链接"
            elif result is None:
                # savedata path not exists.
                # savedata path is a file.
                # error path.
                stuts_str = "本地存档路径错误"
            self.sync_status_label.setText(stuts_str)
            return True

    def create_sync_func(self):
        AddNewSyncWindow(self.cloud_path_label.text()).exec()

    def fix_sync_func(self):
        pass

    def del_sync_func(self):
        req = messagebox(
            self,
            QMessageBox.Critical,
            "警告",
            "你即将取消云存档同步！存档会从云同步文件夹还原回本地游戏文件夹中！",
            "yesno",
        )
        if req == 1:
            return
        # before delet symlink,backup game savedata.
        game_name = self.gamename_label.text()
        os.makedirs
        # delet sync
        ncd_savepath = self.cloudata_path_label.text()
        local_savepath = self.savepath_label.text()
        ncdgame_path = os.path.split(ncd_savepath)[0]
        result = del_sync(local_savepath, ncdgame_path)
        if result:
            messagebox(self, QMessageBox.Information, "成功", "云端文件夹存档已还原回本地游戏文件夹！")
            # write json file.

        else:
            messagebox(self, QMessageBox.Critical, "错误", "删除同步链接失败！")

    def check_sync_func(self):
        req = messagebox(
            self,
            QMessageBox.Information,
            "提示",
            "即将开始检查所有的游戏存档同步信息，如果游戏存档较多可能会花费较长时间。",
            "yesno",
        )
        if req == 0:
            count = self.sync_listwidget.count()
            for i in range(count):
                self.sync_listwidget.setCurrentRow(i)
            self.sync_listwidget.setCurrentRow(0)

    def about_func(self):
        with open(r"Data\\ReadMe.txt", encoding="utf8") as text:
            messagebox(self, QMessageBox.Information, "关于...", text.read())

    def open_cloud_func(self):
        path = self.cloud_path_label.text()
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox(self, QMessageBox.Critical, "错误", "同步文件夹不存在，请检查路径。")

    def edit_cloud_func(self):
        req = messagebox(
            self, QMessageBox.Warning, "警告", "修改同步文件夹不会改变任何已存在的同步链接！", "yesno"
        )
        if req == 0:  # OK scene
            new_cloud_path = QFileDialog.getExistingDirectory(
                self, "请选择游戏文件夹...", self.cloud_path_label.text()
            )
            if new_cloud_path == "":
                return
            new_cloud_path = os.path.normpath(new_cloud_path)
            self.cloud_path_label.setText(new_cloud_path)
            self.config_obj.save_config("cloud_path", new_cloud_path)
        elif req == 1:  # Cancel scene
            return

    def edit_savedata_func(self):
        pass

    def open_cloudata_path_func(self):
        """open cloudata path with explorer."""
        path = self.cloudata_path_label.text()
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox(self, QMessageBox.Critical, "错误", "云存个档不存在，请检查路径。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = Config(r"Data\config.json")
    userdata = UserData(r"Data\userdata.json")
    main_window = MainWindow(config, userdata)
    main_window.show()
    app.exec()
