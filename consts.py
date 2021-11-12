from dotenv import load_dotenv, find_dotenv
import  os



load_dotenv(find_dotenv())


API_URL_REQUEST = os.getenv('API_URL_REQUEST')
DATABASE_URL= ''
DATABASE_USERNAME = ''
DATABASE_PASSWORD = ''
