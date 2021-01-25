from flask import redirect, request, render_template, Blueprint
from backend.controllers.controller_category import CategoryController
from backend.models.category import Category


category = Blueprint(__name__, 'category')
_CATEGORY_CONTROLLER = CategoryController()


@category.route('/category/form', methods=['GET'])
def category_form():
    return render_template('category/form_category.html', titulo='Category')


@category.route('/category/update')
def category_update():
    id = request.args.get('id')
    category = _CATEGORY_CONTROLLER.read_by_id(id)
    return render_template(
        'category/form_category.html', titulo='Edit Category', update=True, id=category.id, name=category.name, 
        description=category.description )


@category.route('/category/update', methods=['POST'])
def category_update_save():
    id = request.form.get('id')
    category = CategoryController().read_by_id(id)
    category.name = request.form.get('nome')
    category.description = request.form.get('descricao')
    _CATEGORY_CONTROLLER.update(category)
    return redirect('/category')
    

@category.route('/category/delete')
def category_delete():
    id = request.args.get('id')
    category = CategoryController().read_by_id(id)
    _CATEGORY_CONTROLLER.delete(category)
    return redirect('/category')


@category.route('/category', methods=['GET'])
def category_list():
    categories = _CATEGORY_CONTROLLER.read_all()
    return render_template('category/list_category.html', title='Categories', data=categories)


@category.route('/category', methods=['POST'])
def category_create():
    category = Category(request.form.get('nome'), request.form.get('descricao'))
    _CATEGORY_CONTROLLER.create(category)
    return redirect('/category')
