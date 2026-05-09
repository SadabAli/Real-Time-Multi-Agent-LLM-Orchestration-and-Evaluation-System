import sqlite3
import time


def sql_tool(query: str):

    start = time.time()

    try:

        conn = sqlite3.connect(":memory:")

        cursor = conn.cursor()

        cursor.execute(
            '''
            CREATE TABLE users (
                id INTEGER,
                name TEXT
            )
            '''
        )

        cursor.execute(
            '''
            INSERT INTO users VALUES
            (1, 'Sadab')
            '''
        )

        cursor.execute(
            "SELECT * FROM users"
        )

        results = cursor.fetchall()

        latency = round(time.time() - start, 2)

        return {
            "status": "success",
            "tool_name": "sql_tool",
            "result": results,
            "latency": latency,
            "error": None
        }

    except Exception as e:

        return {
            "status": "failure",
            "tool_name": "sql_tool",
            "result": None,
            "latency": 0,
            "error": str(e)
        }