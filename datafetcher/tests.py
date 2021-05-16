from django.test import TestCase

from .CSMARDataFetcher import CSMARDataFetcher

class CSMARDataFetcherTest(TestCase):

    def test_update_list(self):
        """
        Test whether CSMARDataFetcherTest can execute update_list() correctly.
        """
        fetcher = CSMARDataFetcher()
        fetcher.update_list()
    
    def test_fetch(self):
        """
        Test whether CSMARDataFetcherTest can execute fetch() correctly.
        
        This test only checks whether the function can run without throwing an error.
        To check the validity of the data, you need to check the sheets manually after run this test.
        """
        code = "000001"
        fetcher = CSMARDataFetcher()
        fetcher.fetch(code)

    def test_fetch_all(self):
        """
        **DO NOT run this test easily, as fetch_all() is a very time-consuming task.**
        
        Test whether CSMARDataFetcherTest can execute fetch_all() correctly.

        This test only checks whether the function can run without throwing an error.
        To check the validity of the data, you need to check the sheets manually after run this test.
        """
        fetcher = CSMARDataFetcher()
        fetcher.fetch_all()