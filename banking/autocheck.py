import unittest
import pexpect

class BankingAutocheck(unittest.TestCase):
    timeout = 3
    def test_age_less_than_12(self):
        bank = pexpect.spawn('ruby run.rb')
        bank.expect(['Banking v0.3', 'Customer age (integer):'], self.timeout)
        bank.sendline('12')
        bank.expect('Customer service: false', self.timeout)
        bank.expect('Offer membership: false', self.timeout)
        bank.expect('Discount rate: false', self.timeout)
        bank.interact()

if __name__ == '__main__':
    unittest.main()

