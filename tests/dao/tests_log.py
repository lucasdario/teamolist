from backend.dao.db.dao_base import BaseDao
from backend.dao.db.dao_log import LogDao
from backend.models.log import Log
from backend.dao.db.session import Session
from sqlalchemy.orm.session import Session as AlchemySession


def test_log_instance():
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
    data = '25/01/2021 às 13:37:20 => Listed Tests'
    log = Log(data)
    returned_id = dao.save(log)
    saved_log = dao.read_by_id(returned_id)

    assert isinstance(log, Log)
    assert isinstance(saved_log, Log)
    assert log.data == saved_log.data


def test_session():
    session = Session()
    inside_session = session.__enter__()
    assert isinstance(session, Session)
    assert isinstance(inside_session, AlchemySession)


def run_test_dao_log():
    try:
        test_log_instance()
        test_save()
        test_read_all()
        test_session()

        print('\033[42;1;30m' + 'all dao.log tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from dao.log FAILED' + '\033[0;0m')
        raise asserterror
