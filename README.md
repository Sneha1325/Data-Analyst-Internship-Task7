# Data-Analyst-Internship-Task7
# Task 7: Get Basic Sales Summary from a Tiny SQLite Database using Python

## 📝 Objective
Use SQL inside Python to pull simple sales info (like total quantity sold and total revenue), 
then display the results using print statements and a simple bar chart.

---

## 🧰 Tools Used
- **Python 3**
- **SQLite3** (built into Python)
- **Pandas**
- **Matplotlib**

---

## 📂 Dataset
A small SQLite database file (`sales_data.db`) containing one table called `sales`:
| product | quantity | price |

---

## ⚙️ Steps Performed
1. **Create** a SQLite database and a sales table  
2. **Insert** sample sales data  
3. **Run** SQL queries to get total quantity and revenue by product  
4. **Load** the query results into Pandas DataFrame  
5. **Display** results using `print()`  
6. **Plot** a bar chart using `matplotlib`

---

## 🧠 SQL Query Used
```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
