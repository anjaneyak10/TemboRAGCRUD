# Tembo RAG 

**TemboRAGCrud** is a Python application developed to streamline the process of creating APIs for indexing and searching within the Tembo RAG stack environment.

## Features
- **Indexing:** This feature allows users to specify a file path within their storage accessible to the Python code. The application then indexes data into a PostgreSQL database.
  
- **Natural Language Query:** Users can ask questions in plain English and utilize OpenAI to search the indexed results. The application returns answers in a chat format.
  
- **OpenAI Configuration:** Users have the flexibility to configure OpenAI to either specialize in their documents only or leverage its expertise in a specific field. For instance, if configuring the application for thousands of Python files, users can request OpenAI to become an expert on the Python programming language.



## Tembo Stack Setup

To set up the Tembo stack, follow these steps:

1. Connect to Tembo RAG Stack Postgres using any SQL client. You can set up using the Tembo [cloud service](https://cloud.tembo.io/).
2. Execute the following SQL commands:
    ```sql
    ALTER SYSTEM SET vectorize.openai_key TO '<your_api_key>';
    SELECT pg_reload_conf();
    INSERT INTO vectorize.prompts (prompt_type, sys_prompt, user_prompt) VALUES (
    'tembo_support_task',
    'You are a Postgres expert and are tasked with helping users find answers in Tembo documentation. You should prioritize answering questions using the provided context, but can draw from your expert Postgres experience where documentation is lacking. Avoid statements like "based on the documentation..."',
    'Context information is below.\n---------------------\n{{ context_str }}\n---------------------\nGiven the Tembo documentation information and your expert Postgres knowledge, answer the question.\n Question: {{ query_str }}\nAnswer:');
    ```

    Replace `<your_api_key>` with your actual API key. You should tailor sys_prompt and user_prompt according to your needs.
3. For additional details and configurations, refer to the [Tembo RAG Documentation](https://tembo.io/docs/product/stacks/ai/rag).

## Python Code Download and Installation

1. Clone the repository using:
```bash
git clone https://github.com/anjaneyak10/TemboRAGCrud.git
 ```
2. Change directory to the cloned repository.
3. Install dependencies from `requirements.txt` using pip:
 ```bash
 pip install -r requirements.txt
 ```
4. Configurations:
Make the required changes in the `.env` file, such as adding your database name.

Sample `.env` would look like:
```env
DATABASE_URL= postgresql://postgres:<password>@<yourTemboHost>:5432/postgres
AGENT_NAME=tembo_support
CHAT_MODEL=gpt-3.5-turbo
TASK=tembo_support_task
PROJECT_NAME=tembo_support
```
5. Run the `main.py` file using before running make sure you have the right configurations-
 ```bash
 python app/main.py
 ```

## Usage
For searching, you can use http://localhost:9083/search with the following POST body:
 ```json
{
    "question": "what is tembo stack ?"
}
```
For indexing, you can use http://localhost:9083/indexFiles with the following POST body:
```json

{
    "path": "sample/Path"
}
```
## UI
You can use the UI provided in the [PersonalizedChatBot GitHub Repository](https://github.com/anjaneyak10/PersonalizedChatBot).
