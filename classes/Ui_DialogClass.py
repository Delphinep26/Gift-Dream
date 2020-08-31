from PyQt5.QtCore import QCoreApplication, QRect, Qt, QMetaObject
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialogButtonBox, QFileDialog,\
    QGridLayout,QLabel,QLineEdit, QToolButton, QHBoxLayout
from classes.ExtractDataClass import *
from pandas import ExcelFile

class Ui_Dialog(QWidget):

    def _open_folder_dialog(self, name):

        directory = str(QFileDialog.getExistingDirectory())
        self.lineEdit_7.setText('{}'.format(directory)) if name == 'input' else self.lineEdit_6.setText(
            '{}'.format(directory))

    def _open_file_dialog(self, name):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if name == "no_dis":
            file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Excel (*.csv)", options=options)
            self.lineEdit_4.setText('{}'.format(file))
        elif name == "trans":
            file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Excel (*.csv)", options=options)
            self.lineEdit_5.setText('{}'.format(file))

    def extract_data(self):
        try:
            distribution_file_name = self.lineEdit_4.text()
            transaction_file_name = self.lineEdit_5.text()
            output_folder = self.lineEdit_6.text()

            extract = ExtractData(transaction_file_name=transaction_file_name,
                                  distribution_file_name=distribution_file_name,
                                  output_folder=output_folder,
                                  transation_cols=self.transation_cols)

        except FileNotFoundError:
            QMessageBox.about(self, "Failed", "קובץ הגדרות לא קיים")
        except KeyError:
            QMessageBox.about(self, "Failed", "בעיה בקובץ הגדרות")
        except Exception :
            QMessageBox.about(self, "Failed", "בעיה בקובץ הגדרות")

        try:

            extract.extract_all()
            extract.load_data()
            QMessageBox.about(self, "Success", "הטעינה בוצעה בהצלחה!")
            QCoreApplication.instance().quit()


        except PermissionError as e:
            QMessageBox.about(self, "Failed", "קובץ יצוא פתוח")
        except FileNotFoundError:
            QMessageBox.about(self, "Failed", "קובץ לא נמצא")
        except ValueError:
            QMessageBox.about(self, "Failed", "אין נתונים באחד מהקבצים או יתכן והזנת נתונים שגויים")
        except KeyError as key_err:
            QMessageBox.about(self, "Failed","עמודות חסרות בקובץ עסקאות, בדוק את קובץ הגדרות")
        except Exception:
            QMessageBox.about(self, "Failed", "שם גיליון לא קיים/מס' עמודה לא תקין/מס' שורה לא תקין")

    def setupUi(self, dialog):

        dialog.setObjectName("Dialog")
        dialog.resize(446, 200)

        self.gridLayoutWidget = QWidget(dialog)
        self.gridLayoutWidget.setGeometry(QRect(10, 140, 411, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 7, 1, 1)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 7, 1, 1)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 7, 1, 1)
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 4, 1, 1)
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 5, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 6, 1, 1)
        self.gridLayoutWidget_2 = QWidget(dialog)
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 411, 108))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 2, 1, 1)
        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 2, 1, 1)
        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 2, 1, 1)
        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.gridLayout_3.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        icon = QIcon()
        icon.addPixmap(QPixmap("./icons/folder.svg"), QIcon.Normal, QIcon.Off)
        self.toolButton_4 = QToolButton(self.gridLayoutWidget_2)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout_3.addWidget(self.toolButton_4, 3, 0, 1, 1)
        self.toolButton_4.clicked.connect(lambda: self._open_folder_dialog('output'))

        self.toolButton_5 = QToolButton(self.gridLayoutWidget_2)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("./icons/excel.svg"), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_3.addWidget(self.toolButton_5, 1, 0, 1, 1)
        self.toolButton_5.clicked.connect(lambda: self._open_file_dialog('trans'))
        self.toolButton_6 = QToolButton(self.gridLayoutWidget_2)
        self.toolButton_6.setIcon(icon1)
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout_3.addWidget(self.toolButton_6, 0, 0, 1, 1)
        self.toolButton_6.clicked.connect(lambda: self._open_file_dialog('no_dis'))
        self.gridLayout_3.addWidget(self.toolButton_6, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QWidget(dialog)
        self.horizontalLayoutWidget.setGeometry(QRect(142, 230, 280, 100))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.label_15 = QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)

        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QRect(80, 150, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        try:
        #Extract Settings
            settings_file = './Settings//settings.xlsx'
            xls = ExcelFile(settings_file)

            df = xls.parse('קובץ עסקאות')
            self.transation_cols = list(df['Column Name'])
            url_settings = xls.parse('קישורים')

            # init data
            self.lineEdit_4.setText(url_settings['קובץ לא להפצה'][0])
            self.lineEdit_5.setText(url_settings['קובץ עסקאות'][0])
            self.lineEdit_6.setText(url_settings['תיקיית יצוא'][0])

        except FileNotFoundError:
            QMessageBox.about(self, "Failed", "קובץ הגדרות לא קיים")
        except KeyError:
            QMessageBox.about(self, "Failed", "בעיה בקובץ הגדרות")


        # Extract data
        self.buttonBox.accepted.connect(self.extract_data)
        self.buttonBox.rejected.connect(dialog.reject)
        QMetaObject.connectSlotsByName(dialog)

        self.retranslateUi(dialog)

    def retranslateUi(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "טעינת עסקאות ללא מתנה"))
        self.label_4.setText(_translate("Dialog", "קובץ לא להפצה"))
        self.label_8.setText(_translate("Dialog", "קובץ עסקאות"))
        self.label_9.setText(_translate("Dialog", "תיקיית ייצוא"))


