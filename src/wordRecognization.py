import torch 
import nltk
import stanfordnlp
#stanfordnlp.download('en') 
from nltk.tokenize import word_tokenize
from nltk.parse.corenlp import CoreNLPParser
from nltk import parse
from nltk.corpus import treebank
from stat_parser import Parser
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM
encoder = 'what is type of cat'


            
    

class word_recogization():
    def __init__(self, encoder):
        self.encoder = encoder
        self.decoder = {}
        
    def judge_question_token(self, x):
        if 'many' in x or 'number' in x or 'much' in x:
            return 'number of '
        elif 'action' in x or 'movement' in x:
            return 'action of '
        elif 'shape' in x or 'type' in x:
            return 'shape of '
        elif 'location' in x or 'place' in x:
            return 'lcoation of '
            
            
    def Standford(self, encoder):
        nlp = stanfordnlp.Pipeline()
        doc = nlp(encoder)
        #x = doc.sentences[0].print_dependencies()
        lists = []
        result = ''
        for i, sent in enumerate(doc.sentences):
            for word in sent.words:
                print("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
                      word.text, word.lemma, word.pos, word.governor, word.dependency_relation))
                if word.pos == 'NN' and  word.governor!= 0:
                    reuslt = word.text
                    governor = word.governor
                if word.pos == 'JJ':
                    result = word.text + ' ' + reuslt
            for word in sent.words:
                if word.governor < governor:
                    lists.append(word.text)
        return result, lists
        
        
    def forward(self):
        self.decoder['nltk'] = {}
        words_tok = word_tokenize(self.encoder)
        result = self.judge_question_token(words_tok)
        lstm_parse = nltk.pos_tag(words_tok)
        for i in lstm_parse:
            if i[1] == 'NN' or  i[1] == 'JJ':
                parse1_result = i[0]
        self.decoder['nltk']['praser'] = result + parse1_result
        self.decoder['nltk']['confidernt_level'] = 0.5
        self.decoder['statpraser'] = {}
        parser = Parser()
        Parse2 = parser.parse(self.encoder)
        for i in Parse2:
            for j in list(i):
                if 'NN' in str(j):
                   stat_parses = j[0]
        self.decoder['statpraser']['praser'] = result + str(stat_parses)
        self.decoder['statpraser']['confidernt_level'] = 0.7
        self.decoder['CoreNLP_praser'] = {}
        CoreNLP_praser, lists = self.Standford(encoder)
        self.decoder['CoreNLP_praser']['praser'] = result + CoreNLP_praser
        self.decoder['CoreNLP_praser']['confidernt_level'] = self.judge_question_token(lists) + CoreNLP_praser
        self.decoder['CoreNLP_praser']['confidernt_level'] = 0.9
        
       
        
        
   
        

        
        
        
    