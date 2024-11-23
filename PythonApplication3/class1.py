from transformers import AutoModel, AutoTokenizer

class my_class(object):
    def download_model(model_name):
    # Load the model and tokenizer from Hugging Face
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

    pass




