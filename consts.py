from dotenv import load_dotenv, find_dotenv
import  os



load_dotenv(find_dotenv())

SERVER_ROUTE = {
    "url":"localhost",
    "port":8000
}

API_URL_REQUEST = os.getenv('API_URL_REQUEST')
DATABASE_URL= ''
DATABASE_USERNAME = ''
DATABASE_PASSWORD = ''
