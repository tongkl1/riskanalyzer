from django.test import TestCase

from .CSMARDataFetcher import CSMARDataFetcher

class CSMARDataFetcherTest(TestCase):

    def test_update_list(self):
        """
        test whether CSMARDataFetcherTest can execute update_list() correctly
        """
        fetcher = CSMARDataFetcher()
        fetcher.update_list()