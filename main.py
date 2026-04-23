from app import create_app
from dotenv import load_dotenv

import os

load_dotenv()


app = create_app()   # ✅ create app at module level

if __name__ == "__main__":
    app.run(debug=True, port=5001)