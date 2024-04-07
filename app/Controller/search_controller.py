from app.Service.SearchService import SearchService

# This class is the controller for searching chat responses.
class SearchController:
    def __init__(self):
        self.searchService = SearchService()

    def search(self,request):
        return self.searchService.get_chat_response(request.json)
