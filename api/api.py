from flask import request
from flask_restful import Resource, abort, reqparse

WISH_LIST = {
    "wish1": {
        "wish": "Buy Macbook Pro",
        "done": False
    },
    "wish2": {
        "wish": "Buy Google Pixel 2",
        "done": False
    }
}

def abort_if_404(id):
    if id not in WISH_LIST:
        abort(404, message="Wish {} tidak ditemukan".format(id))

parser = reqparse.RequestParser()
parser.add_argument('wish')
parser.add_argument('done')

class Wish(Resource):
    def get(self, id):
        abort_if_404(id)
        return WISH_LIST[id]

    def put(self, id):
        abort_if_404(id)
        args = parser.parse_args()
        wish = {
            'wish': args['wish'],
            'done': args['done']
        }
        WISH_LIST[id] = wish
        return {id: WISH_LIST[id]}, 201

    def delete(self, id):
        abort_if_404(id)
        del WISH_LIST[id]
        return '', 204

class WishList(Resource):
    def get(self):
        return WISH_LIST

    def post(self):
        args = parser.parse_args()
        if WISH_LIST:
            id = int(max(WISH_LIST.keys()).lstrip('wish')) + 1
        else:
            id = int(1)
        id = 'wish{}'.format(id)
        WISH_LIST[id] = {
            'wish': args['wish'],
            'done': False
        }
        return {id: WISH_LIST[id]}, 201