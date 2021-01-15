from flask import render_template, request, redirect, Blueprint
from backend.controllers.controller_seller import create_seller, list_sellers, edit_seller, remove_seller
from backend.models.seller import Seller

seller = Blueprint(__name__, 'seller')


@seller.route('/seller/form', methods=['GET'])
def seller_form():
    return render_template('seller/form_seller.html', titulo='Seller')


@seller.route('/seller', methods=['POST'])
def seller_create():
    seller = Seller(request.form.get('nome'), request.form.get('phone'), request.form.get('email'))
    create_seller(seller)
    return redirect('/seller')


@seller.route('/seller', methods=['GET'])
def seller_list_():
    sellers = list_sellers()
    return render_template('seller/list_seller.html', title='Sellers', data=sellers)


@seller.route('/seller/update')
def seller_update():
    id = request.args.get('id')
    name = request.args.get('name')
    phone = request.args.get('phone')
    email = request.args.get('email')

    return render_template('seller/form_seller.html', titulo='Edit Seller',
                           update=True, id=id, name=name, phone=phone, email=email)


@seller.route('/seller/update', methods=['POST'])
def seller_update_save():
    id = request.form.get('id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    edit_seller(id, name, phone, email)

    return redirect('/seller')


@seller.route('/seller/delete')
def seller_delete():
    id = request.args.get('id')
    remove_seller(id)

    return redirect('/seller')
