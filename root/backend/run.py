from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Database connection string
DATABASE_URL = "mssql+pyodbc://paulc:092%40290Mxx@192.168.1.195/inventory?driver=ODBC+Driver+17+for+SQL+Server"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Query the database
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM slot_master_active"))
            # Convert rows to dictionaries explicitly
            data = [dict(row._mapping) for row in result]  # Use _mapping for SQLAlchemy Row objects
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/test-connection', methods=['GET'])
def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # Simple query to test the connection
        return jsonify({"message": "Database connection successful"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)