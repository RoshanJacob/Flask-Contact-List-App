from flask import request, jsonify, Flask, render_template
import random

app = Flask(__name__)


names = [
    'John',
    'Raj',
    'Marie',
    'Albert',
]
contacts = [
    {
        'id': 1,
        'name': names[random.randint(0, len(names))],
        'contact': 638479347,
    },
    {
        'id': 2,
        'name': names[random.randint(0, 2) + 1],
        'contact': 3207948970,
    }


]


@app.route('/')
def welcome():
    return render_template('hello.html')


@app.route('/update-data', methods=['POST'])
def post_data():
    if not request.json:
        return jsonify({
            'status': 'Error!',
            'message': 'Data not provided!'
        })

    addedContact = {
        'id': contacts[-1]['id'] + 1,
        'name': names[random.randint(0,  3)],
        'contact': request.json.get('contact')
    }

    contacts.append(addedContact)

    return jsonify({
        'status': 'Success!',
        'message': 'Your contact has been appended to the list successfully!'
    })


@app.route('/get-data')
def getData():
    if len(contacts) > 0:
        return jsonify({
            'contacts': contacts
        })
    else:
        return jsonify({
            'message': 'There are no contacts in your list!'
        })


if __name__ == '__main__':
    app.run(debug=True)
