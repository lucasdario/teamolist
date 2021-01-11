from flask import Blueprint, render_template
from backend.funcoes import read_log


log = Blueprint(__name__, 'log')


@log.route('/logs', methods=['GET'])
def logs_read():
    logs_data = read_log()
    return render_template('log/logs.html', title='Logs', data=logs_data)
