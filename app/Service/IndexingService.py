from flask import jsonify
from app.Dao.IndexDao import IndexDao

class IndexingService:

    def __init__(self):
        self.indexDao = IndexDao()

    # This method validates user input and calls the DAO to index a file
    def indexAllFiles(self, request):
        data= request.json
        # Check if the request has a 'path' key
        if 'path' not in data:
            return jsonify({'error': 'No "path" key found in the JSON data'})
        path = data['path']
        daoResponse = self.indexDao.indexAllFiles(path)
        # Check if the response from the DAO is successful or not
        if daoResponse =="Indexing Done":
            return jsonify({'message': 'Indexing Done'})
        else:
            return jsonify({'error': daoResponse})
