"""Tradingview does not give us access to their data, the only accessible chart data are the current information
related to where the cursor is on the chart. This program will scrape those data using selenium and the data path."""

from selenium import webdriver
import pyautogui

import csv
import os
from time import sleep


def get_values():
    """The only way to get the data from Tradingview is to use xpath, here, you may want to custom this
    depending on which data you want to gather."""
    # Closing price
    price = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[3]/div[1]/div/table/tr[1]/td[2]/div/div[3]/div[1]/div/span[4]/span[2]"
    ).text

    # Parabolic SAR
    sar = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[3]/div[1]/div/table/tr[1]/td[2]/div/div[3]/div[2]/div/span[1]/span"
    ).text

    # Difference between closing price and SAR.
    dif_sar = float(price) * 1000 - float(sar) * 1000

    # Klinger
    klinger1 = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[3]/div[1]/div/table/tr[3]/td[2]/div/div[3]/div[1]/div/span[1]/span"
    ).text
    # If the value is > 1000, remove the "K" and multiply by 1000 to get a float.
    try:
        if "K" in klinger1:
            klinger1 = klinger1[:len(klinger1) - 1]
            klinger1 = float(klinger1) * 1000
    # Error may occur if the value is None.
    except:
        pass

    klinger2 = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[3]/div[1]/div/table/tr[3]/td[2]/div/div[3]/div[1]/div/span[2]/span"
    ).text
    # If the value is > 1000, remove the "K" and multiply by 1000 to get a float.
    try:
        if "K" in klinger2:
            klinger2 = klinger2[:len(klinger2) - 1]
            klinger2 = float(klinger2) * 1000
        klinger = float(klinger1) - float(klinger2)
    # Error may occur if the value is None.
    except:
        klinger = 0
        pass

    # RSI
    rsi = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[3]/div[1]/div/table/tr[5]/td[2]/div/div[3]/div[1]/div/span[1]/span"
    ).text

    return price, dif_sar, klinger, rsi


def create_csv():
    """Create the csv file, you can custom this depending on tha data you need."""
    row = ["price", "dif_sar", "klinger", "rsi"]
    if not os.path.exists("csv.csv"):
        with open('csv.csv', 'w', newline="") as write_file:
            writer = csv.writer(write_file)
            writer.writerow(row)


def edit_csv(price, dif_sar, klinger, rsi):
    """Add a new line to the csv file."""
    row = [price, dif_sar, klinger, rsi]
    with open('csv.csv', 'a', newline="") as write_file:
        writer = csv.writer(write_file)
        writer.writerow(row)


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.tradingview.com/#signin")
    except Exception as e:
        print('Error Involving Chrome Driver \n')
        quit()

    create_csv()
    previous_price = 0
    input("""Log in Tradingview, get you chart ready, go to your starting point and press any key to start. \n
    Once you started, put your cursor on the chart, the chart will move to the right and gather the data from your starting point. 
    \n""")
    while True:
        # Once the loop is started, will press the right arrow key to go to the next candle, and add the data to the
        # csv.
        pyautogui.press("right")
        # Some errors may occur if the chart is moving too fast.
        sleep(0.1)
        # Gets the values you want.
        price, dif_sar, klinger, rsi = get_values()
        if price == "n/a":
            continue
        # Add the new line to the csv file.
        if price != previous_price:
            edit_csv(price, dif_sar, klinger, rsi)
            previous_price = price





