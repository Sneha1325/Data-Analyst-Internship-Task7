Python 3.14.0a7 (tags/v3.14.0a7:29af6ce, Apr  8 2025, 11:49:24) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import sqlite3
... import pandas as pd
... import matplotlib.pyplot as plt
... 
... conn = sqlite3.connect("sales_data.db")
... cursor = conn.cursor()
... 
... cursor.execute("""
... CREATE TABLE IF NOT EXISTS sales (
...     id INTEGER PRIMARY KEY AUTOINCREMENT,
...     product TEXT,
...     quantity INTEGER,
...     price REAL
... )
... """)
... 
... sample_data = [
...     ('Apple', 30, 2.5),
...     ('Banana', 50, 1.2),
...     ('Orange', 40, 1.8),
...     ('Grapes', 25, 3.0),
...     ('Mango', 20, 4.0)
... ]
... 
... cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
... conn.commit()
... 
... query = """
... SELECT 
...     product, 
...     SUM(quantity) AS total_qty, 
...     SUM(quantity * price) AS revenue
... FROM sales
... GROUP BY product
... """
... 
... df = pd.read_sql_query(query, conn)
... 
... print("Sales Summary:")
... print(df)
... 
... df.plot(kind='bar', x='product', y='revenue', legend=False)
... plt.title('Revenue by Product')
... plt.xlabel('Product')
... plt.ylabel('Total Revenue')
... plt.tight_layout()
... sssssss
... plt.savefig("sales_chart.png")
... plt.show()
... 
... # Close connection
... conn.close()
