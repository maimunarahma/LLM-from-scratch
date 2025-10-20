import re

# 1. Read the text
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("Total number of characters:", len(raw_text))
print(raw_text[:99])  # show first 100 chars

# 2. Preprocess and tokenize
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

print("First 30 tokens:", preprocessed[:30])
print("Total tokens:", len(preprocessed))

# 3. Build vocabulary (unique tokens)
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print("Vocabulary size:", vocab_size)

# 4. Create token <-> id mappings
vocab = {s: i for i, s in enumerate(all_words)}
print("Example vocab pairs:", list(vocab.items())[:10])

# 5. Define tokenizer class
class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed if s in self.str_to_int]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Clean spacing before punctuation
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

# 6. Test tokenizer
tokenizer = SimpleTokenizerV1(vocab)

text = """It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print("Encoded IDs:", ids)

decoded = tokenizer.decode(ids)
print("Decoded text:", decoded)
