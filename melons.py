"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Serving as a base class."""
    def __init__(self, order_type, species, qty, tax):
    """Initialize melon order attributes"""

        self.order_type = order_type
        self.species = species
        self.qty = qty
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
     """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__("domestic", species, qty, 0.08)
        """Initialize melon order attributes"""
        self.order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code
        self.shipped = False
        self.tax = 0.17

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
