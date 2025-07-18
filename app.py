from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import sys

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_inventory():
    df = pd.read_csv('https://trevorscholz.dev/nasa9295.csv')
    df.fillna('', inplace=True)
    df['text'] = df[['object','brand','size']].agg(' '.join, axis=1)
    
    embeddings = model.encode(df['text'].tolist(), convert_to_tensor=True)
    df['embedding'] = [e.cpu().numpy() for e in embeddings]

    return df

inventory = load_inventory()

@app.route('/', methods=['GET','POST'])
def index():
    results = []

    if request.method == 'POST':
        query = request.form['query']
        if not query.strip():
            return render_template('index.html', results=[], error="Please enter a search query.")

        query_embedding = model.encode(query, convert_to_tensor=True).cpu().numpy()
        all_embeddings = np.stack(inventory['embedding'].values)

        dot_products = np.dot(all_embeddings, query_embedding)
        norms = np.linalg.norm(all_embeddings, axis=1) * np.linalg.norm(query_embedding)
        scores = dot_products / (norms + 1e-9)

        top_results = scores.argsort()[-5:][::-1]

        for i in top_results:
            item = inventory.iloc[i]
            results.append({
                'name': item['object'],
                'brand': item['brand'],
                'size': item['size'],
                'drybox': item['drybox'],
                'score': round(scores[i], 3)
            })

    return render_template('index.html', results=results)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:]).strip()
        if not query:
            print("Please provide a search query.")
            sys.exit(1)

        query_embedding = model.encode(query, convert_to_tensor=True).cpu().numpy()
        all_embeddings = np.stack(inventory['embedding'].values)

        dot_products = np.dot(all_embeddings, query_embedding)
        norms = np.linalg.norm(all_embeddings, axis=1) * np.linalg.norm(query_embedding)
        scores = dot_products / (norms + 1e-9)

        top_results = scores.argsort()[-5:][::-1]
        print(f"\nTop results for: \"{query}\"\n")

        for i in top_results:
            item = inventory.iloc[i]
            print(f"{item['object']} ({item['brand']}, {item['size']}): drybox={item['drybox']}, score={round(scores[i], 3)}")

    else:
        app.run(debug=True)
