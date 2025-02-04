from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class TableWidget(QTableWidget):

    def __init__(self,parent=None):
        QTableWidget.__init__(self, parent)
        self.cellChanged.connect(self.onCellChanged)
        self.df = None
        self.saved = True

    def is_saved(self):
        return self.saved;

    def save(self):
        self.saved = True

    def get_df(self):
        return self.df

    def filter(self,status):
        if status != "הכל" and status != None:
            all_status_rows = self.df['סטטוס'] == status
            list_index_status = all_status_rows[all_status_rows].index.values
        else:
            list_index_status = self.df.index

        for index in self.df.index:
            if(index in list_index_status):
                self.showRow(index)
            else:
                self.hideRow(index)

    def check_exist(self,list_trans_id):

        exist_trans = []
        no_exist_trans = []

        for index in self.df.index:
            if self.df.iloc[index,1] in list_trans_id:
                exist_trans.append(self.df.iloc[index,1])
            else:
                no_exist_trans.append(self.df.iloc[index,1])
        no_exist_trans = set(list_trans_id) - set(exist_trans)
        exist_trans = set(exist_trans)
        return exist_trans,no_exist_trans

    def setModelTable(self,df):

        self.df = df.fillna("")
        nRows = len(self.df.index)
        nColumns = len(self.df.columns)
        self.setRowCount(nRows)
        self.setColumnCount(nColumns)
        for c,header_title in enumerate(df.columns.tolist()):
            self.setHorizontalHeaderItem(c,QTableWidgetItem(header_title))

        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = self.df.iloc[i, j]
                itemWidget = QTableWidgetItem(str(item))
                self.setItem(i, j, itemWidget)

        self.saved = True
        #self.setSortingEnabled(True)

    def update_cell(self, row, column,value):
        self.df.set_value(row, column,value)

    @pyqtSlot(int, int)
    def onCellChanged(self, row, column):
        self.saved = False
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text
