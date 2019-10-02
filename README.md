# tradingview_scraper
This scraper will allow you to scrape any data from any indicator on any chart. You do not have to use a shared chart.


# Requirements
- Python
- pyautogui `pip install pyautogui`
 - selenium `pip install selenium`


# Usage
The only way to get datas from real-time charts on tradingview in to use the items path. So first thing to do is to open a chart
with the indicators you want. Then custom the function get_values with the corresponding paths. 
<br/><br/>
Once this is done, run the program. It will open a chrome page, go to the desired chart, select a starting point, and press any key on 
the console. 
<br/><br/>
Go back to your chart, the chart will now move to the next candle and add the data to the csv file. Close the program when you are done.

