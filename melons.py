"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Serving as a base class and refactor."""
    def __init__(self, order_type, species, qty):
    """Initialize melon order attributes"""

        self.order_type = order_type
        self.species = species
        self.qty = qty

class DomesticMelonOrder(object):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class InternationalMelonOrder(object):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
