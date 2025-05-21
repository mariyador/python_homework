import sqlite3

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        cursor = conn.cursor()

        #Task 1: Complex JOINs with Aggregation
        query = """
        SELECT o.order_id, SUM(li.quantity * p.price) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("Task 1: First 5 Orders Total Price")
        for order_id, total_price in results:
            print(f"Order {order_id}: ${total_price:.2f}")

        #Task 2: Understanding Subqueries
        query2 = """
        SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, SUM(li.quantity * p.price) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) AS sub
        ON c.customer_id = sub.customer_id_b
        GROUP BY c.customer_id
        ORDER BY average_total_price DESC;
        """

        cursor.execute(query2)
        results2 = cursor.fetchall()

        print("Task 2: Average Order Price per Customer")
        for name, avg_price in results2:
            print(f"{name}: ${avg_price:.2f}" if avg_price else f"{name}: No orders")


        #Task 3: An Insert Transaction Based on Data
        try:
            # Get customer_id
            cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
            customer = cursor.fetchone()
            if not customer:
                raise Exception("Customer not found.")
            customer_id = customer[0]

            # Get employee_id
            cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
            employee = cursor.fetchone()
            if not employee:
                raise Exception("Employee not found.")
            employee_id = employee[0]

            # Get 5 cheapest products
            cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
            product_ids = cursor.fetchall()
            if not product_ids:
                raise Exception("Products not found.")

            # Start transaction
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id)
                VALUES (?, ?)
                RETURNING order_id
            """, (customer_id, employee_id))
            order_id = cursor.fetchone()[0]

            # Insert line_items
            for pid in product_ids:
                cursor.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity)
                    VALUES (?, ?, 10)
                """, (order_id, pid[0]))

            conn.commit()

            # Output result
            cursor.execute("""
                SELECT li.line_item_id, li.quantity, p.product_name
                FROM line_items li
                JOIN products p ON li.product_id = p.product_id
                WHERE li.order_id = ?
            """, (order_id,))
            results3 = cursor.fetchall()
            
            print("Task 3: An Insert Transaction Based on Data")
            print(f"Created order ID: {order_id}")
            for line_id, qty, product in results3:
                print(f"Line {line_id}: {qty}x {product}")

        except Exception as e:
            conn.rollback()
            print("Transaction failed:", e) 

        # Task 4: Aggregation with HAVING

        query4 = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
        ORDER BY order_count DESC;
        """

        cursor.execute(query4)
        results4 = cursor.fetchall()

        print("Task 4: Aggregation with HAVING")
        for emp_id, first_name, last_name, count in results4:
            print(f"{emp_id}: {first_name} {last_name} — {count} orders")
        
except sqlite3.Error as e:
    print("Database error", e)