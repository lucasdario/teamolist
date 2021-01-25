from backend.controllers.controller_marketplace import MarketplaceController
from flask import Blueprint, render_template, request, redirect
from backend.models.marketplace import Marketplace

marketplace = Blueprint(__name__, 'marketplace')
_MARKETPLACE_CONTROLLER = MarketplaceController()


@marketplace.route('/marketplace/form', methods=['GET'])
def marketplace_form():
    return render_template('marketplace/form_marketplace.html', titulo='Marketplace')


@marketplace.route('/marketplace', methods=['POST'])
def marketplace_create():
    marketplace = Marketplace(request.form.get('name'), request.form.get('description'))
    _MARKETPLACE_CONTROLLER.create(marketplace)
    return redirect('/marketplace')


@marketplace.route('/marketplace', methods=['GET'])
def marketplace_list():
    marketplaces = _MARKETPLACE_CONTROLLER.read_all()
    return render_template('marketplace/list_marketplace.html', title='Marketplaces', data=marketplaces)


@marketplace.route('/marketplace/update')
def marketplace_update():
    id = request.args.get('id')
    marketplace = _MARKETPLACE_CONTROLLER.read_by_id(id)
    return render_template('marketplace/form_marketplace.html', titulo='Edit Marketplace',
                           update=True, id=marketplace.id, name=marketplace.name, description=marketplace.description)


@marketplace.route('/marketplace/update', methods=['POST'])
def marketplace_update_save():
    id = request.form.get('id')
    marketplace = MarketplaceController().read_by_id(id)
    marketplace.name = request.form.get('name')
    marketplace.description = request.form.get('description')
    _MARKETPLACE_CONTROLLER.update(marketplace)
    return redirect('/marketplace')


@marketplace.route('/marketplace/delete')
def marketplace_delete():
    id = request.args.get('id')
    marketplace = MarketplaceController().read_by_id(id)
    _MARKETPLACE_CONTROLLER.delete(marketplace)
    return redirect('/marketplace')
