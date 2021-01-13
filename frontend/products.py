from flask import Blueprint, redirect, request, render_template
from backend.controllers.product import list_products, create_product
from backend.models.product import Product

product = Blueprint(__name__, 'product')


@product.route('/product/form', methods=['GET'])
def product_form():
    return render_template('product/form_product.html', titulo='Product')


@product.route('/product', methods=['GET'])
def product_list():
    products_list = list_products()
    return render_template('product/list_product.html', title='Products', data=products_list)


@product.route('/product', methods=['POST'])
def product_create():
    product = Product(request.form.get('nome'), request.form.get('descricao'), request.form.get('preco'))
    create_product(product)
    return redirect('/product')
