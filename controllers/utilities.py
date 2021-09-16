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