from backend.controllers.controller_base import BaseController
from backend.models.base_model import BaseModel
from backend.models.category import Category
from backend.controllers.controller_category import CategoryController


name_ = 'Tênis'
description_ = 'Tênis para corrida'


def run_test_controller_categories():
    try:
        obj_instance()
        controller_instance()
        methods()
        print('\033[42;1;30m' +
              'all controller.category tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' +
              'some test from controller.category FAILED'+'\033[0;0m')
        raise asserterror


def obj_instance():
    obj = Category(name_, description_)
    assert isinstance(
        obj, BaseModel), '[in controller test] Objeto base model não é do tipo esperado'
    assert isinstance(
        obj, Category), '[in controller test] Objeto category não é do tipo esperado'
    return obj


def controller_instance():
    controller = CategoryController()
    assert isinstance(
        controller, BaseController), '[in controller test] Objeto base controller não é do tipo esperado'
    assert isinstance(
        controller, BaseController), '[in controller test] Objeto category controller não é do tipo esperado'
    return controller


def methods():
    obj = obj_instance()
    controller = controller_instance()

    result = controller.create(obj)
    assert result != None, '[in controller test] O retorno de controller.save não é o esperado'

    list_all = controller.read_all()
    assert isinstance(
        list_all, list), '[in controller test] O retorno de controller.read_all não é o esperado'

    obj_update = controller.read_by_id(result)
    assert isinstance(
        obj_update, Category), '[in controller test] O retorno de controller.read_by_id não é o esperado'

    assert obj_update.name == name_, '[in controller test] O resultado de obj.name para save não é satisfatório'
    assert obj_update.description == description_, '[in controller test] O resultado de obj.description para save não é satisfatório'

    name2_ = 'Eletrodomesticos'
    description2_ = 'Linha branca'
    obj_update.name = name2_
    obj_update.description = description2_
    controller.update(obj_update)

    result_update = controller.read_by_id(result)
    assert result_update.name == name2_, '[in controller test] O resultado de obj.name para udpate não é satisfatório'
    assert result_update.description == description2_, '[in controller test] O resultado de obj.description para update não é satisfatório'

    controller.delete(result_update)
    result_delete = controller.read_by_id(result)
    assert result_delete == None, '[in controller test] O retorno de controller.delete não é o esperado'
