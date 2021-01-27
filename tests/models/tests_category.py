import re
from backend.models.base_model import BaseModel
from backend.models.category import Category

name_ = 'Perfumes'
description_ = 'Perfumaria feminina e masculina'


def run_test_model_categories():
    try:
        obj_instace()
        obj_types()
        obj_values()
        obj_exceptions()
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
    assert obj.name != '', '[in model test] A saída de "name" está vazia'
    assert len(obj.name) <= 200, '[in model test] A saída de "name" contém mais de 200 caracteres'
    assert re.match(r'^[a-zà-úA-ZÀ-Ú0-9 ]+$', obj.name), '[in model test] A saída de "name" contém caracteres especiais'
    assert len(obj.description) <= 400, '[in model test] A saída de "description" contém mais de 400 caracteres'

def obj_exceptions():
    obj_empty_name_exception()
    obj_special_character_in_name_exception()
    obj_name_lenght_exception()
    obj_description_lenght_exception()


def obj_empty_name_exception():
    try:
        obj = Category('', description_)
        raise NotImplementedError('Exception not raised!')
    except Exception as e:
        assert isinstance(e, AssertionError), '[in model test] A exceção da validação do nome nao é do tipo esperado'
        assert e.args == ('Name cannot be empty',), '[in model test] A saída de "name" não é válida ou igual a entrada'


def obj_special_character_in_name_exception():
    try:
        obj = Category('@', description_)
        raise NotImplementedError('Exception not raised!')
    except ValueError as e:
        assert isinstance(e, ValueError), '[in model test] A exceção da validação do nome não é do tipo esperado'
        assert e.args == ('Invalid characteres in name!',), '[in model test] A saida da exceção da validação do nome não é a esperada'


def obj_name_lenght_exception():
    try:
        obj = Category('n' * 201, description_)
        raise NotImplementedError('Exception not raised!')
    except ValueError as e:
        assert isinstance(e, ValueError), '[in model test] A exceção da validação do nome não é do tipo esperado'
        assert e.args == ('Name must be less than 200 characters!',), '[in model test] A saida da exceção da validação do nome não é a esperada'


def obj_description_lenght_exception():
    try:
        obj = Category(name_, 'n' * 401)
        raise NotImplementedError('Exception not raised!')
    except ValueError as e:
        assert isinstance(e, ValueError), '[in model test] A exceção da validação da descrição não é do tipo esperado'
        assert e.args == ('Description must be less than 400 characters!',), '[in model test] A saida da exceção da validação da descrição não é a esperada'