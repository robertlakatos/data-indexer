from transformers import AutoTokenizer

def create_fixed_length_chunks_with_tokenizer(text, chunk_size=128):
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    chunks = []
    tokens = tokenizer.tokenize(text, max_length=1024, truncation=True)  # Tokenize the text using Hugging Face tokenizer
    for i in range(0, len(tokens), chunk_size):
        chunk_tokens = tokens[i:i + chunk_size]
        chunk = tokenizer.convert_tokens_to_string(chunk_tokens)
        chunks.append(chunk)  # Store the chunk as a Document
    return chunks