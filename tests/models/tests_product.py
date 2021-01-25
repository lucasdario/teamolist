from backend.models.product import Product

class TestProduct:

    name = 'Roupa'
    description = 'muito bonita'
    price = 25.00

    def test(self):
        product = Product(self.name, self.description, self.price)
        assert product.name is self.name
        assert product.description is self.description
        assert product.price is self.price
        assert isinstance(product, Product)
