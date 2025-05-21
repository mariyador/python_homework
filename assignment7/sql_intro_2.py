import pandas as pd
import sqlite3

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        sql = """
        SELECT 
            li.line_item_id, 
            li.quantity, 
            li.product_id, 
            p.product_name, 
            p.price 
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        """
        df = pd.read_sql_query(sql, conn)
        print("First 5 rows:")
        print(df.head())

        df['total'] = df['quantity'] * df['price']
        print("With 'total' column:")
        print(df.head())

        summary = df.groupby('product_id').agg({
            'line_item_id': 'count',
            'total': 'sum',
            'product_name': 'first'
        })
        summary = summary.sort_values(by='product_name')
        print("Summary grouped by product_id:")
        print(summary.head())

        summary.to_csv("order_summary.csv")
        print("CSV file 'order_summary.csv' has been created.")


except sqlite3.Error as e:
    print("Database error:", e)