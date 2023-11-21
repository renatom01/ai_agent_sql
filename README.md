# Langchain SQL Agent Bot

This Python script utilizes the Langchain library to interact with a SQL database and answer user queries. The Langchain library integrates natural language processing capabilities with SQL database interactions, allowing users to ask questions and receive relevant information from the connected database.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https: XXXXXXXXX
   ```

2. **Navigate to the project directory:**

   ```bash
   cd langchaXXXXXXXXX
   ```

3. **Install the required dependencies using `pip`:**

   ```bash
   pip install -r requirements.txt
   ```

   This installs the necessary packages, including Langchain and its dependencies.

4. **Create a `.env` file in the project directory and set the required environment variables, such as the OpenAI API key:**

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Run the script:**

   ```bash
   python langchain_sql_agent.py
   ```

2. **Enter a question when prompted:**

   ```bash
   User: How many customers do we have in the database?
   ```

3. The LLM will based on the question provided, if related to policies on return and refund it provides those informations, for question regarding the data it utilizes Langchain to query the connected SQLite database (Chinook.db) and provide an answer based on the given question.

## Configuration

- **OpenAI API Key:**
  Ensure that you have a valid OpenAI API key and set it in the `.env` file.

- **Database Connection:**
  The script is configured to connect to an SQLite database named `Chinook.db`. Modify the `SQLDatabase.from_uri` line in the script if your database has a different name or location.

## Dependencies

- Langchain
- dotenv
