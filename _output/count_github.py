import pandas as pd

# Files to process
files = ["questions.csv", "question_tags.csv"]

# Keyword to search
keyword = "GitHub"

# Function to count occurrences
def count_lines_with_keyword(file_path, keyword):
    count = 0
    chunk_size = 10**6  # Process large files in chunks
    try:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size, dtype=str, encoding="utf-8", on_bad_lines="skip"):
            count += chunk.astype(str).apply(lambda x: x.str.contains(keyword, case=False, na=False)).sum().sum()
        print(f"Total lines containing '{keyword}' in {file_path}: {count}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Run the count function
for file in files:
    count_lines_with_keyword(file, keyword)

