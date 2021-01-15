from backend.controllers.controller_marketplace import create_marketplace, list_marketplaces, edit_marketplace,\
    remove_marketplace
from flask import Blueprint, render_template, request, redirect
from backend.models.marketplace import Marketplace

marketplace = Blueprint(__name__, 'marketplace')


@marketplace.route('/marketplace/form', methods=['GET'])
def marketplace_form():
    return render_template('marketplace/form_marketplace.html', titulo='Marketplace')


@marketplace.route('/marketplace', methods=['POST'])
def marketplace_create():
    marketplace = Marketplace(request.form.get('name'), request.form.get('description'))
    create_marketplace(marketplace)
    return redirect('/marketplace')


@marketplace.route('/marketplace', methods=['GET'])
def marketplace_list():
    marketplaces = list_marketplaces()
    return render_template('marketplace/list_marketplace.html', title='Marketplaces', data=marketplaces)


@marketplace.route('/marketplace/update')
def marketplace_update():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')

    return render_template('marketplace/form_marketplace.html', titulo='Edit Marketplace',
                           update=True, id=id, name=name, description=description)


@marketplace.route('/marketplace/update', methods=['POST'])
def marketplace_update_save():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    edit_marketplace(id, name, description)

    return redirect('/marketplace')


@marketplace.route('/marketplace/delete')
def marketplace_delete():
    id = request.args.get('id')
    remove_marketplace(id)

    return redirect('/marketplace')
