from flask import Flask, jsonify, request
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
        # Get pagination parameters from the query string
        page = int(request.args.get('page', 1))  # Default to page 1
        limit = int(request.args.get('limit', 50))  # Default to 50 rows per page
        offset = (page - 1) * limit

        # Query the database with LIMIT and OFFSET for pagination
        with engine.connect() as connection:
            result = connection.execute(text(f"""
                SELECT
                    cl.casino_name,
                    sm.serial_no,
                    v.vendor_name,
                    cab.cabinet_name,
                    th.theme_name
                FROM slot_master_active sm
                JOIN clients.dbo.casinos cl ON sm.casino_id = cl.reference_key
                JOIN vendors.dbo.vendors v ON sm.vendor_id = v.reference_key
                JOIN vendors.dbo.cabinets cab ON sm.cabinet_id = cab.reference_key
                JOIN vendors.dbo.themes th ON sm.theme_id = th.reference_key
                ORDER BY sm.serial_no
                OFFSET :offset ROWS FETCH NEXT :limit ROWS ONLY
            """), {"offset": offset, "limit": limit})
            
            # Convert rows to dictionaries explicitly
            data = [dict(row._mapping) for row in result]

        # Return the paginated data along with metadata
        return jsonify({
            "data": data,
            "page": page,
            "limit": limit
        })
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