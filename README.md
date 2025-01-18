# NLP_a1_That What I Like
Assignment a1_That What I Like

## Project Overview

This project implements and analyzes various **Word Embedding models** (Word2Vec and GloVe) for Natural Language Processing (NLP) tasks, such as word similarity and word analogies. A web application is developed to search for the top 10 most similar contexts using a trained Skipgram model.

### Preparation and Training

 - Modified the **Word2Vec** implementation (with and without negative sampling) and **GloVe** from the lab lecture.
 - Trained the models using a real-world corpus, specifically **news articles** from the **nltk** dataset.
 - A function was created to allow dynamic modification of the window size during training, with a default window size of 2.


### Model Comparison and Analysis

1. **Training Loss and Time Comparison**:
   - Compared **Skip-gram**, **Skip-gram with Negative Sampling**, and **GloVe** models based on training loss and training time.

2. **Word Analogies**:
   - Evaluated model performance on **Word Analogies** for syntactic and semantic accuracy using the **Word analogies dataset** (i.e., capital-common-countries and past-tense).

3. **Similarity Analysis**:
   - Used the **Similarity Dataset** to calculate the correlation between dot products of the model embeddings and provided similarity metrics.


 - **Skip-gram**: A variant of Word2Vec that tries to predict surrounding context words given a target word.
 - **Skip-gram with Negative Sampling**: An enhanced version of Skip-gram that uses negative sampling for efficient training.
 - **GloVe**: A count-based model for word embeddings that uses global co-occurrence statistics.


#### Table: Training Loss, Time Comparison and Accuracy
| Model                     | Window Size | Training Loss | Training Time | Syntactic Accuracy | Semantic Accuracy |
|---------------------------|-------------|---------------|---------------|--------------------|-------------------|
| Skipgram                  | 2           | 10.03         | 43 sec        | 0                  | 0                 |
| Skipgram (NEG)            | 2           | 12.22         | 44 sec        | 0                  | 0                 |
| GloVe                     | 2           | 22.81         | 22 sec        | 0                  | 0                 |
| GloVe (Gensim Pre-trained)| N/A         | -             | -             | 0.55               | 0.53              |

- **Training Loss**: The loss function value used during training. Lower values indicate better performance.
- **Training Time**: The time it took to train the model on the dataset.
- **Syntactic Accuracy**: Accuracy on tasks involving syntactic relationships (e.g., past-tense analogies).
- **Semantic Accuracy**: Accuracy on tasks involving semantic relationships (e.g., capital-common-countries analogies).


#### Table: Similarity Correlation (MSE - Mean Squared Error)
| Model                     | Skipgram    | Skipgram (NEG) | GloVe        | GloVe (Gensim)     |
|---------------------------|-------------|----------------|--------------|--------------------|
| MSE                       | -0.07       | 0.04           | 0.13         | 0.53               |
- **MSE**: Mean Squared Error between predicted similarity and true similarity.

### Web Application for Search Similar Context

The application allows users to input search queries and retrieves the top 10 most similar contexts from a trained Skipgram model.

#### Features
- **Search Input Box**: Users can enter a search query into an input field.
- **Similarity Search**: The application calculates the **dot product** between the input query and the context embeddings from the trained Skipgram model.
- **Top 10 Similar Contexts**: Displays the 10 most similar words or contexts based on their similarity to the query.

#### How It Works
1. **User Input**: The user enters a query (word) into the search box on the web page.
2. **Embedding Calculation**: The application retrieves the embedding for the query from the Skipgram model.
3. **Dot Product Calculation**: It calculates the dot product between the query vector and the context vectors to measure similarity.
4. **Top 10 Results**: The top 10 most similar words/contexts are displayed on the webpage.
