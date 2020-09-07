from pandas import read_csv, merge,to_datetime
from datetime import date,timedelta
from os import path,startfile
import numpy as np


class ExtractData:

    def __init__(self, **kwargs):

        valid_keys = ["transaction_file_name", "transaction_file_name_v2","distribution_file_name", "output_folder", "transation_cols",
                      "gasp_file_name", "gasp_sheet_name","gifts_codes_file_name"]

        for key in valid_keys:
            setattr(self, key, kwargs.get(key))

    def export_excel(self, df, area_name, status):

        if area_name != "":
            df_to_export = df[(df['אזור'] == area_name) &  (df['סטטוס'] == status)].iloc[:, 1:-3]
            if len(df_to_export) > 0:
                df_to_export['חתימה + חותמת'] = " "
                today = date.today().strftime("%d_%m_%Y")
                filename = self.output_folder + "//" + "פערים_" + area_name +'_' +today +".xls"
                df_to_export.to_excel(filename, index=False)
                path_docs = path.realpath(filename)
                startfile(path_docs)
                return True
        return False

    def read_gasps(self,status):

        gasps = read_csv(self.gasp_file_name, encoding="ISO-8859-8")
        gasps = gasps.astype({"עסקה": str})
        gasps['הפצה'] = to_datetime(gasps['הפצה'], format="%d/%m/%Y")
        gasps = gasps.sort_values(by=['הפצה','אזור','עיר'])
        #gasps = gasps.astype({"הפצה": str})
        # print(gasps['הפצה'].dtype)
        gasps['הפצה'] = gasps['הפצה'].apply(lambda x: x.strftime("%d/%m/%Y"))
        gasps = gasps.reset_index(drop=True)
        # if status and status != "הכל":
        #     gasps = gasps[gasps['סטטוס'] == status]
        return gasps

    def __read_transaction(self):

        self.transactions = read_csv(self.transaction_file_name, encoding="ISO-8859-8")
        self.transactions.columns = self.transactions.columns.str.lstrip()
        self.transactions.columns = self.transactions.columns.str.rstrip()

    def __read_gifts_codes(self):

        self.gifts_codes = read_csv(self.gifts_codes_file_name, encoding="ISO-8859-8")
        self.gifts_codes.columns = self.gifts_codes.columns.str.lstrip()
        self.gifts_codes.columns = self.gifts_codes.columns.str.rstrip()

    def __read_transaction_version2(self):

        self.transactions_v2 = read_csv(self.transaction_file_name_v2, encoding="ISO-8859-8")
        self.transactions_v2.columns = self.transactions_v2.columns.str.lstrip()
        self.transactions_v2.columns = self.transactions_v2.columns.str.rstrip()

    def __read_new_gasps(self, trans_id_list):
        self.__read_transaction()
        self.__read_transaction_version2()
        self.__read_gifts_codes()

        added_gasps = merge(self.transactions[self.transactions['עסקה'].isin(trans_id_list)],
                           self.transactions_v2,
                           how='inner',
                           on=['עסקה'])

        added_gasps = merge(added_gasps,
                            self.gifts_codes,
                            how='left',
                            left_on='1 שי',
                            right_on='קוד מתנה')

        # today= date.today()
        date_dist = date.today()  + timedelta(days=1)
        date_dist = date_dist.strftime("%d/%m/%Y")
        added_gasps['כמות'] = 1
        added_gasps['הערות'] = " "
        added_gasps['חתימה'] = " "
        added_gasps['נייד'] = added_gasps['נייד'].astype(str)
        added_gasps['טלפון'] = added_gasps['טלפון'].astype(str)
        added_gasps['נייד'] = np.where((added_gasps['נייד'] == "0") | (~ added_gasps['נייד'].str.startswith('5')),
                                       added_gasps['טלפון'], added_gasps['נייד'])
        added_gasps['עסקה'] = added_gasps['עסקה'].astype(str)
        added_gasps['סטטוס'] = "פתוח"
        added_gasps['חברה'] = added_gasps['חברה'].str.strip()
        added_gasps['שם  איזור'] = added_gasps['שם  איזור'].str.strip()
        added_gasps['שם  איזור'] = added_gasps['שם  איזור'].str.replace(' +', ' ')
        added_gasps['כתובת'] = added_gasps['כתובת למסירה'].str.replace(' +', ' ')
        added_gasps['שם עיר'] = added_gasps['שם עיר'].str.replace(' +', ' ')
        added_gasps['הפצה'] = date_dist
        added_gasps['מקבל תווים'] = added_gasps['מקבל תווים'].str.replace(' +', ' ')
        added_gasps['מקבל'] = added_gasps['מקבל תווים'] + " - 0" + added_gasps['נייד']
        added_gasps = added_gasps.rename(columns={'שם  איזור': 'אזור', 'שם מתנה': 'שי', 'טלפון': 'טלפון במשרד'})

        added_gasps = added_gasps[['הפצה','עסקה','אזור','שם עיר','כתובת' , 'חברה','מקבל','שי','כמות','הערות' ,'חתימה','סטטוס']]

        #added_gasps = added_gasps[['הפצה','עסקה', 'חברה', 'אזור', 'כמות','אזור','שם עיר','כתובת', 'מקבל','הערות' ,'חתימה','סטטוס']]
        added_gasps = added_gasps.fillna("")
        # print(set(added_gasps['עסקה']))
        no_found = set(trans_id_list) - set(added_gasps['עסקה'])
        return added_gasps , no_found

    def __find_no_distribution(self):

        if len(self.transactions) == 0:
            raise ValueError

        gift_trans = self.transactions[(self.transactions['1 שי'] != 25) & (self.transactions['1 שי'] != 0)]


        try:
            no_distribution = read_csv(self.distribution_file_name, encoding='utf-8')
        except:
            try:
                no_distribution = read_csv(self.distribution_file_name, encoding="ISO-8859-8")
            except:
                raise Exception

        self.update_no_distribution = merge(gift_trans, no_distribution, how='inner', on=['מספר חברה'])
        self.update_no_distribution = self.update_no_distribution[self.transation_cols]
        self.update_no_distribution.sort_values(by=self.transation_cols,ascending=False)

    def load_data(self):
        self.update_no_distribution.to_excel(self.output_folder + "/output.xlsx", index=False)

    def save(filename, df):
        to_datetime(df['הפצה'])
        df['כמות'].astype(int)
        df.to_csv(filename, index=False, encoding="ISO-8859-8")

    def get_update_no_distribution(self):
        #self.__find_no_distribution()
        return self.update_no_distribution;

    def add_gasps(self, trans_id_list):
        added_gasps , no_found = self.__read_new_gasps(trans_id_list)
        added_gasps.to_csv(self.gasp_file_name,mode='a',header=False,index=False, encoding="ISO-8859-8")
        return no_found

    def extract_all(self):

        self.__read_transaction()
        self.__find_no_distribution()

