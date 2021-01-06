from flask import Flask, render_template, request
import sys
sys.path.append('.')
from backend.funcoes import escrever_arquivo, log
from backend.product import product_list
from backend.marketplaces import list_marketplaces


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
        return render_template('cadastro.html', titulo='Seller', op=opcao)
    elif opcao == 'categoria':
        return render_template('cadastro.html', titulo='Categoria', op=opcao)
    else:
        return render_template('index.html', titulo='Marketplace Olist')


@app.route('/gravar')
def gravar_dados():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    desc = str(desc).replace('*', '-').replace('%', '-')
    nome = str(nome).replace('*', '-').replace('%', '-')
    
    if preco is None:
        dado = f'{nome}*{desc}'
        escrever_arquivo(dado, 0, 'a')
        log('gravar_marketplace')
    else:
        dado = f'{nome}*{desc}*{preco}'
        escrever_arquivo(dado, 1, 'a')
        log('gravar_produto')
    return render_template('index.html', titulo='Marketplace Olist')

@app.route('/product-list', methods=['GET'])
def product_listing():
    products_list = product_list()
    return render_template('list.html', title = 'Products', data = products_list)


@app.route('/marketplace', methods=['GET'])
def marketplace_list():
    marketplaces = list_marketplaces()
    print(marketplaces)
    
    return render_template('list.html', title='Marketplaces', data=marketplaces)


app.debug = True

app.run()