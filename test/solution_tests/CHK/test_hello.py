from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("ABCD") == 115
    def test_checkout4a(self):
        assert checkout_solution.checkout("AAAABCD") == 245

    def test_checkout2b(self):
        assert checkout_solution.checkout("ABBCD") == 130

    def test_checkout4b(self):
        assert checkout_solution.checkout("ABBBBCD") == 175

