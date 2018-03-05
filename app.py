from flask import Flask
from flask_restplus import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

m_transaction = api.model('Transaction',
                          {
                              'id': fields.Integer(1),
                              'amount': fields.Integer(10),
                              'description': fields.String('STARBUCKS COFFEE'),
                              'date': fields.String("01/01/1990"),
                              'place': fields.String("Paris"),
                              'currency': fields.String("EUR"),
                              'class': fields.Boolean(0),
                          })
transactions = []
first_transaction = {
    'id': 1,
    'amount': 10,
    'description': 'starbucks',
    'date': "01/01/1990",
    'place': "Paris",
    'currency': "EUR",
    'class': 0
}
transactions.append(first_transaction)


@api.route('/transactions')
class Transactions(Resource):
    @api.marshal_with(m_transaction)
    def get(self):
        return transactions


@api.route('/user/<int:userId>/transactions/')
class TransactionsByUser(Resource):
    @api.marshal_with(m_transaction)
    def get(self, userId):
        pass

    @api.expect(m_transaction)
    def post(self, userId):
        if userId:
            another_transaction = api.payload
            transactions.append(another_transaction)
            return {'result': 'Transaction added'}, 201


@api.route('/user/<int:userId>/transactions/new')
class NewTransactionByUser(Resource):
    @api.marshal_with(m_transaction)
    def get(self, userId):
        pass

    @api.expect(m_transaction)
    def post(self, userId):
        pass


if __name__ == '__main__':
    app.run(debug=True)
