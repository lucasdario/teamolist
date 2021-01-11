from flask import Blueprint, redirect, request, render_template
from backend.controllers.product import list_products, create_product


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
    form_data = request.form
    create_product(form_data)
    return redirect('/product')
