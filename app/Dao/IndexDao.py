import os

from tembo_py.rag import TemboRAG


class IndexDao:
    # Index all files in the given directory
    def indexAllFiles(self, filePath):
        try:
            url = os.getenv("DATABASE_URL")
            rag = TemboRAG(project_name=os.getenv("PROJECT_NAME"),
                           chat_model="gpt-4",
                           connection_string=url)
            chunks = rag.prepare_from_directory(filePath)
            rag.load_documents(chunks)
        except Exception as e:
            return str(e)
        return "Indexing Done"
