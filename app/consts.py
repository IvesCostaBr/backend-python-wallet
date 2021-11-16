from dotenv import load_dotenv, find_dotenv
import  os


load_dotenv(find_dotenv())

SERVER_ROUTE = {
    "url":"127.0.0.1",
    "port":8000
}
DEBUG=True
API_URL_REQUEST = os.getenv('API_URL_REQUEST')
