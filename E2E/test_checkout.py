from pageObject.currencyClass import Currency
from utilities.BaseClass import BaseClass


class TestCheckout(BaseClass):
    """
    This test case is to verify that when a currency is selected
    or changed to euro, it also reflects on the prices of the goods
    and also the checkout price changes to euro
    """
    def test_euro_currency(self):
        Currency.click_currency(self)
        Currency.select_euro(self)
        """ Below is Assertion made to validate that the currency sign on 
            the checkout button changes to the currency selected
        """
        assert "€" in Currency.checkout_currency(self)
        for cur in Currency.price_currency(self):
            print(cur.text.index("€"))
            assert "€" == cur.text[5]

    """
        This test case is to verify that when a currency is selected 
        or changed to pounds, it also reflects on the prices of the goods
        and the checkout currency changes to pounds
    """
    def test_pounds_currency(self):
        Currency.click_currency(self)
        Currency.select_pounds(self)
        """ Below is Assertion made to validate that the currency sign on 
        the checkout button changes to the currency selected
        """
        assert "£" in Currency.checkout_currency(self)
        # Iterate through the prices to assert that the currency sign changes
        for cur in Currency.price_currency(self):
            print(cur.text)
            print(cur.text.index("£"))
            assert "£" == cur.text[0]

    """
        This test case is to verify that when a currency is selected 
        or changed to dollars, it also reflects on the prices of the goods
        and also the checkout price changes to dollars
    """
    def test_dollar_currency(self):
        Currency.click_currency(self)
        Currency.select_dollars(self)
        """ Below is Assertion made to validate that the currency sign on 
            the checkout button changes to the currency selected
        """
        assert "$" in Currency.checkout_currency(self)
        for cur in Currency.price_currency(self):
            assert "$" == cur.text[0]


