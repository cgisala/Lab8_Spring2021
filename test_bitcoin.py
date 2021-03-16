import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin_usd_calculator as bit_calculator

class TestBitcoinExchangeRates(TestCase):

    """ Testing bitcoin_usd_calculator """
    def test_bitcoin_usd_calculator(self):
        # Assert 1 bitcoin is worth 55965.567 and should result in 55965.57
        rate = 55965.567
        amount = 1.0
        self.assertEqual(55965.57, bit_calculator.bitcoin_usd_calculator(rate, amount))

    """ Mocking print_results() """
    @patch('builtins.print')
    def test_print_results(self, mock_print):
        bit_calculator.print_results(1, 55965.98)
        mock_print.assert_called_once_with('\n1 bitcoin is equals to $ 55965.98\n')

    """ Mocking user_input() """
    @patch('builtins.input', side_effect=['a','-1','0','1'])
    def test_user_input(self, mock_input):
        bitcoin_amount = bit_calculator.user_input()
        self.assertEqual(1, bitcoin_amount)


if __name__ == '__main__':
    unittest.main()