from langchain import SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

db_user = "postgres"
db_pass = "1q2w3e4r"
db_host = "localhost"
db_name = "dvdrental"

db = SQLDatabase.from_uri(f"postgresql+psycopg2://{db_user}:{db_pass}@localhost:5432/{db_name}")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)


def ask_to_database():
    while True:
        query = input("Database'e sor: ")
        db_chain.run(query)


ask_to_database()