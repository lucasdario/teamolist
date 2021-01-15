from flask import render_template, request, redirect, Blueprint
from backend.controllers.controller_seller import SellerController
from backend.models.seller import Seller

seller = Blueprint(__name__, 'seller')


@seller.route('/seller/form', methods=['GET'])
def seller_form():
    return render_template('seller/form_seller.html', titulo='Seller')


@seller.route('/seller', methods=['POST'])
def seller_create():
    seller = Seller(request.form.get('name'), request.form.get('phone'), request.form.get('email'))
    SellerController().create(seller)
    return redirect('/seller')


@seller.route('/seller', methods=['GET'])
def seller_list_():
    sellers = SellerController().read_all()
    return render_template('seller/list_seller.html', title='Sellers', data=sellers)


@seller.route('/seller/update')
def seller_update():
    id = request.args.get('id')
    seller = SellerController().read_by_id(id)

    return render_template('seller/form_seller.html', titulo='Edit Seller',
                           update=True, id=id, name=seller.name, phone=seller.phone, email=seller.email)


@seller.route('/seller/update', methods=['POST'])
def seller_update_save():
    id = request.form.get('id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    seller = Seller(name, phone, email, id)
    SellerController().update(seller)

    return redirect('/seller')


@seller.route('/seller/delete')
def seller_delete():
    id = request.args.get('id')
    SellerController().delete(id)

    return redirect('/seller')
