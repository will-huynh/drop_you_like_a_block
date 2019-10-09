from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import logging, logging.handlers
import threading
import os
from time import sleep

"""Handle navigation to BlockDrop game page."""
def open_game(driver, link="https://arcade-7e162.web.app/blockdrop"):
    logging.info("Opening BlockDrop game at: {}".format(link))
    driver.get(link)

"""Get bottom-row cells which contain colors (blocks)."""
def get_colored_cells(driver, cells_in_row=12, row_id_factor=14, cell_id="Cell#", signal_attr="block selected"):
    cell_ids = []
    colored_cells = []
    logging.info("Creating HTML IDs for bottom-row cell elements.")
    for i in range(0, cells_in_row):
        cell_ids.append("{0}{1}".format(cell_id, row_id_factor*(i+1)))
    logging.info("Finding bottom-row cells with blocks.")
    for id in cell_ids:
        cell = driver.find_element_by_id(id)
        if signal_attr in cell.get_attribute('class'):
            colored_cells.append(cell)
    if colored_cells is None:
        logging.warning("No bottom-row cells contain blocks.")
    else:
        logging.warning("Bottom-row cells contain blocks, returning applicable cells.")
        return colored_cells

"""Click all given cells."""
def click_cells(driver, cells):
    logging.info("Clicking given cells.")
    for cell in cells:
        cell.click()
    logging.info("All cells clicked.")

"""Interrupt method for game."""
def interrupt_thread(check_interrupt):
    interrupt_input = str(input())
    check_interrupt.append(True)

"""Perform all actions required to play the game."""
def play_game(driver):
    open_game(driver)
    interrupt_game = []
    threading.Thread(target=interrupt_thread, args=(interrupt_game,)).start()
    logging.warning("Playing game, quit at any time by entering any key into the console.")
    while not interrupt_game:
        click_cells(driver, get_colored_cells(driver))

"""Initialize required services and run the main script."""
def main():
    logger = logging.getLogger()
    console_handler = logging.StreamHandler()
    file_handler = logging.handlers.TimedRotatingFileHandler(filename='drop_you_like_a_block.log', when='d', interval=1, backupCount=14)
    log_format = '%(name)s | %(asctime)s | %(levelname)s | %(message)s'
    formatter = logging.Formatter(fmt=log_format)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    cd_path = os.path.abspath("chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path=cd_path, options=options)
    play_game(driver)

if __name__ == "__main__":
    main()
