import webbrowser
import logging

from url_helper import UrlHelper

logging.basicConfig(
    filename=r'C:\temp\python_logs\pyort_swapper_failures.log',
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    filemode='a',
    level=logging.DEBUG
)


try:
    url_helper = UrlHelper()
    url = url_helper.get_url()
    modified_url = url_helper.parse_modify_url(url)
    webbrowser.get(url_helper.chrome_path).open(modified_url, 2)

except Exception as e:
    logging.error("Port swapper failed.")
    exit(0)

