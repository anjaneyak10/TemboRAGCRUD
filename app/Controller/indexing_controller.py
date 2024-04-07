from app.Service.IndexingService import IndexingService

# This class is the controller for indexing files.
class IndexingController:
    def __init__(self):
        self.indexingService = IndexingService()

    def indexAllFiles(self,request):
        return self.indexingService.indexAllFiles(request)
