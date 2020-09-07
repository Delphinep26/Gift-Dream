from PyQt5.QtCore import QCoreApplication, QRect, Qt,QMetaObject
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialogButtonBox, QFileDialog,\
    QGridLayout,QLabel,QLineEdit, QToolButton, QHBoxLayout
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QDialog
import json


class Ui_DialogSettings(QWidget):

    def __init__(self,parent, transaction_file_name,transaction_file_name_v2, main_folder_name,distribution_file_name, settings_file):
        super().__init__()
        self.parent = parent
        self.transaction_file_name = transaction_file_name
        self.transaction_file_name_v2 = transaction_file_name_v2
        self.distribution_file_name = distribution_file_name
        self.main_folder_name = main_folder_name
        self.settings_file = settings_file

    def setupUi(self, dialog):

        dialog.setObjectName("Dialog")
        dialog.resize(500, 155)
        self.gridLayoutWidget_2 = QWidget(dialog)
        self.gridLayoutWidget_2.setGeometry(QRect(5, 5, 490, 100))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.companies_label = QLabel(self.gridLayoutWidget_2)
        self.companies_label.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.companies_label, 0, 2, 1, 1)
        self.trans_label = QLabel(self.gridLayoutWidget_2)
        self.trans_label.setObjectName("label_8")
        self.trans_label_v2 = QLabel(self.gridLayoutWidget_2)
        self.trans_label_v2.setObjectName("label_8")

        self.main_folder_label = QLabel(self.gridLayoutWidget_2)
        self.main_folder_label.setObjectName("main_folder_label")

        self.gridLayout_3.addWidget(self.trans_label, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.trans_label_v2, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.main_folder_label, 3, 2, 1, 1)

        self.trans_file = QLineEdit(self.gridLayoutWidget_2)
        self.trans_file.setObjectName("trans_file")
        self.trans_file.setReadOnly(True)

        self.trans_file_v2 = QLineEdit(self.gridLayoutWidget_2)
        self.trans_file_v2.setObjectName("trans_file")
        self.trans_file_v2.setReadOnly(True)

        self.main_folder = QLineEdit(self.gridLayoutWidget_2)
        self.main_folder.setObjectName("main_folder")
        self.main_folder.setReadOnly(True)

        # self.gift_codes_button = QToolButton(self.gridLayoutWidget_2)
        # # iconfolder = QIcon()
        # # iconfolder.addPixmap(QPixmap("./icons/folder.svg"), QIcon.Normal, QIcon.Off)
        # # self.gift_codes_button.setIcon(iconfolder)
        # self.gift_codes_button.setObjectName("gift_codes_button")
        #
        # # self.gift_codes_button.clicked.connect(lambda: self._open_file_gifts_codes('main_folder'))
        #self.gridLayout_3.addWidget(self.gift_codes_button, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.trans_file, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.trans_file_v2, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.main_folder, 3, 1, 1, 1)

        self.no_dist_file = QLineEdit(self.gridLayoutWidget_2)
        self.no_dist_file.setObjectName("no_dist_file")
        self.no_dist_file.setReadOnly(True)
        self.gridLayout_3.addWidget(self.no_dist_file, 0, 1, 1, 1)

        self.toolButton_5 = QToolButton(self.gridLayoutWidget_2)
        iconexcel = QIcon()
        iconexcel.addPixmap(QPixmap("./icons/excel.svg"), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(iconexcel)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_3.addWidget(self.toolButton_5, 1, 0, 1, 1)
        self.toolButton_5.clicked.connect(lambda: self._open_file_dialog('trans'))

        self.trans_v2_button = QToolButton(self.gridLayoutWidget_2)
        self.trans_v2_button.setIcon(iconexcel)
        self.trans_v2_button.setObjectName("trans_v2_button")
        self.gridLayout_3.addWidget(self.trans_v2_button, 2, 0, 1, 1)
        self.trans_v2_button.clicked.connect(lambda: self._open_file_dialog('trans_v2'))

        self.main_folder_button = QToolButton(self.gridLayoutWidget_2)
        iconfolder = QIcon()
        iconfolder.addPixmap(QPixmap("./icons/folder.svg"), QIcon.Normal, QIcon.Off)
        self.main_folder_button.setIcon(iconfolder)
        self.main_folder_button.setObjectName("main_folder_button")
        self.gridLayout_3.addWidget(self.main_folder_button, 3, 0, 1, 1)
        self.main_folder_button.clicked.connect(lambda: self._open_file_dialog('main_folder'))



        self.toolButton_6 = QToolButton(self.gridLayoutWidget_2)
        self.toolButton_6.setIcon(iconexcel)
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout_3.addWidget(self.toolButton_6, 0, 0, 1, 1)
        self.toolButton_6.clicked.connect(lambda: self._open_file_dialog('no_dis'))
        self.gridLayout_3.addWidget(self.toolButton_6, 0, 0, 1, 1)
        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QRect(150, 120, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setObjectName("Save")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # init data
        self.no_dist_file.setText(self.distribution_file_name)
        self.trans_file.setText(self.transaction_file_name)
        self.trans_file_v2.setText(self.transaction_file_name_v2)
        self.main_folder.setText(self.main_folder_name)

        # Extract data
        self.buttonBox.accepted.connect(self.__save)
        self.buttonBox.rejected.connect(dialog.reject)
        QMetaObject.connectSlotsByName(dialog)

        self.retranslateUi(dialog)
        return self.gridLayoutWidget_2

    def retranslateUi(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "הגדרת קבצים"))
        self.companies_label.setText(_translate("Dialog", "קובץ לא להפצה"))
        self.trans_label.setText(_translate("Dialog", "קובץ עסקאות 200"))
        self.trans_label_v2.setText(_translate("Dialog", "קובץ עסקאות 1220"))
        self.main_folder_label.setText(_translate("Dialog", "תיקיית חג ראשית"))

    def _open_file_dialog(self, name):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if name == "no_dis":
            file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Excel (*.csv)", options=options)
            self.no_dist_file.setText('{}'.format(file))
        elif name == "trans":
            file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Excel (*.csv)", options=options)
            self.trans_file.setText('{}'.format(file))
        elif name == "trans_v2":
            file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Excel (*.csv)", options=options)
            self.trans_file_v2.setText('{}'.format(file))
        elif name == "main_folder":
            directory = str(QFileDialog.getExistingDirectory())
            self.main_folder.setText('{}'.format(directory))

    def __save(self):

        if self.no_dist_file.text() != "" and self.trans_file.text() != "" \
                and self.trans_file_v2.text() != "" and self.main_folder.text() != "":
            buttonReply = QMessageBox.question(self, 'שמירת הגדרות', "האם אתה בטוח שאתה רוצה לשמור?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes :
                with open(self.settings_file) as json_file:
                    settings = json.load(json_file)
                settings['קובץ לא להפצה'] = self.no_dist_file.text()
                settings['קובץ עסקאות'] = self.trans_file.text()
                settings['קובץ עסקאות 200'] = self.trans_file_v2.text()
                settings['תיקייה ראשית'] = self.main_folder.text()

                with open(self.settings_file, 'w') as outfile:
                    json.dump(settings, outfile)

                QMessageBox.about(self, "נשמר בהצלחה", "הנתונים נשמרו בהצלחה, הפעל מחדש")

                print('Saved.')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    Dialog.ui = Ui_DialogSettings("","", "", ""," ")
    Dialog.ui.setupUi(Dialog)
    Dialog.exec_()
    Dialog.show()
