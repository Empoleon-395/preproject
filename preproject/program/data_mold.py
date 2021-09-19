from janome.tokenizer import Tokenizer
class data_mold:
    def __init__(self,df):
        self.df = df
        self.t = Tokenizer()
        sentences=list(self.df["rev_text"])
        self.word_list = [self.extract_words(sentence) for sentence in sentences]
        
    def extract_words(self,text):
        self.tokens = self.t.tokenize(text)
        return [token.base_form for token in self.tokens 
            if token.part_of_speech.split(',')[0] in['名詞', '動詞','形容詞']]
    
    def rm_stop_words(self):
        with open("../data/StopWord_word_Japanese.txt",encoding="utf-8") as f:
            stop_words = f.read().splitlines()
        for i,n in enumerate(self.word_list):
            self.word_list[i] = list(filter(lambda x: x not in stop_words, n))
    
    def return_word_list(self):
        return self.word_list