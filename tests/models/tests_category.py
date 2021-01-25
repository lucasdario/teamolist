from backend.models.base_model import BaseModel
from backend.models.category import Category

name_ = 'Perfumes'
description_ = 'Perfumaria feminina e masculina'


def run_test_model_categories():
    try:
        obj_instace()
        obj_types()
        obj_values()
        print('\033[42;1;30m'+'all model.category tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' +
              'some test from model.category FAILED'+'\033[0;0m')
        raise asserterror


def obj_instace():
    obj = Category(name_, description_)
    assert isinstance(
        obj, BaseModel), '[in model test] O objeto category não é do tipo esperado'
    assert isinstance(
        obj, Category), '[in model test] O objeto category não é do tipo esperado'
    return obj


def obj_types():
    obj = obj_instace()
    assert isinstance(
        obj.name, str), '[in model test] O retorno para category.name não é do tipo esperado'
    assert isinstance(
        obj.description, str), '[in model test] O retorno para category.description não é do tipo esperado'


def obj_values():
    obj = obj_instace()
    assert obj.name == name_, '[in model test] A saída de "name" não é válida ou igual a entrada'
    assert obj.description == description_, '[in model test] A saída de "description" não é válida ou igual a entrada'
