from flask import Flask, jsonify
import json
import datetime
import os

app = Flask(__name__)

@app.route('/news.all.get')
def get_news_all_articles():
    try:
        with open('news_data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/news.categories.get')
def get_news_categories():
    try:
        time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'title': 'List of Categories',
            'time': time_now_str,
            'categories': [
                {'id': 1, 'name': 'Sports'},
                {'id': 2, 'name': 'Politics'},
                {'id': 3, 'name': 'Education'}
            ]
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return 'Welcome ENSIA Students from Flask!'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
