from tests.models.tests_marketplace import run_test_model_marketplace
from tests.models.tests_category import run_test_model_categories
from tests.dao.tests_category import run_test_dao_categories
from tests.models.tests_product import run_test_model_product
from tests.models.tests_seller import run_test_model_seller
from tests.models.tests_log import run_test_model_log
from tests.dao.tests_log import run_test_dao_log
from dotenv import load_dotenv

load_dotenv()

run_test_model_marketplace()
run_test_model_product()
run_test_model_categories()
run_test_model_seller()
run_test_model_log()
run_test_dao_log()
run_test_dao_categories()
