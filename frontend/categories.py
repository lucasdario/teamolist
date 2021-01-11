from flask import redirect, request, render_template, Blueprint
from backend.categories import create_category, list_categories


category = Blueprint(__name__, 'category')


@category.route('/category/form', methods=['GET'])
def category_form():
    return render_template('category/form_category.html', titulo='Category')


@category.route('/category', methods=['GET'])
def category_list():
    categories = list_categories()
    return render_template('category/list_category.html', title='Categories', data=categories)


@category.route('/category', methods=['POST'])
def category_create():
    category_data = request.form
    create_category(category_data)
    return redirect('/category')
