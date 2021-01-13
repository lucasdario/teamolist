from backend.controllers.marketplace import list_marketplaces, create_marketplace
from flask import Blueprint, render_template, request, redirect
from backend.models.marketplace import Marketplace

marketplace = Blueprint(__name__, 'marketplace')


@marketplace.route('/marketplace/form', methods=['GET'])
def marketplace_form():
    return render_template('marketplace/form_marketplace.html', titulo='Marketplace')


@marketplace.route('/marketplace', methods=['GET'])
def marketplace_list():
    marketplaces = list_marketplaces()
    return render_template('marketplace/list_marketplace.html', title='Marketplaces', data=marketplaces)


@marketplace.route('/marketplace', methods=['POST'])
def marketplace_create():
    marketplace = Marketplace(request.form.get('nome'), request.form.get('descricao'))
    create_marketplace(marketplace)
    return redirect('/marketplace')
