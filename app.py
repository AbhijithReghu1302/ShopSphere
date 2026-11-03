
from flask import Flask, render_template, request, jsonify
import os
import oracledb

app = Flask(__name__)

DB_CONFIG = {
    "user": "SHOPSPHERE",
    "password": os.getenv("ORACLE_PASSWORD"),
    "dsn": "localhost:1521/FREEPDB1"
}


def get_connection():
    return oracledb.connect(**DB_CONFIG)


# HOME PAGE - FETCH PRODUCTS FROM ORACLE
@app.route("/")
def home():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT PRODUCT_ID, PRODUCT_NAME, PRICE, STOCK_QUANTITY
            FROM PRODUCTS
            ORDER BY PRODUCT_ID
        """)

        rows = cursor.fetchall()

        products = [
            {
                "id": row[0],
                "name": row[1],
                "price": float(row[2]),
                "stock": row[3]
            }
            for row in rows
        ]

        cursor.close()
        return render_template("index.html", products=products)

    except Exception as error:
        return f"Unable to load products: {error}", 500

    finally:
        if connection:
            connection.close()


# DISCOUNT CALCULATOR - CALL ORACLE PL/SQL FUNCTION
@app.route("/calculate-discount", methods=["POST"])
def calculate_discount():
    connection = None

    try:
        data = request.get_json()
        amount = float(data.get("amount", 0))

        if amount <= 0:
            return jsonify({"error": "Enter an amount greater than zero."}), 400

        connection = get_connection()
        cursor = connection.cursor()

        discount = cursor.callfunc(
            "CALCULATE_DISCOUNT",
            oracledb.NUMBER,
            [amount]
        )

        final_amount = amount - float(discount)

        cursor.close()

        return jsonify({
            "original_amount": amount,
            "discount": float(discount),
            "final_amount": final_amount
        })

    except Exception as error:
        return jsonify({"error": str(error)}), 500

    finally:
        if connection:
            connection.close()


# START FLASK APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
