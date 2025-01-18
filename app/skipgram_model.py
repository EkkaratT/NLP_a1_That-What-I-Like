# skipgram_model.py

import torch
import torch.nn as nn

class Skipgram(nn.Module):
    
    def __init__(self, vocab_size, emb_size, word2index):
        super(Skipgram,self).__init__()
        self.embedding_v = nn.Embedding(vocab_size, emb_size)
        self.embedding_u = nn.Embedding(vocab_size, emb_size)
        self.word2index  = word2index
    
    def forward(self, center_words, target_words, all_vocabs):
        center_embeds = self.embedding_v(center_words) # [batch_size, 1, emb_size]
        target_embeds = self.embedding_u(target_words) # [batch_size, 1, emb_size]
        all_embeds    = self.embedding_u(all_vocabs) #   [batch_size, voc_size, emb_size]
        
        scores      = target_embeds.bmm(center_embeds.transpose(1, 2)).squeeze(2)
        #[batch_size, 1, emb_size] @ [batch_size, emb_size, 1] = [batch_size, 1, 1] = [batch_size, 1]

        norm_scores = all_embeds.bmm(center_embeds.transpose(1, 2)).squeeze(2)
        #[batch_size, voc_size, emb_size] @ [batch_size, emb_size, 1] = [batch_size, voc_size, 1] = [batch_size, voc_size]

        nll = -torch.mean(torch.log(torch.exp(scores)/torch.sum(torch.exp(norm_scores), 1).unsqueeze(1))) # log-softmax
        # scalar (loss must be scalar)    
            
        return nll # negative log likelihood
    
    def get_embed(self, word):
        word2index = self.word2index
        
        try:
            index = word2index[word]
        except:
            index = word2index['<UNK>']
            
        word = torch.LongTensor([index])
        
        embed_c = self.embedding_v(word)
        embed_o = self.embedding_u(word)
        embed   = (embed_c + embed_o) / 2
        
        return embed[0][0].item(), embed[0][1].item()
        
