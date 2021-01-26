from sqlalchemy.orm.session import Session as AlchemySession

from backend.dao.db.dao_base import BaseDao
from backend.dao.db.dao_log import LogDao
from backend.dao.db.session import Session
from backend.models.log import Log


def test_log_dao_instance():
    dao = LogDao()
    assert isinstance(dao, LogDao)
    assert isinstance(dao, BaseDao)


def test_read_all():
    dao = LogDao()
    logs = dao.read_all()
    assert isinstance(logs, list)
    assert all(isinstance(item, Log) for item in logs)


def test_save():
    dao = LogDao()
    data = 'Listed Tests'
    log = Log(data)
    returned_id = dao.save(log)
    saved_log = dao.read_by_id(returned_id)

    assert isinstance(log, Log)
    assert isinstance(saved_log, Log)
    assert log.data == saved_log.data


def test_save_existing_log_should_raise_exception():
    dao = LogDao()
    data = 'Listed Tests'
    log = Log(data)
    returned_id = dao.save(log)
    saved_log = dao.read_by_id(returned_id)

    saved_log.data = 'Test'

    try:
        dao.save(saved_log)
        raise AssertionError('PermissionError exception not raised!')
    except PermissionError as e:
        assert isinstance(e, PermissionError)
        assert e.args == ('You cannot modify a Log.',)


def test_delete_log_should_raise_exception():
    dao = LogDao()
    data = 'Listed Tests'
    log = Log(data)
    returned_id = dao.save(log)
    saved_log = dao.read_by_id(returned_id)

    try:
        dao.delete(saved_log)
        raise AssertionError('PermissionError exception not raised!')
    except PermissionError as e:
        assert isinstance(e, PermissionError)
        assert e.args == ('You cannot delete a Log.',)


def test_session():
    session = Session()
    inside_session = session.__enter__()
    assert isinstance(session, Session)
    assert isinstance(inside_session, AlchemySession)


def run_test_dao_log():
    try:
        test_log_dao_instance()
        test_save()
        test_save_existing_log_should_raise_exception()
        test_delete_log_should_raise_exception()
        test_read_all()
        test_session()

        print('\033[42;1;30m' + 'all dao.log tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from dao.log FAILED' + '\033[0;0m')
        raise asserterror
