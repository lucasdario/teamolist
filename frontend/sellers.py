from flask import render_template, request, redirect, Blueprint
from backend.controllers.seller import create_seller, list_sellers
from backend.models.seller import Seller

seller = Blueprint(__name__, 'seller')


@seller.route('/seller/form', methods=['GET'])
def seller_form():
    return render_template('seller/form_seller.html', titulo='Seller')


@seller.route('/seller', methods=['GET'])
def seller_list_():
    sellers = list_sellers()
    return render_template('seller/list_seller.html', title='Sellers', data=sellers)


@seller.route('/seller', methods=['POST'])
def seller_create():
    seller = Seller(request.form.get('nome'), request.form.get('telefone'), request.form.get('email'))
    create_seller(seller)
    return redirect('/seller')
