from flask import render_template, request, redirect, Blueprint
from backend.controllers.controller_seller import SellerController
from backend.models.seller import Seller

seller = Blueprint(__name__, 'seller')
_SELLER_CONTROLLER = SellerController()


@seller.route('/seller/form', methods=['GET'])
def seller_form():
    return render_template('seller/form_seller.html', titulo='Seller')


@seller.route('/seller', methods=['POST'])
def seller_create():
    seller = Seller(request.form.get('name'), request.form.get('phone'), request.form.get('email'))
    _SELLER_CONTROLLER.create(seller)
    return redirect('/seller')


@seller.route('/seller', methods=['GET'])
def seller_list_():
    sellers = _SELLER_CONTROLLER.read_all()
    return render_template('seller/list_seller.html', title='Sellers', data=sellers)


@seller.route('/seller/update')
def seller_update():
    id = request.args.get('id')
    seller = _SELLER_CONTROLLER.read_by_id(id)
    return render_template('seller/form_seller.html', titulo='Edit Seller',
                           update=True, id=id, name=seller.name, phone=seller.phone, email=seller.email)


@seller.route('/seller/update', methods=['POST'])
def seller_update_save():
    id = request.form.get('id')
    seller = SellerController().read_by_id(id)
    seller.name = request.form.get('name')
    seller.phone = request.form.get('phone')
    seller.email = request.form.get('email')
    _SELLER_CONTROLLER.update(seller)
    return redirect('/seller')


@seller.route('/seller/delete')
def seller_delete():
    id = request.args.get('id')
    seller = SellerController().read_by_id(id)
    _SELLER_CONTROLLER.delete(seller)
    return redirect('/seller')
