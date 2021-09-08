import sys

import uvicorn
from dotenv import load_dotenv

load_dotenv()

from app.api import create_app
from app.config import AppConfig
from app.infrastructures.persistence import create_tables
from app.modules.container import AppContainer


container = AppContainer()
container.config.from_pydantic(AppConfig())
container.wire(packages=[sys.modules["app"]])
create_tables(container.db())
app_ = create_app(container)

if __name__ == "__main__":
    uvicorn.run(app_, host="0.0.0.0", port=8000)
