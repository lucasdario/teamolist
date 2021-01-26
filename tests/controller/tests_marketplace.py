import sys
sys.path.append('.')

from backend.controllers.controller_marketplace import MarketplaceController
from backend.models.marketplace import Marketplace

def test_controller_marketplace_instance():
    mkt=MarketplaceController()
    assert isinstance(mkt.read_all(),list)
    assert isinstance(mkt.read_by_id(mkt.read_all()[0].id),Marketplace)


def test_controller_marketplace_save():
    mkt=MarketplaceController()
    obj_mkt=Marketplace('FastShop','Loja online')
    id_aux=mkt.create(obj_mkt)
    mkt_aux=mkt.read_by_id(id_aux)    
    assert id_aux==mkt_aux.id
    assert mkt_aux.name==obj_mkt.name
    assert mkt_aux.description==obj_mkt.description
    assert isinstance(mkt_aux.name,str)
    assert isinstance(mkt_aux.description,str)

def test_controller_marketplace_delete():
    mkt=MarketplaceController()
    id_aux=mkt.delete(mkt.read_all()[0])
    assert mkt.read_by_id(id_aux) == None

def test_controller_marketplace_update():
    mkt=MarketplaceController()
    mkt_aux=mkt.read_by_id(mkt.read_all()[0].id)
    mkt_aux.name="Mudou nome"
    mkt_aux.description="Mudou descricao"
    id_aux=mkt.update(mkt_aux)
    mkt_aux2=mkt.read_by_id(id_aux)
    assert mkt_aux.name==mkt_aux2.name    
    assert mkt_aux.description==mkt_aux2.description

def run_test_controller_marketplace():
    try:
        test_controller_marketplace_instance()
        test_controller_marketplace_save()
        test_controller_marketplace_delete()
        test_controller_marketplace_update()
        print('\033[42;1;30m'+'all controller.marketplace tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+'some test from controller.marketplace FAILED'+'\033[0;0m')
        raise asserterror