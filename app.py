from flask import Flask, render_template, jsonify, request, url_for, abort
import json
import os
import random
from functools import lru_cache

app = Flask(__name__)

# Use LRU cache to avoid loading the JSON file multiple times
@lru_cache(maxsize=1)
def load_duas():
    try:
        with open('data/duas.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.logger.error(f"Error loading duas.json: {e}")
        return []

@app.route('/')
def home():
    duas_data = load_duas()
    categories = set()
    for dua in duas_data:
        for category in dua.get('categories', []):
            categories.add(category)

    categories = sorted(list(categories))

    # Get 3 random duas but ensure they're different each time
    featured_duas = random.sample(duas_data, min(3, len(duas_data)))

    return render_template('home.html',
                          categories=categories,
                          featured_duas=featured_duas)

@app.route('/category/<category_name>')
def category(category_name):
    duas_data = load_duas()
    filtered_duas = [dua for dua in duas_data if category_name in dua.get('categories', [])]

    if not filtered_duas:
        return render_template('category.html',
                              category=category_name,
                              duas=[],
                              empty=True)

    return render_template('category.html',
                          category=category_name,
                          duas=filtered_duas,
                          empty=False)

@app.route('/search')
def search():
    query = request.args.get('q', '').lower().strip()
    duas_data = load_duas()

    if query:
        results = []
        for dua in duas_data:
            if (query in dua.get('title', '').lower() or
                query in dua.get('translation', '').lower() or
                query in dua.get('transliteration', '').lower() or
                any(query in cat.lower() for cat in dua.get('categories', []))):
                results.append(dua)

        return render_template('search_results.html',
                              query=query,
                              results=results,
                              count=len(results))
    else:
        return render_template('search_results.html',
                              query='',
                              results=[],
                              count=0)

@app.route('/duas')
def get_duas():
    category = request.args.get('category', None)
    duas_data = load_duas()

    if category:
        duas_data = [dua for dua in duas_data if category in dua.get('categories', [])]

    return jsonify(duas_data)

@app.route('/all-duas')
def all_duas():
    duas_data = load_duas()
    return render_template('all_duas.html', duas=duas_data, count=len(duas_data))

@app.route('/dua/<int:dua_id>')
def dua_detail(dua_id):
    duas_data = load_duas()
    dua = next((d for d in duas_data if d.get('id') == dua_id), None)

    if dua:
        # Find related duas that share at least one category with the current dua
        related_duas = [d for d in duas_data if d.get('id') != dua_id and
                       any(cat in dua.get('categories', []) for cat in d.get('categories', []))]

        # Sort related duas by number of shared categories for more relevant suggestions
        related_duas.sort(key=lambda d: len(set(d.get('categories', [])).intersection(set(dua.get('categories', [])))), reverse=True)

        related_duas = related_duas[:3]  # Limit to 3 related duas

        return render_template('dua_detail.html', dua=dua, related_duas=related_duas)
    else:
        abort(404)

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error(f"Server error: {e}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)
