import time
import mysql.connector

def maintain_latest_500_records():
    # Database connection
    conn = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor()

    while True:
        # Check the row count
        cursor.execute("SELECT COUNT(*) FROM my_table")
        row_count = cursor.fetchone()[0]

        # Delete the oldest record if the row count exceeds 500
        if row_count > 500:
            cursor.execute("DELETE FROM my_table ORDER BY id LIMIT 1")
            conn.commit()

        # Sleep for a short interval before checking again
        time.sleep(1)  # Adjust the sleep interval as needed

    # Close the connection (this will never be reached in this loop)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    maintain_latest_500_records()