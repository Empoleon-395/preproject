from gensim.models import word2vec
import os
class my_word2vec:
    def fit(self,word_list,vector_size=100,min_count=1,workers=0,seed=0):
        os.environ['PYTHONHASHSEED']="0"
        self.model = word2vec.Word2Vec(sentences=word_list,vector_size=100,min_count=1,workers=1,seed=0)

    def similar_words(self,word,n=10):
        self.ret_1 = self.model.wv.most_similar(positive=[word],topn=n) 
        print("=========================================================================\n",word,"に最も近い単語",n,"個")
        for item in self.ret_1:
            print(item[0], item[1])

    def similar_2words(self,word1,word2,n=10):
        self.ret_2 = self.model.wv.most_similar(positive=[word1,word2],topn=n)
        print("=========================================================================\n",word1,"＋",word2,"に最も近い単語",n,"個")
        for item in self.ret_2:
            print(item[0], item[1])