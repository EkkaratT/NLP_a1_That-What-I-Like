# NLP_a1_That What I Like
Assignment a1_That What I Like

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

#### Table: Similarity Correlation
| Model                     | Skipgram    | Skipgram (NEG) | GloVe        | GloVe (Gensim)     |
|---------------------------|-------------|----------------|--------------|--------------------|
| MSE                       | -0.07       | 0.04           | 0.13         | 0.53               |
- **MSE**: Mean Squared Error between predicted similarity and true similarity.

### Web Application for Search Similar Context

The application allows users to input search queries and retrieves the top 10 most similar contexts from a trained Skipgram model.

**Features**
- Search Input Box: Users can enter a search query into an input field.
- Similarity Search: Based on the input query, the application calculates the dot product between the query and the context embeddings from the Skipgram model.
- Top 10 Similar Contexts: The application retrieves and displays the top 10 most similar contexts based on the trained word embeddings.
