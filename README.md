# NLP_a1_That What I Like
Assignment a1_That What I Like

| Model                     | Window Size | Training Loss | Training Time | Syntactic Accuracy | Semantic Accuracy |
|---------------------------|-------------|---------------|---------------|--------------------|-------------------|
| Skipgram                  | 2           | 10.03         | 43 sec        | 0                  | 0                 |
| Skipgram (NEG)            | 2           | 12.22         | 44 sec        | 0                  | 0                 |
| GloVe                     | 2           | 22.81         | 22 sec        | 0                  | 0                 |
| GloVe (Gensim Pre-trained)| N/A         | -             | -             | 0.55               | 0.53              |


| Model                     | Skipgram    | Skipgram (NEG) | GloVe        | GloVe (Gensim)     |
|---------------------------|-------------|----------------|--------------|--------------------|
| MSE                       | -0.07       | 0.04           | 0.13         | 0.53               |
