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

    def test_checkout4b2e(self):
        assert checkout_solution.checkout("BBBBEE") == 155

    def test_checkout_none(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_badandgood(self):
        assert checkout_solution.checkout("BCAa") == -1

    def test_checkout2e2b(self):
        assert checkout_solution.checkout("BBEE") == 110

    def test_checkout1e2b(self):
        assert checkout_solution.checkout("BBE") == 85

    def test_checkout5a(self):
        assert checkout_solution.checkout("AAAAABCD") == 265

    def test_checkout8a(self):
        assert checkout_solution.checkout("AAAAAAAABCD") == 395

    def test_checkout2f(self):
        assert checkout_solution.checkout("FF") == 20

    def test_checkout3f(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_checkout6f(self):
        assert checkout_solution.checkout("FFFFFF") == 40


