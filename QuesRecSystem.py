import pandas as pd
import numpy as np
import operator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

import pymysql
pymysql.__version__
'0.9.3'


class recommendations:

    def __init__(self):
        self.tfidf = TfidfVectorizer(analyzer='word',ngram_range=(1,2))

    def sql_conn(self):
        # Mysql Server connection
        mysql_conn = pymysql.connect(host='******',
                                    database='*******',
                                    user='*****',
                                    password='*****',)

        return mysql_conn   
       
    def data(self):

        mysql_conn =self.sql_conn()

        df = pd.read_sql_query('''SELECT* FROM low_carb_program_v2.td_questions''', mysql_conn)

        questions = df[['question_id','user_id','question']]

        return questions

    def cosine_score(self,text):  
        """
        calcultes cosine cosine_similarities,
        between the input and the docs history 
        after feature_extraction
        """
        questions = self.data()
        ques_vecs = self.tfidf.fit_transform(questions['question'])
        input_vecs = self.tfidf.transform([text])
        cosine_similarities = linear_kernel(input_vecs,ques_vecs).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-6:-1]
        
        return related_docs_indices

        

    def similar_questions(self, text):

        related_docs_indices = self.cosine_score(text)
        questions = self.data()
        ques = questions.reset_index(drop=True) 
        similar_ques = ques[ques.index.isin(related_docs_indices)]
        sim_ques_ids = list(similar_ques['question_id'])
            
        return {"ques_recs_ids":sim_ques_ids}






