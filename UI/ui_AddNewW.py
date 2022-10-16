# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewWJbtpFF.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 270)
        Dialog.setMinimumSize(QSize(600, 270))
        Dialog.setMaximumSize(QSize(600, 270))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.browse_icon_btn = QPushButton(self.groupBox)
        self.browse_icon_btn.setObjectName(u"browse_icon_btn")

        self.horizontalLayout.addWidget(self.browse_icon_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 2)

        self.game_name_edit = QLineEdit(self.groupBox)
        self.game_name_edit.setObjectName(u"game_name_edit")
        self.game_name_edit.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.game_name_edit, 1, 1, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.browse_savedata_btn = QPushButton(self.groupBox)
        self.browse_savedata_btn.setObjectName(u"browse_savedata_btn")

        self.horizontalLayout_2.addWidget(self.browse_savedata_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 5, 1, 1, 2)

        self.savedata_edit = QLineEdit(self.groupBox)
        self.savedata_edit.setObjectName(u"savedata_edit")
        self.savedata_edit.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.savedata_edit, 6, 1, 1, 2)

        self.icon_label = QLabel(self.groupBox)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMaximumSize(QSize(183, 183))
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.icon_label, 0, 0, 10, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.ok_btn = QPushButton(self.groupBox)
        self.ok_btn.setObjectName(u"ok_btn")

        self.horizontalLayout_3.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_3.addWidget(self.cancel_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 7, 1, 3, 2)

        self.icon_edit = QLineEdit(self.groupBox)
        self.icon_edit.setObjectName(u"icon_edit")
        self.icon_edit.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.icon_edit, 3, 1, 2, 2)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u540c\u6b65\u94fe\u63a5", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u540c\u6b65\u94fe\u63a5", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u56fe\u6807\uff1a", None))
        self.browse_icon_btn.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u6587\u4ef6", None))
        self.game_name_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u6e38\u620f\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u540d\u79f0\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u672c\u5730\u5b58\u6863\u8def\u5f84\uff1a", None))
        self.browse_savedata_btn.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u6587\u4ef6\u5939", None))
        self.savedata_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u70b9\u51fb\u6d4f\u89c8\u6587\u4ef6\u5939\uff0c\u9009\u62e9\u6e38\u620f\u5b58\u6863\u76ee\u5f55", None))
        self.icon_label.setText(QCoreApplication.translate("Dialog", u"\u65e0\u56fe\u6807", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.icon_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u70b9\u51fb\u6d4f\u89c8\u6587\u4ef6\u9009\u62e9\u6e38\u620f\u56fe\u6807\u6587\u4ef6", None))
    # retranslateUi

