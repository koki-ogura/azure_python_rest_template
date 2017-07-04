from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def get_route():
    return make_response(jsonify({'message':'hello rest world!'}))

users = []

@app.route('/api', methods=['POST'])
def post_api():
    try:
        command = request.json['command']
        if (command == 'list'):
            return make_response(jsonify({'users': users}))
        elif (command == 'append'):
            name = request.json['name']
            age = request.json['age']
            data = {'name':name, 'age':age}
            users.append(data)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'invalid command'}))
    except:
        return make_response(jsonify({'error': 'invalid params'}))


if __name__ == '__main__':
  app.run()
