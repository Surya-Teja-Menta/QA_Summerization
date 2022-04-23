from transformers import pipeline

def get_model():
    return pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')

def get_ans(question, context):
    model = get_model()
    return model(question, context)['answer']
