# Form implementation generated from reading ui file '.\hm3u8dl_gui.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_hm3u8dl_gui(object):
    def setupUi(self, hm3u8dl_gui):
        hm3u8dl_gui.setObjectName("hm3u8dl_gui")
        hm3u8dl_gui.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        hm3u8dl_gui.resize(470, 492)
        font = QtGui.QFont()
        font.setPointSize(12)
        hm3u8dl_gui.setFont(font)
        hm3u8dl_gui.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDialableCharactersOnly|QtCore.Qt.InputMethodHint.ImhDigitsOnly|QtCore.Qt.InputMethodHint.ImhLowercaseOnly|QtCore.Qt.InputMethodHint.ImhPreferLowercase|QtCore.Qt.InputMethodHint.ImhPreferUppercase)
        self.layoutWidget = QtWidgets.QWidget(hm3u8dl_gui)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 20, 77, 66))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_update = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_update.setObjectName("pushButton_update")
        self.verticalLayout_2.addWidget(self.pushButton_update)
        self.pushButton_workDir = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_workDir.setObjectName("pushButton_workDir")
        self.verticalLayout_2.addWidget(self.pushButton_workDir)
        self.widget = QtWidgets.QWidget(hm3u8dl_gui)
        self.widget.setGeometry(QtCore.QRect(10, 390, 451, 45))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_enableDel = QtWidgets.QCheckBox(self.widget)
        self.checkBox_enableDel.setChecked(True)
        self.checkBox_enableDel.setTristate(False)
        self.checkBox_enableDel.setObjectName("checkBox_enableDel")
        self.gridLayout_2.addWidget(self.checkBox_enableDel, 0, 0, 1, 1)
        self.label_mergeMode = QtWidgets.QLabel(self.widget)
        self.label_mergeMode.setObjectName("label_mergeMode")
        self.gridLayout_2.addWidget(self.label_mergeMode, 0, 1, 1, 1)
        self.comboBox_mergeMode = QtWidgets.QComboBox(self.widget)
        self.comboBox_mergeMode.setObjectName("comboBox_mergeMode")
        self.comboBox_mergeMode.addItem("")
        self.comboBox_mergeMode.addItem("")
        self.comboBox_mergeMode.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_mergeMode, 0, 2, 1, 1)
        self.label_thread = QtWidgets.QLabel(self.widget)
        self.label_thread.setObjectName("label_thread")
        self.gridLayout_2.addWidget(self.label_thread, 0, 3, 1, 1)
        self.lineEdit_thread = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_thread.setObjectName("lineEdit_thread")
        self.gridLayout_2.addWidget(self.lineEdit_thread, 0, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_port = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.gridLayout.addWidget(self.lineEdit_port, 0, 1, 1, 1)
        self.label_port = QtWidgets.QLabel(self.widget)
        self.label_port.setObjectName("label_port")
        self.gridLayout.addWidget(self.label_port, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 5, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(hm3u8dl_gui)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 20, 291, 68))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_verison = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_verison.sizePolicy().hasHeightForWidth())
        self.lineEdit_verison.setSizePolicy(sizePolicy)
        self.lineEdit_verison.setObjectName("lineEdit_verison")
        self.verticalLayout_3.addWidget(self.lineEdit_verison)
        self.lineEdit_workDir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_workDir.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_workDir.setText("")
        self.lineEdit_workDir.setObjectName("lineEdit_workDir")
        self.verticalLayout_3.addWidget(self.lineEdit_workDir)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.splitter = QtWidgets.QSplitter(hm3u8dl_gui)
        self.splitter.setGeometry(QtCore.QRect(91, 255, 371, 26))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEdit_key = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.comboBox_key = QtWidgets.QComboBox(self.splitter)
        self.comboBox_key.setObjectName("comboBox_key")
        self.comboBox_key.addItem("")
        self.comboBox_key.addItem("")
        self.comboBox_key.addItem("")
        self.comboBox_key.addItem("")
        self.comboBox_key.addItem("")
        self.comboBox_key.addItem("")
        self.comboBox_key.addItem("")
        self.layoutWidget2 = QtWidgets.QWidget(hm3u8dl_gui)
        self.layoutWidget2.setGeometry(QtCore.QRect(91, 292, 371, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_nonce = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_nonce.setObjectName("lineEdit_nonce")
        self.verticalLayout_5.addWidget(self.lineEdit_nonce)
        self.lineEdit_iv = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_iv.setObjectName("lineEdit_iv")
        self.verticalLayout_5.addWidget(self.lineEdit_iv)
        self.lineEdit_proxy = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_proxy.setObjectName("lineEdit_proxy")
        self.verticalLayout_5.addWidget(self.lineEdit_proxy)
        self.layoutWidget3 = QtWidgets.QWidget(hm3u8dl_gui)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 22, 78, 371))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_verison = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_verison.setFont(font)
        self.label_verison.setObjectName("label_verison")
        self.verticalLayout.addWidget(self.label_verison)
        self.label_workDir = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_workDir.setFont(font)
        self.label_workDir.setObjectName("label_workDir")
        self.verticalLayout.addWidget(self.label_workDir)
        self.label_m3u8url = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_m3u8url.setFont(font)
        self.label_m3u8url.setObjectName("label_m3u8url")
        self.verticalLayout.addWidget(self.label_m3u8url)
        self.label_title = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.label_headers = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_headers.setFont(font)
        self.label_headers.setObjectName("label_headers")
        self.verticalLayout.addWidget(self.label_headers)
        self.label_baseurl = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_baseurl.setFont(font)
        self.label_baseurl.setObjectName("label_baseurl")
        self.verticalLayout.addWidget(self.label_baseurl)
        self.label_key = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_key.setFont(font)
        self.label_key.setObjectName("label_key")
        self.verticalLayout.addWidget(self.label_key)
        self.label_nonce = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nonce.setFont(font)
        self.label_nonce.setObjectName("label_nonce")
        self.verticalLayout.addWidget(self.label_nonce)
        self.label_iv = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_iv.setFont(font)
        self.label_iv.setObjectName("label_iv")
        self.verticalLayout.addWidget(self.label_iv)
        self.label_proxy = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_proxy.setFont(font)
        self.label_proxy.setObjectName("label_proxy")
        self.verticalLayout.addWidget(self.label_proxy)
        self.layoutWidget4 = QtWidgets.QWidget(hm3u8dl_gui)
        self.layoutWidget4.setGeometry(QtCore.QRect(91, 97, 371, 151))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_m3u8url = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_m3u8url.setObjectName("lineEdit_m3u8url")
        self.verticalLayout_4.addWidget(self.lineEdit_m3u8url)
        self.lineEdit_title = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout_4.addWidget(self.lineEdit_title)
        self.lineEdit_headers = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_headers.setObjectName("lineEdit_headers")
        self.verticalLayout_4.addWidget(self.lineEdit_headers)
        self.lineEdit_baseurl = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_baseurl.setObjectName("lineEdit_baseurl")
        self.verticalLayout_4.addWidget(self.lineEdit_baseurl)
        self.widget1 = QtWidgets.QWidget(hm3u8dl_gui)
        self.widget1.setGeometry(QtCore.QRect(10, 450, 451, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_data = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.horizontalLayout_5.addWidget(self.lineEdit_data)
        self.pushButton_start = QtWidgets.QPushButton(self.widget1)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_5.addWidget(self.pushButton_start)

        self.retranslateUi(hm3u8dl_gui)
        self.comboBox_mergeMode.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(hm3u8dl_gui)

    def retranslateUi(self, hm3u8dl_gui):
        _translate = QtCore.QCoreApplication.translate
        hm3u8dl_gui.setWindowTitle(_translate("hm3u8dl_gui", "hm3u8dl_gui"))
        self.pushButton_update.setText(_translate("hm3u8dl_gui", "检查更新"))
        self.pushButton_workDir.setText(_translate("hm3u8dl_gui", "选择"))
        self.checkBox_enableDel.setText(_translate("hm3u8dl_gui", "删除分片"))
        self.label_mergeMode.setText(_translate("hm3u8dl_gui", "合并方式"))
        self.comboBox_mergeMode.setCurrentText(_translate("hm3u8dl_gui", "3"))
        self.comboBox_mergeMode.setItemText(0, _translate("hm3u8dl_gui", "1"))
        self.comboBox_mergeMode.setItemText(1, _translate("hm3u8dl_gui", "2"))
        self.comboBox_mergeMode.setItemText(2, _translate("hm3u8dl_gui", "3"))
        self.label_thread.setText(_translate("hm3u8dl_gui", "线程数"))
        self.lineEdit_thread.setText(_translate("hm3u8dl_gui", "16"))
        self.lineEdit_port.setText(_translate("hm3u8dl_gui", "8000"))
        self.label_port.setText(_translate("hm3u8dl_gui", "端口号"))
        self.lineEdit_key.setWhatsThis(_translate("hm3u8dl_gui", "<html><head/><body><p>这是key</p></body></html>"))
        self.comboBox_key.setItemText(0, _translate("hm3u8dl_gui", "None"))
        self.comboBox_key.setItemText(1, _translate("hm3u8dl_gui", "AES-128-CBC"))
        self.comboBox_key.setItemText(2, _translate("hm3u8dl_gui", "AES-128-ECB"))
        self.comboBox_key.setItemText(3, _translate("hm3u8dl_gui", "SAMPLE-AES-CTR"))
        self.comboBox_key.setItemText(4, _translate("hm3u8dl_gui", "SAMPLE-AES"))
        self.comboBox_key.setItemText(5, _translate("hm3u8dl_gui", "cbcs"))
        self.comboBox_key.setItemText(6, _translate("hm3u8dl_gui", "copyrightDRM"))
        self.label_verison.setText(_translate("hm3u8dl_gui", "版本号"))
        self.label_workDir.setText(_translate("hm3u8dl_gui", "工作目录"))
        self.label_m3u8url.setText(_translate("hm3u8dl_gui", "m3u8地址"))
        self.label_title.setText(_translate("hm3u8dl_gui", "标题"))
        self.label_headers.setText(_translate("hm3u8dl_gui", "headers"))
        self.label_baseurl.setText(_translate("hm3u8dl_gui", "baseurl"))
        self.label_key.setText(_translate("hm3u8dl_gui", "key"))
        self.label_nonce.setText(_translate("hm3u8dl_gui", "nonce"))
        self.label_iv.setText(_translate("hm3u8dl_gui", "iv"))
        self.label_proxy.setText(_translate("hm3u8dl_gui", "代理"))
        self.pushButton_start.setText(_translate("hm3u8dl_gui", "Start!"))
