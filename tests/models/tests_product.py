from backend.models.product import Product

def run_test_model_product():
    name = 'Roupa'
    description = 'muito bonita'
    price = 25.00
    try:
        product = Product(name, description, price)
        assert product.name is name
        assert product.description is description
        assert product.price is price
        assert isinstance(product, Product)
        print('\033[42;1;30m' + 'all model.product tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from model.product FAILED' + '\033[0;0m')
        raise asserterror

