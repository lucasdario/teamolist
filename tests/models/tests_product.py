import sys
sys.path.append('.')

from backend.models.product import Product
from backend.models.base_model import BaseModel

name = 'Roupa'
description = 'muito bonita'
price = 25.00

def test_model_product():
    try:
        test_instances()
        test_atrtributes()
        test_empty_name()
        test_empty_price()
        test_name_lenght()
        test_description_lenght()
        print('\033[42;1;30m' + 'all model.product tests PASSED' + '\033[0;0m')
    except AssertionError as error:
        print('\033[41;1;37m' +
              'some test from model.product FAILED' + '\033[0;0m')
        raise error

def test_instances():
    prod = Product(name, description, price)
    assert isinstance(prod, BaseModel), 'Object is not a BaseModel!'
    assert isinstance(prod, Product), 'Object is not a Product!'
    return prod

def test_atrtributes():
    prod = test_instances()
    assert isinstance(prod.name, str), 'Product.name is not a string!'
    assert len(prod.name) <= 200, 'Product.name is greater than 200 chars'
    assert isinstance(prod.description, str), 'Product.description is not a string!'
    assert len(prod.description) <= 500, 'Product.description is greater than 200 chars'
    assert isinstance(prod.price, float), 'Product.price is not a float!'
    assert prod.price > 0.0, 'Product.price is not greater than 0.0!'

def test_name_lenght():
    try:
        prod = Product('*' * 201, description, price)
        raise NotImplementedError('Exception not raised!')
    except ValueError as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

def test_description_lenght():
    try:
        prod = Product(name, '*' * 501, price)
        raise NotImplementedError('Exception not raised!')
    except ValueError as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

def test_empty_name():
    try:
        prod = Product('', description, price)
        raise NotImplementedError('Exception not raised!')
    except Exception as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

def test_empty_price():
    try:
        prod = Product(name, description, 0.0)
        raise NotImplementedError('Exception not raised!')
    except Exception as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

def test_negative_price():
    try:
        prod = Product(name, description, -10.0)
        raise NotImplementedError('Exception not raised!')
    except Exception as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

test_model_product()