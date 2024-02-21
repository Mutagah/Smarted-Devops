# package that contains the methods to get data from the endpoint
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url =  "https://kmpdc.go.ke/Registers/General_Practitioners.php"

table_data = None

def fetchData():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Sorry, there was an unsuccessful fetching of data")
    else:
        # Getting all data that would be categorized as text and converting is using the html parser to make it easier to manipulate the content
        parsed_html_response = BeautifulSoup(response.text, "html.parser")       
        # Everything that is within the table tag
        table_data = parsed_html_response.find("table")
        return table_data

def dataDisplay():
    
    new_workbook = Workbook()
    # if table_data exists, loop through the data while inserting it in an excel worksheet
    
    if fetchData():
        for number_of_row_entries, row_data in enumerate(fetchData().find_all("tr")):
            #In html data is input as table rows and each row has a table data or a table header.
            for number_of_cell_entries, cell_data in enumerate(row_data.find_all(["th", "td"])):
                # Getting the current active worksheet in the workbook that is yet to be saved
                new_workbook.active.cell(row = number_of_row_entries + 1, column = number_of_cell_entries + 1, value = cell_data.text )
    else:
        print("Check you data fetching method")


    new_workbook.save("general_practitioners_2024.xlsx")

dataDisplay()