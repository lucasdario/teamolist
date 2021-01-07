from flask import Flask, render_template, request, redirect
import sys
sys.path.append('.')

from backend.funcoes import escrever_arquivo, log, read_log
from backend.product import list_product
from backend.marketplaces import list_marketplaces
from backend.seller import create_seller, seller_list
from backend.categories import create_category, list_categories


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html', titulo='Marketplace Olist')


@app.route('/cadastro')
def view_cadastro():
    opcao = request.args.get('opcao')

    if opcao == 'marketplace':
        return render_template('cadastro.html', titulo='Marketplace', op=opcao)
    elif opcao == 'produto':
        return render_template('cadastro.html', titulo='Produto', op=opcao)
    elif opcao == 'seller':
        return render_template('cadastro_seller.html', titulo='Seller', op=opcao)
    elif opcao == 'category':
        return render_template('form_category.html', titulo='Category')
    else:
        return render_template('index.html', titulo='Marketplace Olist')


@app.route('/gravar')
def gravar_dados():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    ref = request.args.get('ref')
    desc = str(desc).replace('*', '-').replace('%', '-')
    nome = str(nome).replace('*', '-').replace('%', '-')
    
    if ref == 'marketplace':
        dado = f'{nome}*{desc}'
        escrever_arquivo(dado, ref, 'a')
        log('Created Marketplace')
    elif ref == 'product':
        dado = f'{nome}*{desc}*{preco}'
        escrever_arquivo(dado, ref, 'a')
        log('Created Product')
    return render_template('index.html', titulo='Marketplace Olist')

@app.route('/product', methods=['GET'])
def product_list():
    products_list = list_product()
    return render_template('list.html', title = 'Products', data = products_list)


@app.route('/marketplace', methods=['GET'])
def marketplace_list():
    marketplaces = list_marketplaces()
    return render_template('list.html', title='Marketplaces', data=marketplaces)

@app.route('/seller', methods=['POST'])
def seller_registration():
    seller = request.form
    create_seller(seller)
    return redirect('/seller')

@app.route('/seller', methods=['GET'])
def seller_listing():
    sellers = seller_list()
    return render_template('listing_seller.html', title='Sellers', data=sellers)

@app.route('/category', methods=['GET'])
def category_list():
    categories = list_categories()
    return render_template('list.html', title='Categories', data=categories)


@app.route('/category', methods=['POST'])
def category_create():
    category_data = request.form
    create_category(category_data)
    return redirect('/category')


@app.route('/logs', methods=['GET'])
def logs_read():
    logs_data = read_log()
    return render_template('logs.html', title='Logs', data=logs_data)


app.debug = True

app.run()
