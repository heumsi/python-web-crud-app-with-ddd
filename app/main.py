import uvicorn
from dotenv import load_dotenv

from app import create_app

load_dotenv()

app_ = create_app()

if __name__ == "__main__":
    uvicorn.run(app_, host="0.0.0.0", port=8000)
