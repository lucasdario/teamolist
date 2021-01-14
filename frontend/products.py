from flask import Blueprint, redirect, request, render_template
from backend.controllers.controller_product import list_products, create_product, remove_product, edit_product
from backend.models.product import Product

product = Blueprint(__name__, 'product')


@product.route('/product/form', methods=['GET'])
def product_form():
    return render_template('product/form_product.html', titulo='Product')


@product.route('/product/update')
def product_update():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    return render_template(
        'product/form_product.html', titulo='Edit Product', update=True, id=id, name=name,
        description=description, price=price)


@product.route('/product/update', methods=['POST'])
def product_update_save():
    id = request.form.get('id')
    name = request.form.get('nome')
    description = request.form.get('descricao')
    price = request.form.get('preco')
    edit_product(id, name, description, price)
    return redirect('/product')


@product.route('/product/delete')
def product_delete():
    id = request.args.get('id')
    remove_product(id)
    return redirect('/product')


@product.route('/product', methods=['GET'])
def product_list():
    products_list = list_products()
    return render_template('product/list_product.html', title='Products', data=products_list)


@product.route('/product', methods=['POST'])
def product_create():
    product = Product(request.form.get('nome'), request.form.get('descricao'), request.form.get('preco'))
    create_product(product)
    return redirect('/product')
