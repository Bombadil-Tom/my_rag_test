from transformers import GPT2Tokenizer

# Initialize the tokenizer for GPT-2 (similar to GPT-3)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Your text to be tokenized
file_path = 'data/extracted_text_chapter_1.txt'
file_paths = ['extracted_text_chapter_1.txt', 'extracted_text_chapter_2.txt', 'extracted_text_chapter_3.txt']
text = ""
# Read the text file
for path in file_paths:
    with open(path, 'r', encoding='utf-8') as file:
        tmp_text = file.read()
        text += tmp_text

# Tokenize the text
tokens = tokenizer.tokenize(text)

# Output the tokens
# print(tokens)

# Count the number of tokens
token_count = len(tokens)
print(f"Number of tokens: {token_count}")
cost_per_1000_tokens = 0.002
total_cost = (token_count / 1000) * cost_per_1000_tokens
print(f"Estimated cost for using GPT-3.5-turbo: ${total_cost:.4f}")