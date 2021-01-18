from flask import Flask
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class SimpleRest(Resource):
    def get(self):
        return {
            u'Description': u'I specialise in functional Python in massively-scalable devops environments.',
            u'Name': u'Tristram Oaten, BSc. MSc.',
            u'Technologies': [
                u'javascript',
                u'python',
                u'linux',
                u'postgres',
                u'scala',
                u'couchdb'
            ],
            u'Twitter': u'@0atman'}


api.add_resource(SimpleRest, '/')

if __name__ == '__main__':
    app.run(debug=True)