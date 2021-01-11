from flask import Blueprint, render_template
from backend.controllers.log import list_logs


log = Blueprint(__name__, 'log')


@log.route('/logs', methods=['GET'])
def logs_read():
    logs_data = list_logs()
    return render_template('log/logs.html', title='Logs', data=logs_data)
