from app.main import *
from app.consts import *
from multiprocessing import Process
import sys
import uvicorn


if __name__ == '__main__':
    try:
        uvicorn.run(app="server:app",
                    host=SERVER_ROUTE["url"],
                    port=SERVER_ROUTE["port"],
                    debug=DEBUG)
    except:
        sys.exit()
