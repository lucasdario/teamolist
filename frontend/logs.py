from flask import Blueprint, render_template
from backend.controllers.controller_log import LogController


log = Blueprint(__name__, 'log')
_LOG_CONTROLLER = LogController()


@log.route('/logs', methods=['GET'])
def logs_read():
    logs_data = _LOG_CONTROLLER.read_all()
    return render_template('log/logs.html', title='Logs', data=logs_data)
