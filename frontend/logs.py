from flask import Blueprint, render_template
from backend.controllers.controller_log import LogController


log = Blueprint(__name__, 'log')


@log.route('/logs', methods=['GET'])
def logs_read():
    logs_data = LogController().read_all()
    return render_template('log/logs.html', title='Logs', data=logs_data)
