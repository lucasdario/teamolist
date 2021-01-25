import sys
sys.path.append('.')

from backend.dao.db.dao_marketplace import MarketplaceDao
from backend.models.marketplace import Marketplace


def test_dao_marketplace_instance():
    obj=MarketplaceDao()
    assert isinstance(obj.read_all(),list)
    assert isinstance(obj.read_by_id(obj.read_all()[0].id),Marketplace)

def test_dao_marketplace_save():
    obj = MarketplaceDao()
    obj_mkt = Marketplace('Shops do Ze','Smarthphone e Video game')
    id_aux=obj.save(obj_mkt)
    obj_aux=obj.read_by_id(id_aux)
    assert id_aux==obj_aux.id
    assert obj_mkt.name == obj_aux.name
    assert obj_mkt.description == obj_aux.description
    assert isinstance(obj_aux.name,str)
    assert isinstance(obj_aux.description,str)

def test_dao_marketplace_delete():
    obj = MarketplaceDao()
    id_aux=obj.delete(obj.read_all()[0])
    obj_aux=obj.read_by_id(id_aux)
    assert obj_aux == None   

def run_test_dao_marketplace():
    try:
        test_dao_marketplace_instance()
        test_dao_marketplace_save()
        test_dao_marketplace_delete()
        print('\033[42;1;30m'+'all dao.marketplace tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+'some test from dao.marketplace FAILED'+'\033[0;0m')
        raise asserterror