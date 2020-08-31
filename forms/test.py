# import sys
# import pandas as pd
# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QApplication, QWidget
# from pandas import np
#
# from classes.TableWidgetClass import TableWidget
#
#
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(700, 100, 350, 380)
#         df_rows = 10
#         df_cols = 3
#         df = pd.DataFrame(np.random.randn(df_rows, df_cols))
#         self.tableWidget = TableWidget(df, self)
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.tableWidget)
#         self.button = QPushButton('Print DataFrame', self)
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)
#         self.button.clicked.connect(self.print_my_df)
#
#     @pyqtSlot()
#     def print_my_df(self):
#         print(self.tableWidget.df)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     ex.show()
#     sys.exit(app.exec_())