import os

from app.Dao.SearchDao import SearchDao

class SearchService:
    def __init__(self):
        self.searchDao = SearchDao()

    # This method validates user input and calls the DAO to get a chat response
    def get_chat_response(self,requestJson):
        if 'question' not in requestJson:
            return {'error': 'No "question" key found in the JSON data'}
        question = requestJson['question']
        query = self.createQueryFromQuestion(question)
        return self.searchDao.execute_query(query)

    # This method creates a query from the question to get chat response
    def createQueryFromQuestion(self,question):
        return "select vectorize.rag( agent_name => '%s', query => '%s',chat_model => '%s',task => '%s')->'chat_response';"\
               %(os.getenv("PROJECT_NAME"),question,os.getenv("CHAT_MODEL"),os.getenv("TASK"))
