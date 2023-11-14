import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_element_presence(self, text):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self, name1):
        # logger_name = inspect.stack()[1][3] + name
        logger_name = name1
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("../logs/log.log")
        fmt = '%(asctime)s %(levelname)s [%(name)s] | %(filename)s(%(funcName)s:%(lineno)d) | - %(message)s'
        fm = logging.Formatter(fmt)
        stream_handler.setFormatter(fm)
        file_handler.setFormatter(fm)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        return logger
