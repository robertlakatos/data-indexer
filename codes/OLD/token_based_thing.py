from llama_index.core import Document, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import AutoTokenizer
from tqdm import tqdm

def create_fixed_length_chunks_with_tokenizer(texts, chunk_size=512):
    # Set Hugging Face embedding model for LlamaIndex
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L12-v2")

    # Hugging Face tokenizer setup
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    chunks = []
    for text in tqdm(texts, desc="Creating chunks"):
        tokens = tokenizer.tokenize(text, max_length=1024, truncation=True)  # Tokenize the text using Hugging Face tokenizer
        for i in range(0, len(tokens), chunk_size):
            chunk_tokens = tokens[i:i + chunk_size]
            chunk = tokenizer.convert_tokens_to_string(chunk_tokens)
            chunks.append(Document(text=chunk)) # Store the chunk as a Document
    return chunks