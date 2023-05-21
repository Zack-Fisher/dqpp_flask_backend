## flask stands between the client and the other services
import webbrowser

import backends as b
import html_help as h

from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.debug = True

@app.route('/hello', methods=['GET'])
def hello_world():
    print("triggered GET route")
    return 'Hello, World!'

@app.route('/', methods=['GET'])
def combined():
    endpoint1 = b.mk_route(b.LARAVEL, '')
    endpoint2 = b.mk_route(b.RAILS, '')

    # Make the requests
    response1 = h.get_raw_html(endpoint1)
    response2 = h.get_raw_html(endpoint2)

    body1 = h.get_body_html(response1)
    body2 = h.get_body_html(response2)

    # Return the combined result
    return render_template('layered_concat.html', bodies=[body1, body2])

if __name__ == '__main__':
    p = b.get_port(b.FLASK)
    print(f"Running on port {p}")
    app.run(port=p)
