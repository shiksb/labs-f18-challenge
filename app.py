from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/pokemon/<query>')
def main(query='1'):
    q = requests.request('GET', 'https://www.pokeapi.co/api/v2/pokemon/' + query).json()
    is_query = query.isdigit()
    id = q.get('id')
    name = q.get('name')
    return render_template('index.html', id=id, name=name, id_query=is_query)

if __name__ == '__main__':
    app.run()
