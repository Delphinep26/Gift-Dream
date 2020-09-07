import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtGui import QIcon,QPixmap,QFont
from classes.ExtractDataClass import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore

from classes.TableWidgetClass import TableWidget
from classes.Ui_DialogSettingsClass import Ui_DialogSettings
from classes.GenerateDocsFilesClass import GenerateDocsFile
from PyQt5.QtWidgets import QDialog
import json
from os.path import dirname, abspath
import os

class MenuForm(QtWidgets.QMainWindow):

    cur_dir = dirname(dirname(abspath(__file__)))

    def setupUi(self, MainWindow):

        screen = QtWidgets.QDesktopWidget().screenGeometry(-1)

        #Set mainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 900)
        MainWindow.showMaximized()
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        #Set Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 50, screen.width()-100, screen.height()-1))
        self.frame.showMaximized()
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frameButton = QtWidgets.QFrame(self.centralwidget)
        self.frameButton.setGeometry(QtCore.QRect(40, 5, screen.width()-100, 45))
        self.frameButton.showMaximized()
        self.frameButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButton.setObjectName("frameButton")
        self.frameButton.setLayoutDirection(QtCore.Qt.RightToLeft)

        self.frameButton.setVisible(False)
        #Set tableView

        self.tableView = TableWidget(self.frame)

        self.tableView.setGeometry(QtCore.QRect(0, 0, self.frame.geometry().width(), 600))
        #self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.hide()
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.horizontalHeader().setAutoScroll(True)

        # Set Buttons
        # Refresh button
        self.pushButtonRefresh = QtWidgets.QPushButton(self.frameButton)
        self.pushButtonRefresh.setGeometry(QtCore.QRect(5, 10, 30, 30))
        icon1 = QIcon()
        # icon1.setThemeName("./icons/refresh.svg")
        icon1.addPixmap(QPixmap("./icons/refresh.svg"), QIcon.Normal, QIcon.Off)
        self.pushButtonRefresh.setIcon(icon1)
        self.pushButtonRefresh.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")

        # Generate buttons
        self.pushButtonGenerate = QtWidgets.QPushButton(self.frameButton)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(480, 10, 200, 30))
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("./icons/print.svg"), QIcon.Normal, QIcon.Off)
        self.pushButtonGenerate.setIcon(icon4)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.pushButtonGenerate.clicked.connect(self.__generate_docs)

        # Open Folder button
        self.pushButtonOpenFolder = QtWidgets.QPushButton(self.frameButton)
        self.pushButtonOpenFolder.setGeometry(QtCore.QRect(685, 10, 200, 30))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./icons/folder.svg"), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenFolder.setIcon(icon2)
        self.pushButtonOpenFolder.setObjectName("pushButtonOpenFolder")
        self.pushButtonOpenFolder.clicked.connect(self.__open_output_folder)

        # Open Main Folder button
        self.pushButtonOpenMainFolder = QtWidgets.QPushButton(self.frameButton)
        self.pushButtonOpenMainFolder.setGeometry(QtCore.QRect(900, 10, 50, 30))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./icons/folders.svg"), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenMainFolder.setIcon(icon2)
        self.pushButtonOpenMainFolder.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonOpenMainFolder.setObjectName("pushButtonOpenMainFolder")
        self.pushButtonOpenMainFolder.clicked.connect(self.__open_main_folder)

        # Save button
        self.pushButtonSave = QtWidgets.QPushButton(self.frameButton)
        self.pushButtonSave.setGeometry(QtCore.QRect(40, 10, 30, 30))
        self.pushButtonSave.setIconSize(QtCore.QSize(20, 20))
        icon1.addPixmap(QPixmap("./icons/save.svg"), QIcon.Normal, QIcon.Off)
        self.pushButtonSave.setIcon(icon1)
        self.pushButtonSave.setObjectName("pushButtonSave")
        # self.pushButtonOpenFolder.clicked.connect(self.__open_output_folder)
        self.pushButtonSave.clicked.connect(self.__save_gasps)

        # pushAddGasp button
        self.pushAddGasp = QtWidgets.QPushButton(self.frameButton)
        self.pushAddGasp.setGeometry(QtCore.QRect(280, 10, 30, 30))
        icon = QIcon()
        icon.addPixmap(QPixmap("./icons/add.svg"), QIcon.Normal, QIcon.Off)
        self.pushAddGasp.setIcon(icon)
        # self.pushAddGasp.setIconSize(QtCore.QSize(30, 30))
        self.pushAddGasp.setObjectName("pushAddGasp")
        self.pushAddGasp.clicked.connect(self.__AddGasp)

        # Add trans id input text
        self.trans_id_list = QtWidgets.QLineEdit(self.frameButton)
        self.trans_id_list.setGeometry(QtCore.QRect(80, 10, 200, 30))
        # icon = QIcon.fromTheme("refresh.svg")
        # self.pushButtonOpenFolder.setIcon(icon)
        self.trans_id_list.setObjectName("trans_id_list")
        self.trans_id_list.setStyleSheet("Background-color: rgb(255, 255, 255);")

        # pushExport button
        self.pushExport = QtWidgets.QPushButton(self.frameButton)
        self.pushExport.setGeometry(QtCore.QRect(410, 10, 30, 30))
        icon = QIcon()
        icon.addPixmap(QPixmap("./icons/excel.svg"), QIcon.Normal, QIcon.Off)
        self.pushExport.setIcon(icon)
        self.pushExport.setIconSize(QtCore.QSize(20, 20))
        self.pushExport.setObjectName("pushExport")
        self.pushExport.clicked.connect(self.__ExportGasp)

        # Add area filter input text
        self.area_name = QtWidgets.QLineEdit(self.frameButton)
        self.area_name.setGeometry(QtCore.QRect(350, 10, 60, 30))
        self.area_name.setObjectName("area_name")

        #Set menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))

        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuGasp = QtWidgets.QMenu(self.menuFile)
        self.menuGasp.setObjectName("menuGasp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.links_settings = QtWidgets.QAction(MainWindow)
        self.links_settings.setObjectName("links_settings")
        self.display_no_dist = QtWidgets.QAction(MainWindow)
        self.display_no_dist.setObjectName("display_no_dist")
        # Option5
        self.display_gasps_status_1 = QtWidgets.QAction(MainWindow)
        self.display_gasps_status_1.setObjectName("display_gasps_status_1")
        # Option6
        self.display_gasps_status_2 = QtWidgets.QAction(MainWindow)
        self.display_gasps_status_2.setObjectName("display_gasps_status_2")
        # Option7
        self.display_gasps_status_3 = QtWidgets.QAction(MainWindow)
        self.display_gasps_status_3.setObjectName("display_gasps_status_3")
        # Option8
        self.display_gasps_status_4 = QtWidgets.QAction(MainWindow)
        self.display_gasps_status_4.setObjectName("display_gasps_status_4")
        # Option9
        self.display_gasps_status_5 = QtWidgets.QAction(MainWindow)
        self.display_gasps_status_5.setObjectName("display_gasps_status_5")
        # Option6
        #self.Inventory_tracking = QtWidgets.QAction(MainWindow)
        #self.Inventory_tracking.setObjectName("Inventory_tracking")

        #self.menuSettings.addAction(self.companies_settings)
        self.menuSettings.addAction(self.links_settings)
        #self.menuSettings.addAction(self.columns_settings)
        self.menuFile.addAction(self.display_no_dist)
        self.menuGasp.addAction(self.display_gasps_status_1)
        self.menuGasp.addAction(self.display_gasps_status_2)
        self.menuGasp.addAction(self.display_gasps_status_3)
        self.menuGasp.addAction(self.display_gasps_status_4)
        self.menuGasp.addAction(self.display_gasps_status_5)

        self.menuGasp.addSeparator()
        self.menuFile.addAction(self.menuGasp.menuAction())

        #self.menuFile.addAction(self.Inventory_tracking)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        #Set triggers buttons
        self.links_settings.triggered.connect(self.__open_settings)
        # self.companies_settings.triggered.connect(self.__companies_settings)
        self.display_no_dist.triggered.connect(self.__open_no_dist)
        self.display_gasps_status_1.triggered.connect(lambda  x :self.__open_gasp("פתוח"))
        self.display_gasps_status_2.triggered.connect(lambda  x :self.__open_gasp("נמסר ללקוח"))
        self.display_gasps_status_3.triggered.connect(lambda x: self.__open_gasp("לא רוצה מתנה"))
        self.display_gasps_status_4.triggered.connect(lambda x: self.__open_gasp("נמסר לנהג"))
        self.display_gasps_status_5.triggered.connect(lambda x: self.__open_gasp("הכל"))
        #self.Inventory_tracking.triggered.connect(self.__open_invent)

        self.homeTitle = QtWidgets.QLabel(self.centralwidget)
        self.homeTitle.setGeometry(QtCore.QRect(screen.width() / 2 -295, screen.height() / 2-75, 500, 100))

        self.homeTitle.setObjectName("homeTitle")

        self.tableTitle = QtWidgets.QLabel(self.centralwidget)
        self.tableTitle.setGeometry(QtCore.QRect(screen.width() - 380, 0, 300, 50))

        self.tableTitle.setObjectName("TableTitle")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(250, 0, 800, 600))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.hide()
        self.__set_stylesheet(MainWindow)
        self.__retranslateUi(MainWindow)

        #Set settings
        try:
            self.__extract_setting()
        except FileNotFoundError:
            QMessageBox.about(self.centralwidget, "Failed", "קובץ הגדרות לא קיים")
            self.menubar.setDisabled(True)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def __set_stylesheet(self,MainWindow):
        fname = './/img//backgroung_image.jpg'

        MainWindow.setStyleSheet("#MainWindow {" +
                                 "background-image: url(" + fname + "); "
                                                                    "background-repeat: repeat; " \
                                                                    "background-position: center;" \
                                                                    "font-size: 50px;" \
                                                                    "}")
        self.frameButton.setStyleSheet("background-color: rgba(208, 202, 202,0.80);")
        # Set css Table view
        stylesheet = "::section{Background-color:rgb(190,1,1);" \
                     "color:rgb(255,255,255);" \
                     "font-weight:700;" \
                     "font-size: 15px;" \
                     "border-radius:5px;}"
        self.tableView.horizontalHeader().setStyleSheet(stylesheet)

        stylesheet = "font-size: 15px;" \
                     "border-radius:5px;"
        self.tableView.setStyleSheet(stylesheet)
        self.area_name.setStyleSheet("Background-color: rgb(255, 255, 255);")

        # # Set css Buttons
        # # stylesheet = ");"
        stylesheet = "#pushButtonOpenMainFolder,#pushButtonOpenFolder,#pushButtonGenerate,#pushAddGasp,#trans_id_list,#pushButtonSave{" \
                     "font-weight:700;" \
                     "color:rgb(255,255,255);" \
                     "Background-color:rgba(22,145,178,0.8);" \
                     "font-size: 15px;}" \
                     "pushButtonOpenMainFolder,#pushButtonOpenFolder:hover,#pushButtonGenerate:hover" \
                     "{Background-color:rgb(255,255,255);" \
                     "color:rgb(22,145,178);}"

        self.pushButtonOpenFolder.setStyleSheet(stylesheet)
        self.pushButtonOpenMainFolder.setStyleSheet(stylesheet)
        self.pushButtonGenerate.setStyleSheet(stylesheet)
        self.menubar.setStyleSheet("#menubar {""font-size: 15px;}")
        self.homeTitle.setStyleSheet("color: rgb(214, 52, 24);"
                                     "font: 35pt; text-align: center")
        self.tableTitle.setStyleSheet("color: rgb(214, 52, 24);")

        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tableTitle.setFont(font)

    def __retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gift Dream"))
        self.pushButtonGenerate.setText(_translate("MainWindow", "הדפסת מכתבים"))
        self.pushButtonOpenFolder.setText(_translate("MainWindow", "מסמכים"))
        self.pushButtonOpenMainFolder.setText(_translate("MainWindow", ""))
        self.menuFile.setTitle(_translate("MainWindow", "קובץ"))
        self.menuGasp.setTitle(_translate("MainWindow", "פערים"))
        self.menuSettings.setTitle(_translate("MainWindow", "הגדרות"))
        self.menuAbout.setTitle(_translate("MainWindow", "אודות"))
        self.links_settings.setText(_translate("MainWindow", "קבצים"))
        self.display_no_dist.setText(_translate("MainWindow", "עסקאות לא להפצה"))
        self.display_gasps_status_1.setText(_translate("MainWindow", "פתוחים"))
        self.display_gasps_status_2.setText(_translate("MainWindow", "נמסרו ללקוח"))
        self.display_gasps_status_3.setText(_translate("MainWindow", "לא רצו מתנות"))
        self.display_gasps_status_4.setText(_translate("MainWindow", "נמסרו לנהג"))
        self.display_gasps_status_5.setText(_translate("MainWindow", "הכל"))

        #self.Inventory_tracking.setText(_translate("MainWindow", "מעקב מלאי"))
        self.homeTitle.setText(_translate("MainWindow", "ברוכים הבאים\n Gift Dream"))
        self.__show_hide_components("")

    def __show_hide_components(self, name):

        self.__hide_components(name)
        self.__show_components(name)


    def __show_components(self, name):

        try:
            self.pushButtonRefresh.disconnect()
        except Exception:
            pass

        if name == "פערים":

            self.tableTitle.setText("טבלת פערים")
            self.frameButton.setVisible(True)
            self.pushButtonRefresh.clicked.connect(self.__extract_gasps)
            self.pushButtonRefresh.show()
            self.pushButtonGenerate.show()
            self.pushButtonOpenFolder.show()
            self.pushButtonSave.show()
            self.tableView.show()

            if self.status == "פתוח":
                self.pushAddGasp.show()
                self.pushExport.show()
                self.area_name.show()
                self.trans_id_list.show()

        if name == "הפצה":

            self.tableTitle.setText("טבלת עסקאות לא להפצה")
            self.frameButton.setVisible(True)
            self.pushButtonRefresh.clicked.connect(self.__extract_no_dist)
            self.pushButtonRefresh.show()
            self.tableView.show()
            self.frame.show()

        if name == "מלאי":
            self.frameButton.show()
            self.tableTitle.setText("מעקב מלאי")
            self.calendarWidget.show()

    def __hide_components(self, name):
        self.homeTitle.hide()
        if name == "פערים":
            if self.status != "פתוח":
                self.pushAddGasp.hide()
                self.pushExport.hide()
                self.area_name.hide()
                self.trans_id_list.hide()

        if name != "פערים":
            self.pushAddGasp.hide()
            self.trans_id_list.hide()
            self.pushButtonRefresh.hide()
            self.pushButtonOpenFolder.hide()
            self.pushButtonGenerate.hide()
            self.pushExport.hide()
            self.area_name.hide()
            self.pushButtonSave.hide()

        if name != "מלאי":
            self.calendarWidget.hide()

    def __extract_setting(self):
        cur_dir = dirname(dirname(abspath(__file__)))

        self.settings_file = cur_dir +'//Settings//settings.txt'
        with open(self.settings_file) as json_file:
            settings = json.load(json_file)

        self.transaction_file_name = settings['קובץ עסקאות']
        self.transaction_file_name_v2 = settings['קובץ עסקאות 200']
        self.gifts_codes_file_name = self.cur_dir +'//Settings//gifts_codes.CSV'
        self.distribution_file_name = settings['קובץ לא להפצה']
        self.main_folder_name = settings['תיקייה ראשית']
        self.transation_cols = ['עסקה', 'מספר חברה', 'שם חברה']
        # self.gasp_file_name = settings['קובץ פערים']
        self.gasp_file_name =  self.main_folder_name +"//"+ "פערים מרוכז" + ".csv"
        # print(self.gasp_file_name)
        self.status = None
        # self.gasp_sheet_name = settings['שם גיליון קובץ פערים']

    def __open_output_folder(self):
        path = os.path.realpath(self.cur_dir + '//docs')
        os.startfile(path)

    def __open_main_folder(self):

        path = os.path.realpath(self.main_folder_name)
        os.startfile(path)

    def __update_TableView(self, df):

        self.tableView.setModelTable(df)
        self.tableView.filter(self.status)

    def __ExportGasp(self):

        if self.area_name != "":
            try:
                extract = ExtractData(output_folder = self.cur_dir + '//docs')
                if (extract.export_excel(self.gasps,self.area_name.text(),"פתוח")):
                    #self.__open_output_folder()
                    pass
                else:
                    QMessageBox.about(self.centralwidget, "אזהרה",
                                      "לא נמצאו עסקאות מאזור {0}".format(self.area_name.text()))
            except PermissionError:
                 QMessageBox.about(self, "Failed", "קובץ פתוח")
            except Exception:
                QMessageBox.about(self.centralwidget, "שגיאה",
                              "תיקייה לא נמצאה או שגיאה בכתיבת הקובץ".format(self.area_name.text()))

    def __AddGasp(self):
        buttonReply = QMessageBox.question(self.tableView, 'הוספת פערים', "האם אתה בטוח?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            try:
                extract = ExtractData(gasp_file_name = self.gasp_file_name,
                                      transaction_file_name=self.transaction_file_name,
                                      transaction_file_name_v2 = self.transaction_file_name_v2,
                                      gifts_codes_file_name= self.gifts_codes_file_name)

                trans_id_list_input = self.trans_id_list.text().replace(" ","").replace("\n","").split(",")
                exist_trans, no_exist_trans = self.tableView.check_exist(trans_id_list_input)
                if len(exist_trans) > 0:
                    QMessageBox.about(self.centralwidget, "אזהרה","העסקאות {0} כבר קיימות בקובץ פערים".format(" ".join(list(exist_trans))))
                if len(no_exist_trans) > 0:
                    no_found = extract.add_gasps(no_exist_trans)
                    #self.__open_gasp(self.status)
                    self.__extract_gasps()
                    # print(type(no_found),no_found)
                    if len(no_found) > 0:
                        QMessageBox.about(self.centralwidget, "הודעה",
                                          "העסקאות {0} לא נמצאו".format(" ".join(list(no_found))))
                    self.__update_TableView(self.gasps)
                    no_exist_trans = no_exist_trans - set(map(str,no_found))
                    # print(type(no_exist_trans),no_exist_trans)
                    if no_exist_trans:
                        QMessageBox.about(self.centralwidget, "הודעה",
                                      "העסקאות {0} הוטענו בהצלחה!".format(" ".join(list(no_exist_trans))))

            except FileNotFoundError:
                QMessageBox.about(self, "Failed", "אחד מהקבצים לא נמצא (פערים,קוד מתנה או csv)")
            except KeyError as key_err:
                QMessageBox.about(self, "Failed", "עמודות חסרות בקובץ פערים")

            except PermissionError:
                 QMessageBox.about(self, "Failed", "קובץ פערים פתוח")
            except Exception:
                 QMessageBox.about(self, "Failed", "תקלה בשליפת/כתיבת הנתונים")

    def __generate_docs(self):
        list_index = []
        for index in self.tableView.selectionModel().selectedRows():
            if not self.tableView.isRowHidden(index.row()):
                list_index.append(index.row())

        if len(list_index) == 0:
            QMessageBox.information(self.tableView, ' הדפסת טפסי לקוח', "לא נבחרו עסקאות")
            return
        buttonReply = QMessageBox.question(self.tableView, ' הדפסת טפסי לקוח', "האם אתה בטוח?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            # print(list_index)
            generate = GenerateDocsFile(self.centralwidget,self.gasps.iloc[list_index])
            result = generate.generate_files(self.cur_dir +'//templates_files//template.docx',self.cur_dir+'//docs')
            if result:
                path = os.path.realpath(self.cur_dir+'//docs')
                os.startfile(path)

    def __open_gasp(self,status=None):

        self.status = status
        if self.__extract_gasps():
            self.__show_hide_components("פערים")

    def __open_no_dist(self):

        if self.__extract_no_dist():
            self.__show_hide_components("הפצה")

    def __open_invent(self):
        self.__show_hide_components("מלאי")

    def __open_settings(self):

        Dialog = QDialog()
        Dialog.ui = Ui_DialogSettings(Dialog,self.transaction_file_name,self.transaction_file_name_v2,self.main_folder_name, self.distribution_file_name,self.settings_file)
        Dialog.ui.setupUi(Dialog)
        Dialog.exec_()

    def __extract_gasps(self):
        try:
            extract = ExtractData(gasp_file_name = self.gasp_file_name)

            self.gasps = extract.read_gasps(self.status)
            self.__update_TableView(self.gasps)
            return True

        except FileNotFoundError:
            QMessageBox.about(self, "Failed", "קובץ פערים לא נמצא")
            return False
        except ValueError:
             QMessageBox.about(self, "Failed", "אין נתונים באחד מהקבצים או יתכן והזנת נתונים שגויים")
        except KeyError as key_err:
             QMessageBox.about(self, "Failed", "עמודות חסרות בקובץ פערים")
        except PermissionError:
             QMessageBox.about(self, "Failed", "קובץ פתוח")
        except Exception:
             QMessageBox.about(self, "Failed", "תקלה בשליפת הנתונים")

    def __save_gasps(self):
        try:
            self.gasps = self.tableView.get_df()
            ExtractData.save(self.gasp_file_name,self.gasps)
            self.tableView.save()
            self.__extract_gasps()
            self.__update_TableView(self.gasps)

        except FileNotFoundError:
            QMessageBox.about(self, "Failed", "קובץ פערים לא נמצא")
        except ValueError:
            QMessageBox.about(self, "Failed", "אין נתונים באחד מהקבצים או יתכן והזנת נתונים שגויים")
        except KeyError as key_err:
            QMessageBox.about(self, "Failed", "עמודות חסרות בקובץ פערים")
        except PermissionError:
            QMessageBox.about(self, "Failed", "קובץ פתוח")
        except Exception:
            QMessageBox.about(self, "Failed", "תקלה בשליפת הנתונים")

    def __extract_no_dist(self):

        self.status = None

        extract = ExtractData(transaction_file_name=self.transaction_file_name,
                              transaction_file_name_v2=self.transaction_file_name_v2,
                                      distribution_file_name=self.distribution_file_name,
                                      output_folder="",
                                      transation_cols=self.transation_cols)

        try:
            extract.extract_all()
            self.no_dists = extract.get_update_no_distribution()
            self.__update_TableView(self.no_dists)
            return True

        except FileNotFoundError:
            QMessageBox.about(self, "Failed", "קובץ הפצה / עסקאות לא נמצא")
            return False
        except PermissionError:
            QMessageBox.about(self, "Failed", "קובץ פתוח")
            return None
        except ValueError:
             QMessageBox.about(self, "Failed", "אין נתונים באחד מהקבצים או יתכן והזנת נתונים שגויים")
        except KeyError as key_err:
             QMessageBox.about(self, "Failed","עמודות חסרות בקובץ הפצה / עסקאות")
        except Exception:
              QMessageBox.about(self, "Failed", "תקלה בשלפית הנתונים")
