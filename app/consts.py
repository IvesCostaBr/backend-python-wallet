from dotenv import load_dotenv, find_dotenv
import  os


load_dotenv(find_dotenv())

SERVER_ROUTE = {
    "url":"127.0.0.1",
    "port":8000
}
DEBUG=False
API_URL_REQUEST = os.getenv('API_URL_REQUEST')
DATABASE_LOCAL="sqlite:///order.db"
DATABASE_URL= f"postgresql+psycopg2://{os.getenv('USER_DATABASE')}:{os.getenv('PASSWORD_DATABASE')}@{os.getenv('DATABASE_URL')}:{os.getenv('PORT_DATABASE')}/{os.getenv('DATABASE')}"

