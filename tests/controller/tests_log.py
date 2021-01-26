from backend.controllers.controller_log import LogController
from backend.models.log import Log
from backend.dao.db.dao_log import LogDao


def test_log_instance():
    controller = LogController()
    assert isinstance(controller, LogController)


def test_read_all():
    controller = LogController()
    logs = controller.read_all()
    assert isinstance(logs, list)
    assert all(isinstance(item, Log) for item in logs)


def test_create():
    controller = LogController()
    data = 'Listed Test'
    returned_id = controller.create(data)
    dao = LogDao()
    saved_log = dao.read_by_id(returned_id)

    assert isinstance(saved_log, Log)
    assert data in saved_log.data


def run_test_controller_log():
    try:
        test_log_instance()
        test_create()
        test_read_all()

        print('\033[42;1;30m' + 'all controller.log tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from controller.log FAILED' + '\033[0;0m')
        raise asserterror


run_test_controller_log()
