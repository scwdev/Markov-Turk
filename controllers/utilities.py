import random
from flask import g
from collections import defaultdict
from models.user import User

def key_check(api_key):
    user = User.query.filter_by(api_key=api_key).first()
    return user

def n_gram_er(training_data, n:int=1, gram:str='word'):
    p_matrix = defaultdict(list)
    for string in training_data:
        gram_list = string
        if gram == 'word':
            gram_list = string.split()
        for i in range(len(gram_list)-n):    
            n_gram = gram_list[i:i+n]
            if gram == 'word':
                n_gram = " ".join(n_gram)
            p_matrix[n_gram].append(gram_list[i+n])
    return p_matrix

def text_generator(p_matrix:dict, gram:str, finished_length:int, first_n_gram:str=None):
    ## check if starting point is assigned
    if first_n_gram in p_matrix.keys():
        chain = first_n_gram
    ## TODO: error catch for 'first_gram' not in matrix keys
    else:
        chain = random.choice(list(p_matrix.keys()))
    ## define initial state
    last_gram = chain
    while len(chain) < finished_length:
        ## define next step from current Markov chain state
        next_gram = random.choice(p_matrix[last_gram])
        ## Add step to output chain (with whitespace depending)
        if gram == "word":
            chain += " " + next_gram
        else:
            chain += next_gram
        ## progress current state
        last_gram = next_gram

    return chain


def mini_sample_serializer(sample):
    return {
        'sample_id': sample.id,
        'sample_title': sample.sample_title
    }

def mini_matrix_serializer(matrix):
    return {
        'matrix_id': matrix.id,
        'matrix_title': matrix.matrix_title
    }

def mini_output_serializer(output):
    return {
        'output_id': output.id,
        'output_title': output.output_title
    }