from flask import Flask, render_template, request
import torch
import pickle
import numpy as np
from skipgram_model import Skipgram  # Assuming you have this file as your model

app = Flask(__name__)

# Load the model and word2index
model_folder = 'model'
with open(f'{model_folder}/word2index.pkl', 'rb') as f:
    word2index = pickle.load(f)

skipgram_args = pickle.load(open(f"{model_folder}/skipgram.args", 'rb'))
model_skipgram = Skipgram(**skipgram_args)
model_skipgram.load_state_dict(torch.load(f"{model_folder}/skipgram.model"))
model_skipgram.eval()

def get_similarity(query, model_skipgram, word2index):
    # Ensure the query is in word2index, defaulting to <UNK> if not found
    query_index = word2index.get(query, word2index["<UNK>"])
    
    # Access the embedding_v layer and retrieve the query embedding
    query_embedding = model_skipgram.embedding_v.weight[query_index].detach().numpy()

    similarities = {}
    # Loop through all words in the vocabulary and compute similarities
    for word, index in word2index.items():
        word_embedding = model_skipgram.embedding_v.weight[index].detach().numpy()
        similarity = np.dot(query_embedding, word_embedding)
        similarities[word] = similarity

    # Sort words by similarity and get the top 10
    sorted_words = sorted(similarities, key=similarities.get, reverse=True)[:10]
    return sorted_words

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    query = request.form['query'].lower()  # Get the query from the form
    similar_words = get_similarity(query, model_skipgram, word2index)
    return render_template('result.html', query=query, similar_words=similar_words)

if __name__ == '__main__':
    app.run(debug=True)
