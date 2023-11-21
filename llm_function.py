#import all necessary libraries
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.prompts.chat import ChatPromptTemplate

#importing and loading .env variables
import dotenv
dotenv.load_dotenv()


def answer_question(question):
    
    """
    The answer_question function processes a user's question within the SQL Agent Chatbot script.
    It utilizes Langchain and the OpenAI language model to generate responses based on the provided question
    and accoding to the prompt engineering.

    Args:
        question (str): The user's input question as a string.

    Returns:
        str: The chatbot's response to the user's question.
    """
    #loading database and creating a SQL agent
    db = SQLDatabase.from_uri("sqlite:///Chinook.db")
    agent_executor = create_sql_agent(
        llm=OpenAI(temperature=0), #allow deterministic responses
        toolkit=SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0)),
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, #agent does not use memory
    )

    #prompt engineering to include information on return and refund policies
    final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """
          If a user asks me about information on refund or return, I should answer based on the following on the following.
          Returns: up to 30 days after invoice date later it is not possible. Refund: up to 7 days of invoice date, 100 percent is returned,
          after that no return is allowed. 

          Otherwise, I can look at the tables in the database to see what I can query.
          Then I should query the schema of the most relevant tables.
         """
         ),
        ("user", "{input}\n ai: "),
    ]
    )
 

    return agent_executor.run(final_prompt.format(input = question))