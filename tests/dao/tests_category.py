from backend.dao.db.dao_base import BaseDao
from backend.models.base_model import BaseModel
from backend.models.category import Category
from backend.dao.db.dao_category import CategoryDao


name_ = 'Smartphones'
description_ = 'Telefones inteligentes'


def run_test_dao_categories():
    try:
        obj_instance()
        dao_instance()
        methods()
        print('\033[42;1;30m'+'all dao.category tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' +
              'some test from dao.category FAILED'+'\033[0;0m')
        raise asserterror


def obj_instance():
    obj = Category(name_, description_)
    assert isinstance(
        obj, BaseModel), '[in dao test] Objeto base model não é do tipo esperado'
    assert isinstance(
        obj, Category), '[in dao test] Objeto category não é do tipo esperado'
    return obj


def dao_instance():
    dao = CategoryDao()
    assert isinstance(
        dao, BaseDao), '[in dao test] Objeto base dao não é do tipo esperado'
    assert isinstance(
        dao, CategoryDao), '[in dao test] Objeto category dao não é do tipo esperado'
    return dao


def methods():
    obj = obj_instance()
    dao = dao_instance()

    result = dao.save(obj)
    assert result != None, '[in dao test] O retorno de dao.save não é o esperado'

    list_all = dao.read_all()
    assert isinstance(
        list_all, list), '[in dao test] O retorno de dao.read_all não é o esperado'

    obj_update = dao.read_by_id(result)
    assert isinstance(
        obj_update, Category), '[in dao test] O retorno de dao.read_by_id não é o esperado'

    assert obj_update.name == name_, '[in dao test] O resultado de obj.name para save não é satisfatório'
    assert obj_update.description == description_, '[in dao test] O resultado de obj.description para save não é satisfatório'

    name2_ = 'Televisores'
    description2_ = 'Televisores FullHD'
    obj_update.name = name2_
    obj_update.description = description2_
    dao.save(obj_update)

    result_update = dao.read_by_id(result)
    assert result_update.name == name2_, '[in dao test] O resultado de obj.name para udpate não é satisfatório'
    assert result_update.description == description2_, '[in dao test] O resultado de obj.description para update não é satisfatório'

    dao.delete(result_update)
    result_delete = dao.read_by_id(result)
    assert result_delete == None, '[in dao test] O retorno de dao.delete não é o esperado'
