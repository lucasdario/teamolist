from flask import redirect, request, render_template, Blueprint
from backend.controllers.controller_category import create_category, list_categories, remove_category, edit_category
from backend.models.category import Category


category = Blueprint(__name__, 'category')


@category.route('/category/form', methods=['GET'])
def category_form():
    return render_template('category/form_category.html', titulo='Category')


@category.route('/category/update')
def category_update():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    return render_template(
        'category/form_category.html', titulo='Edit Category', update=True, id=id, name=name, 
        description=description )


@category.route('/category/update', methods=['POST'])
def category_update_save():
    id = request.form.get('id')
    name = request.form.get('nome')
    description = request.form.get('descricao')
    edit_category(id, name, description)
    return redirect('/category')
    

@category.route('/category/delete')
def category_delete():
    id = request.args.get('id')
    remove_category(id)
    return redirect('/category')


@category.route('/category', methods=['GET'])
def category_list():
    categories = list_categories()
    return render_template('category/list_category.html', title='Categories', data=categories)


@category.route('/category', methods=['POST'])
def category_create():
    category = Category(request.form.get('nome'), request.form.get('descricao'))
    create_category(category)
    return redirect('/category')
