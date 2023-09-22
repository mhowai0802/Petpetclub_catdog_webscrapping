from ig_common import *
from dotenv import load_dotenv

load_dotenv()

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

list_tag = get_tag_name('#cat', driver)
print(list_tag)
list_of_account = get_user_name(list_tag, driver)
print(list_of_account)
