from flask import Flask, render_template

from frontend.marketplaces import marketplace
from frontend.products import product
from frontend.sellers import seller
from frontend.categories import category
from frontend.logs import log

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.register_blueprint(marketplace)
app.register_blueprint(product)
app.register_blueprint(seller)
app.register_blueprint(category)
app.register_blueprint(log)


@app.route('/')
def index():
    return render_template('index.html', titulo='Marketplace Olist')
