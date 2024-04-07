from flask import Blueprint, request
from app.Controller.indexing_controller import IndexingController
from app.Controller.search_controller import SearchController

indexing_controller = IndexingController()
search_controller = SearchController()

controller = Blueprint('config', __name__)

# Defining the route for indexing files. This route will be used to index all the files in the given path.
@controller.route('/indexFiles', methods=['POST'])
def indexAllFiles():
    return indexing_controller.indexAllFiles(request)

# Defining the route for searching.
# This route will be used to generate answer for the given question.
@controller.route('/search', methods=['POST'])
def search():
    return search_controller.search(request)
