from datetime import datetime, timedelta
from django.utils.timezone import make_aware
import math
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
from urllib3.exceptions import InsecureRequestWarning
import warnings

from .DataFetcher import DataFetcher
from .models import SheetTracker
from api.csmarapi.CsmarService import CsmarService
from data.models import BalanceSheet, IncomeSheet, CashflowSheetDirect, CashflowSheetIndirect

class CSMARDataFetcher(DataFetcher):
    # 静默未来版本警告, 该警告来源于NumPy的bug
    warnings.simplefilter(action='ignore', category=FutureWarning)
    # 静默http不安全警告 (垃圾国泰安)
    warnings.filterwarnings('ignore', category=InsecureRequestWarning, module='urllib3')

    connection_count = 0
    csmar = None
    login = False
    queryLimit = 200000
    query_days_limit = 365 * 4
    username = 'YOUR_CSMAR_ACCOUNT'
    pwd = '123456'
    temp_data_path = 'temp'
    balance_sheet_fields = None
    balance_sheet_mapping = None
    income_sheet_fields = None
    income_sheet_mapping = None
    cashflow_sheet_fields = None
    cashflow_sheet_mapping = None
    cashflow_sheet_indirect_fields = None
    cashflow_sheet_indirect_mapping = None

    def __init__(self):
        super().__init__()
        if self.connection_count == 0:
            CSMARDataFetcher.csmar = CsmarService()
            CSMARDataFetcher.login = False
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'balance_sheet_fields.txt')) as f:
                CSMARDataFetcher.balance_sheet_fields = f.read().split(',')
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'balance_sheet_mapping.txt')) as f:
                CSMARDataFetcher.balance_sheet_mapping = {x[0] : x[1] for x in [y.strip().split(',') for y in f.readlines()]}
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'income_sheet_fields.txt')) as f:
                CSMARDataFetcher.income_sheet_fields = f.read().split(',')
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'income_sheet_mapping.txt')) as f:
                CSMARDataFetcher.income_sheet_mapping = {x[0] : x[1] for x in [y.strip().split(',') for y in f.readlines()]}
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'cashflow_sheet_fields.txt')) as f:
                CSMARDataFetcher.cashflow_sheet_fields = f.read().split(',')
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'cashflow_sheet_mapping.txt')) as f:
                CSMARDataFetcher.cashflow_sheet_mapping = {x[0] : x[1] for x in [y.strip().split(',') for y in f.readlines()]}
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'cashflow_sheet_indirect_fields.txt')) as f:
                CSMARDataFetcher.cashflow_sheet_indirect_fields = f.read().split(',')
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'cashflow_sheet_indirect_mapping.txt')) as f:
                CSMARDataFetcher.cashflow_sheet_indirect_mapping = {x[0] : x[1] for x in [y.strip().split(',') for y in f.readlines()]}
        CSMARDataFetcher.connection_count += 1
        self.end_date = datetime.now().strftime('%Y-%m-%d')
        self.start_date = '1980-01-01'
        self.bar = None
    
    def __del__(self):
        super().__del__()
        CSMARDataFetcher.connection_count -= 1
        if self.connection_count == 0:
            CSMARDataFetcher.csmar = None
            CSMARDataFetcher.login = False
            CSMARDataFetcher.balance_sheet_fields = None
            CSMARDataFetcher.balance_sheet_mapping = None
            CSMARDataFetcher.income_sheet_fields = None
            CSMARDataFetcher.income_sheet_mapping = None
            CSMARDataFetcher.cashflow_sheet_fields = None
            CSMARDataFetcher.cashflow_sheet_mapping = None
            CSMARDataFetcher.cashflow_sheet_indirect_fields = None
            CSMARDataFetcher.cashflow_sheet_indirect_mapping = None

    def download_data(self, table_name : str, field_list : str, condition : str = '') -> pd.DataFrame:
        if not self.login:
            self.csmar.login(self.username, self.pwd)
            CSMARDataFetcher.login = True
        return self.get_CSMAR_data(table_name, field_list, self.start_date, self.end_date, condition)
    
    def get_CSMAR_data(self, table_name : str, field_list : str, start_date : str, end_date : str, condition : str = '') -> pd.DataFrame:
        count = self.query_count(field_list, table_name, start_date, end_date, condition)

        # 临时存储文件夹(防止国泰安下到一半崩溃)
        if not os.path.exists(os.path.join('datafetcher', self.temp_data_path)):
            os.makedirs(os.path.join('datafetcher', self.temp_data_path))

        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, table_name + '.pickle')) and os.path.exists(
                os.path.join('datafetcher', self.temp_data_path, table_name + '_date.txt')):
            res = pd.read_pickle(os.path.join('datafetcher', self.temp_data_path, table_name + '.pickle'))
            with open(os.path.join('datafetcher', self.temp_data_path, table_name + '_date.txt')) as f:
                current_day = f.read()
        else:
            res = pd.DataFrame()
            current_day = start_date

        next = self.time_delta(current_day, self.query_days_limit)

        self.bar = tqdm(desc='Download Progress', total=count)
        self.bar.update(res.shape[0])
        while next < end_date:
            query_res = self.query(table_name, field_list, current_day, next, condition)
            res = pd.concat([res] + query_res)
            next = self.time_delta(next, self.query_days_limit + 1)
            current_day = self.time_delta(current_day, self.query_days_limit + 1)
            res.to_pickle(os.path.join('datafetcher', self.temp_data_path, table_name + '.pickle'))
            with open(os.path.join('datafetcher', self.temp_data_path, table_name + '_date.txt'), 'w') as f:
                f.write(current_day)

        if current_day <= end_date:
            query_res = self.query(table_name, field_list, current_day, end_date, condition)
            res = pd.concat([res] + query_res)

        self.bar.close()
        self.bar = None

        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, table_name + '.pickle')):
            os.remove(os.path.join('datafetcher', self.temp_data_path, table_name + '.pickle'))
        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, table_name + '_date.txt')):
            os.remove(os.path.join('datafetcher', self.temp_data_path, table_name + '_date.txt'))

        return res.reset_index(drop=True)
    
    def query(self, table_name : str, field_list : str, start_date : str, end_date : str, condition : str = '') -> list:
        count = self.csmar.queryCount(field_list, condition, table_name, start_date, end_date)
        res = []
        i_max = math.ceil(count / self.queryLimit)
        for i in range(i_max):
            query_res = self.csmar.query(field_list,
                                         condition + ' limit %d,%d' % (i * self.queryLimit, self.queryLimit),
                                         table_name,
                                         start_date,
                                         end_date)
            res.append(pd.DataFrame(query_res))
            if not self.bar is None:
                self.bar.update(len(query_res))
        return res

    def query_count(self, field_list : str, table_name : str, start_date : str, end_date : str, condition : str = '') -> int:
        current_day = start_date
        next = self.time_delta(current_day, self.query_days_limit)
        cnt = 0
        while next < end_date:
            query_res = self.csmar.queryCount(field_list, condition, table_name, current_day, next)
            cnt += query_res
            next = self.time_delta(next, self.query_days_limit + 1)
            current_day = self.time_delta(current_day, self.query_days_limit + 1)

        if current_day <= end_date:
            query_res = self.csmar.queryCount(field_list, condition, table_name, current_day, end_date)
            cnt += query_res

        return cnt

    def update_list(self):
        '''
        拉取股票列表加入不存在的项
        '''
        stock_list = self.download_data('TRD_Co', ['Stkcd', 'Markettype'])
        entry_list = []
        for _, row in stock_list.iterrows():
            code = row['Stkcd']
            market_type = row['Markettype']
            if market_type != 1 and market_type != 4 and market_type != 16 and market_type != 32:
                continue
            if not SheetTracker.objects.filter(pk=code).exists():
                entry = SheetTracker(code=code, last_update=None, last_accounting_period=None)
                entry_list.append(entry)
        if len(entry_list) > 0:
            SheetTracker.objects.bulk_create(entry_list)

    def fetch(self, code: str):
        '''
        拉取指定代码的股票的财务数据

        Parameters:
        - code : str, 证券代码
        '''

        print('Fetching Balance Sheets')

        balance_sheet = self.download_data('FS_Combas', self.balance_sheet_fields, 'Typrep="A" and Stkcd=' + code)
        balance_sheet = balance_sheet.loc[balance_sheet['Typrep'] == 'A']
        balance_sheet['Accper'] = pd.to_datetime(balance_sheet['Accper']).dt.date
        balance_sheet = balance_sheet.replace([None], 0).replace(np.nan, 0)
        balance_sheet['A002126000'] += balance_sheet['A002127000']

        entry_list = []
        for _, row in balance_sheet.iterrows():
            date = row['Accper']
            if not BalanceSheet.objects.filter(code=code, date=date).exists():
                mapping = dict()
                for k, v in self.balance_sheet_mapping.items():
                    mapping[k] = row[v]
                entry = BalanceSheet(**mapping)
                entry_list.append(entry)

        if len(entry_list) > 0:
            BalanceSheet.objects.bulk_create(entry_list)

        print('Fetching Income Sheets')

        income_sheet = self.download_data('FS_Comins', self.income_sheet_fields, 'Typrep="A" and Stkcd=' + code)
        income_sheet = income_sheet.loc[income_sheet['Typrep'] == 'A']
        income_sheet['Accper'] = pd.to_datetime(income_sheet['Accper']).dt.date
        income_sheet = income_sheet.replace([None], 0).replace(np.nan, 0)

        entry_list = []
        for _, row in income_sheet.iterrows():
            date = row['Accper']
            if not IncomeSheet.objects.filter(code=code, date=date).exists():
                mapping = dict()
                for k, v in self.income_sheet_mapping.items():
                    mapping[k] = row[v]
                entry = IncomeSheet(**mapping)
                entry_list.append(entry)

        if len(entry_list) > 0:
            IncomeSheet.objects.bulk_create(entry_list)

        print('Fetching Cashflow Statements')

        cashflow_sheet = self.download_data('FS_Comscfd', self.cashflow_sheet_fields, 'Typrep="A" and Stkcd=' + code)
        cashflow_sheet = cashflow_sheet.loc[cashflow_sheet['Typrep'] == 'A']
        cashflow_sheet['Accper'] = pd.to_datetime(cashflow_sheet['Accper']).dt.date
        cashflow_sheet = cashflow_sheet.replace([None], 0).replace(np.nan, 0)

        entry_list = []
        for _, row in cashflow_sheet.iterrows():
            date = row['Accper']
            if not CashflowSheetDirect.objects.filter(code=code, date=date).exists():
                mapping = dict()
                for k, v in self.cashflow_sheet_mapping.items():
                    mapping[k] = row[v]
                entry = CashflowSheetDirect(**mapping)
                entry_list.append(entry)

        if len(entry_list) > 0:
            CashflowSheetDirect.objects.bulk_create(entry_list)

        print('Fetching Indirect Cashflow Statements')

        cashflow_sheet_indirect = self.download_data('FS_Comscfi', self.cashflow_sheet_indirect_fields, 'Typrep="A" and Stkcd=' + code)
        cashflow_sheet_indirect = cashflow_sheet_indirect.loc[cashflow_sheet_indirect['Typrep'] == 'A']
        cashflow_sheet_indirect['Accper'] = pd.to_datetime(cashflow_sheet_indirect['Accper']).dt.date
        cashflow_sheet_indirect = cashflow_sheet_indirect.replace([None], 0).replace(np.nan, 0)

        entry_list = []
        for _, row in cashflow_sheet_indirect.iterrows():
            date = row['Accper']
            if not CashflowSheetIndirect.objects.filter(code=code, date=date).exists():
                mapping = dict()
                for k, v in self.cashflow_sheet_indirect_mapping.items():
                    mapping[k] = row[v]
                entry = CashflowSheetIndirect(**mapping)
                entry_list.append(entry)

        if len(entry_list) > 0:
            CashflowSheetIndirect.objects.bulk_create(entry_list)

        # 更新SheetTracker的信息
        try:
            to_update = SheetTracker.objects.get(pk=code)
            to_update.last_update = make_aware(datetime.now())
            to_update.last_accounting_period = balance_sheet['Accper'].iloc[-1]
            to_update.save()
        except:
            pass
    
    def fetch_all(self):
        '''
        拉取所有股票的财务数据

        由于国泰安的土豆服务器连接质量堪忧, 这个函数比对每只股票都运行一次fetch()快很多
        '''
        if not os.path.exists(os.path.join('datafetcher', self.temp_data_path)):
            os.makedirs(os.path.join('datafetcher', self.temp_data_path))

        print('Fetching Balance Sheets')

        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'balance_sheet.pickle')):
            balance_sheet = pd.read_pickle(os.path.join('datafetcher', self.temp_data_path, 'balance_sheet.pickle'))
        else:
            balance_sheet = self.download_data('FS_Combas', self.balance_sheet_fields, 'Typrep="A"')
            balance_sheet = balance_sheet.loc[balance_sheet['Typrep'] == 'A'] # 再次确保没有母公司报表混入
            balance_sheet['Accper'] = pd.to_datetime(balance_sheet['Accper']).dt.date
            balance_sheet = balance_sheet.replace([None], 0).replace(np.nan, 0)
            balance_sheet['A002126000'] += balance_sheet['A002127000'] # 处理国泰安的一项录入错误
            balance_sheet.to_pickle(os.path.join('datafetcher', self.temp_data_path, 'balance_sheet.pickle'))

        code_list = set([x[0] for x in SheetTracker.objects.all().values_list('code')])
        now = datetime.now()
        entry_list = []
        to_update = set()
        bar = tqdm(desc='Process Progress', total=balance_sheet.shape[0])
        code_date_list = set([(x[0], x[1]) for x in BalanceSheet.objects.all().values_list('code', 'date')])
        for _, row in balance_sheet.iterrows():
            code = row['Stkcd']
            date = row['Accper']
            bar.update(1)
            if code in code_list and (code, date) not in code_date_list:
                entry = BalanceSheet(**{k : row[v] for k, v in self.balance_sheet_mapping.items()})
                entry_list.append(entry)
                to_update.add(code)

        bar.close()
        print('Updating database')
        if len(entry_list) > 0:
            BalanceSheet.objects.bulk_create(entry_list, batch_size=10000)


        print('Fetching Income Sheets')

        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'income_sheet.pickle')):
            income_sheet = pd.read_pickle(os.path.join('datafetcher', self.temp_data_path, 'income_sheet.pickle'))
        else:
            income_sheet = self.download_data('FS_Comins', self.income_sheet_fields, 'Typrep="A"')
            income_sheet = income_sheet.loc[income_sheet['Typrep'] == 'A'] # 再次确保没有母公司报表混入
            income_sheet['Accper'] = pd.to_datetime(income_sheet['Accper']).dt.date
            income_sheet = income_sheet.replace([None], 0).replace(np.nan, 0)
            income_sheet.to_pickle(os.path.join('datafetcher', self.temp_data_path, 'income_sheet.pickle'))

        code_list = set([x[0] for x in SheetTracker.objects.all().values_list('code')])
        entry_list = []
        bar = tqdm(desc='Process Progress', total=income_sheet.shape[0])
        code_date_list = set([(x[0], x[1]) for x in IncomeSheet.objects.all().values_list('code', 'date')])
        for _, row in income_sheet.iterrows():
            code = row['Stkcd']
            date = row['Accper']
            bar.update(1)
            if code in code_list and (code, date) not in code_date_list:
                entry = IncomeSheet(**{k : row[v] for k, v in self.income_sheet_mapping.items()})
                entry_list.append(entry)
                to_update.add(code)

        bar.close()
        print('Updating database')
        if len(entry_list) > 0:
            IncomeSheet.objects.bulk_create(entry_list, batch_size=10000)

        print('Fetching Cashflow Statements')

        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet.pickle')):
            cashflow_sheet = pd.read_pickle(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet.pickle'))
        else:
            cashflow_sheet = self.download_data('FS_Comscfd', self.cashflow_sheet_fields, 'Typrep="A"')
            cashflow_sheet = cashflow_sheet.loc[cashflow_sheet['Typrep'] == 'A'] # 再次确保没有母公司报表混入
            cashflow_sheet['Accper'] = pd.to_datetime(cashflow_sheet['Accper']).dt.date
            cashflow_sheet = cashflow_sheet.replace([None], 0).replace(np.nan, 0)
            cashflow_sheet.to_pickle(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet.pickle'))

        code_list = set([x[0] for x in SheetTracker.objects.all().values_list('code')])
        entry_list = []
        bar = tqdm(desc='Process Progress', total=cashflow_sheet.shape[0])
        code_date_list = set([(x[0], x[1]) for x in CashflowSheetDirect.objects.all().values_list('code', 'date')])
        for _, row in cashflow_sheet.iterrows():
            code = row['Stkcd']
            date = row['Accper']
            bar.update(1)
            if code in code_list and (code, date) not in code_date_list:
                entry = CashflowSheetDirect(**{k : row[v] for k, v in self.cashflow_sheet_mapping.items()})
                entry_list.append(entry)
                to_update.add(code)

        bar.close()
        print('Updating database')
        if len(entry_list) > 0:
            CashflowSheetDirect.objects.bulk_create(entry_list, batch_size=10000)

        print('Fetching Indirect Cashflow Statements')

        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet_indirect.pickle')):
            cashflow_sheet_indirect = pd.read_pickle(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet_indirect.pickle'))
        else:
            cashflow_sheet_indirect = self.download_data('FS_Comscfi', self.cashflow_sheet_indirect_fields, 'Typrep="A"')
            cashflow_sheet_indirect = cashflow_sheet_indirect.loc[cashflow_sheet_indirect['Typrep'] == 'A'] # 再次确保没有母公司报表混入
            cashflow_sheet_indirect['Accper'] = pd.to_datetime(cashflow_sheet_indirect['Accper']).dt.date
            cashflow_sheet_indirect = cashflow_sheet_indirect.replace([None], 0).replace(np.nan, 0)
            cashflow_sheet_indirect.to_pickle(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet_indirect.pickle'))

        code_list = set([x[0] for x in SheetTracker.objects.all().values_list('code')])
        entry_list = []
        bar = tqdm(desc='Process Progress', total=cashflow_sheet_indirect.shape[0])
        code_date_list = set([(x[0], x[1]) for x in CashflowSheetIndirect.objects.all().values_list('code', 'date')])
        for _, row in cashflow_sheet_indirect.iterrows():
            code = row['Stkcd']
            date = row['Accper']
            bar.update(1)
            if code in code_list and (code, date) not in code_date_list:
                entry = CashflowSheetIndirect(**{k : row[v] for k, v in self.cashflow_sheet_indirect_mapping.items()})
                entry_list.append(entry)
                to_update.add(code)

        bar.close()
        print('Updating database')
        if len(entry_list) > 0:
            CashflowSheetIndirect.objects.bulk_create(entry_list, batch_size=10000)

        balance_sheet = balance_sheet.sort_values(by=['Stkcd', 'Accper']).groupby('Stkcd').last()['Accper']
        update_list = []
        if len(to_update) > 0:
            for item in to_update:
                try:
                    obj = SheetTracker.objects.get(pk=item)
                    obj.last_update = make_aware(now)
                    obj.last_accounting_period = balance_sheet.loc[item]
                    update_list.append(obj)
                except:
                    pass
        SheetTracker.objects.bulk_update(update_list, ['last_update', 'last_accounting_period'], batch_size=10000)

        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'balance_sheet.pickle')):
            os.remove(os.path.join('datafetcher', self.temp_data_path, 'balance_sheet.pickle'))
        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'income_sheet.pickle')):
            os.remove(os.path.join('datafetcher', self.temp_data_path, 'income_sheet.pickle'))
        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet.pickle')):
            os.remove(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet.pickle'))
        if os.path.exists(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet_indirect.pickle')):
            os.remove(os.path.join('datafetcher', self.temp_data_path, 'cashflow_sheet_indirect.pickle'))

    @staticmethod
    def time_delta(currentDate: str, days: int) -> str:
        return datetime.strftime(datetime.strptime(currentDate, '%Y-%m-%d') + timedelta(days=days), '%Y-%m-%d')