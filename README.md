

# Tembo RAG API Setup Guide

This application is used to create APIs for performing indexing and searching on the Tembo RAG stack.

## Tembo Stack Setup

To set up the Tembo stack, follow these steps:

1. Connect to Tembo RAG Stack Postgres using any sql client
2. Execute the following SQL commands:
    ```sql
    ALTER SYSTEM SET vectorize.openai_key TO '<your_api_key>';
    SELECT pg_reload_conf();
    ```
    Replace `<your_api_key>` with your actual API key.
3. For additional details and configurations, refer to the [Tembo RAG Documentation](https://tembo.io/docs/product/stacks/ai/rag).

## Installation

1. Install dependencies from `requirements.txt` using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Make the required changes in the `.env` file, such as adding your database name.

## UI

You can use the UI provided in the [PersonalizedChatBot GitHub Repository](https://github.com/anjaneyak10/PersonalizedChatBot/tree/main).
