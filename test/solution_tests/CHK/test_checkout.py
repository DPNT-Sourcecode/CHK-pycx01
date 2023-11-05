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

    def test_checkout15H(self):
        assert checkout_solution.checkout("H"*15) == 125

    def test_checkout2K(self):
        assert checkout_solution.checkout("KK") == 120

    def test_checkout3NM(self):
        assert checkout_solution.checkout("NNNM") == 120

    def test_checkout5P(self):
        assert checkout_solution.checkout("PPPPP") == 200

    def test_checkout3Q(self):
        assert checkout_solution.checkout("QQQ") == 80

    def test_checkout4Q3R(self):
        assert checkout_solution.checkout("RRRQQQQ") == 230

    def test_checkout4U(self):
        assert checkout_solution.checkout("UUUU") == 120

    def test_checkout5V(self):
        assert checkout_solution.checkout("VVVVV") == 220


    def test_checkout_bundleS(self):
        assert checkout_solution.checkout("SSS") == 45

    def test_checkout_bundleST(self):
        assert checkout_solution.checkout("SSSTTT") == 90

    def test_checkout_bundleSTX(self):
        assert checkout_solution.checkout("SSSTTTXXX") == 135

    def test_checkout_bundleSTXY(self):
        assert checkout_solution.checkout("SSSTTTXXXYYY") == 180

    def test_checkout_bundleSTXYZ(self):
        assert checkout_solution.checkout("STXYZSTXYZSTXYZ") == 225


