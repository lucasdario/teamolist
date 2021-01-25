from tests.models.tests_category import start_all
from tests.models.tests_product import TestProduct
from tests.models.tests_seller import run_test_model_seller


TestProduct().test()
start_all()
run_test_model_seller()