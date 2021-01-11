from backend.dao.db import create_tables
from frontend.main import app

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
