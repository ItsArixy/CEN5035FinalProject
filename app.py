import connection
import bs4 as BeautifulSoup
import requests

conn = connection.connect_to_database("localhost", "root", "myLildiddle11", "stock_data")
# create the database and create an html parser to look through public stock trackers
# create a table to store stock data that scans public stock trackers 
conn.execute("""
CREATE TABLE IF NOT EXISTS stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10),
    price DECIMAL(10, 2),
    volume INT
)
""")
# create a function that gathers stock data from public stock trackers and inserts it into the database
def gather_stock_data():
    # use requests to get the html from a public stock tracker
    url = "https://finance.yahoo.com/most-active"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # find the table that contains the stock data
    table = soup.find("table", {"class": "W(100%)"})
    # loop through the rows of the table and extract the stock data
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        symbol = cols[0].text.strip()
        price = float(cols[2].text.strip().replace(",", ""))
        volume = int(cols[6].text.strip().replace(",", ""))
        # insert the stock data into the database
        conn.execute("INSERT INTO stock_data (symbol, price, volume) VALUES (%s, %s, %s)", (symbol, price, volume))