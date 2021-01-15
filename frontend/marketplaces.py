from backend.controllers.controller_marketplace import MarketplaceController
from flask import Blueprint, render_template, request, redirect
from backend.models.marketplace import Marketplace

marketplace = Blueprint(__name__, 'marketplace')


@marketplace.route('/marketplace/form', methods=['GET'])
def marketplace_form():
    return render_template('marketplace/form_marketplace.html', titulo='Marketplace')


@marketplace.route('/marketplace', methods=['POST'])
def marketplace_create():
    marketplace = Marketplace(request.form.get('name'), request.form.get('description'))
    MarketplaceController().create(marketplace)
    return redirect('/marketplace')


@marketplace.route('/marketplace', methods=['GET'])
def marketplace_list():
    marketplaces = MarketplaceController().read_all()
    return render_template('marketplace/list_marketplace.html', title='Marketplaces', data=marketplaces)


@marketplace.route('/marketplace/update')
def marketplace_update():
    id = request.args.get('id')
    marketplace = MarketplaceController().read_by_id(id)

    return render_template('marketplace/form_marketplace.html', titulo='Edit Marketplace',
                           update=True, id=marketplace.id, name=marketplace.name, description=marketplace.description)


@marketplace.route('/marketplace/update', methods=['POST'])
def marketplace_update_save():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')

    marketplace = Marketplace(name, description, id)
    MarketplaceController().update(marketplace)

    return redirect('/marketplace')


@marketplace.route('/marketplace/delete')
def marketplace_delete():
    id = request.args.get('id')
    MarketplaceController().delete(id)

    return redirect('/marketplace')
