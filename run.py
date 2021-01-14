from backend.dao.db import Connection
from frontend.main import app

if __name__ == "__main__":
    Connection().create_tables()
    app.run(debug=True)
