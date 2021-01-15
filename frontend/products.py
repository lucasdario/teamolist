from flask import Blueprint, redirect, request, render_template
from backend.controllers.controller_product import ProductController
from backend.models.product import Product


product = Blueprint(__name__, 'product')
_PRODUCT_CONTROLLER = ProductController()


@product.route('/product/form', methods=['GET'])
def product_form():
    return render_template('product/form_product.html', titulo='Product')


@product.route('/product/update')
def product_update():
    id = request.args.get('id')
    product = _PRODUCT_CONTROLLER.read_by_id(id)
    return render_template(
        'product/form_product.html', titulo='Edit Product', update=True, id=product.id, name=product.name,
        description=product.description, price=product.price)


@product.route('/product/update', methods=['POST'])
def product_update_save():
    id = request.form.get('id')
    name = request.form.get('nome')
    description = request.form.get('descricao')
    price = request.form.get('preco')
    product = Product(name, description, price, id)
    _PRODUCT_CONTROLLER.update(product)
    return redirect('/product')


@product.route('/product/delete')
def product_delete():
    id = request.args.get('id')
    _PRODUCT_CONTROLLER.delete(id)
    return redirect('/product')


@product.route('/product', methods=['GET'])
def product_list():
    products = _PRODUCT_CONTROLLER.read_all()
    return render_template('product/list_product.html', title='Products', data=products)


@product.route('/product', methods=['POST'])
def product_create():
    product = Product(request.form.get('nome'), request.form.get('descricao'), request.form.get('preco'))
    _PRODUCT_CONTROLLER.create(product)
    return redirect('/product')
