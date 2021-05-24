from abc import ABCMeta, abstractmethod

class DataFetcher(metaclass=ABCMeta):
    def __init__(self):
        pass

    def __del__(self):
        pass

    @abstractmethod
    def update_list(self):
        '''
        拉取股票列表加入不存在的项
        '''
        pass

    @abstractmethod
    def fetch(self, code : str):
        '''
        拉取指定代码的股票的财务数据
        Parameters:
        - code : str, 证券代码
        '''
        pass

    @abstractmethod
    def fetch_all(self):
        '''
        拉取所有股票的财务数据
        '''
        pass
