import sys
import re
import collections
import string

# Define a list of common stop words to ignore
STOP_WORDS = {"the", "is", "and", "a", "an", "to", "of", "in", "that", "it", "on", "for", "with", "as", "was", "at", "by", "this", "which", "or", "be", "from", "are", "were", "but", "not", "we", "they", "you", "he", "she", "his", "her", "its", "my", "your", "our", "their", "so", "if", "then"}

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Tokenize words, removing punctuation and converting to lowercase
        words = re.findall(r'\b\w+\b', text.lower())
        filtered_words = [word for word in words if word not in STOP_WORDS]
        total_words = len(words)
        
        # Count word frequencies (excluding stop words)
        word_counts = collections.Counter(filtered_words)
        most_common_words = word_counts.most_common(5)
        
        # Compute average word length
        avg_word_length = sum(len(word) for word in words) / total_words if total_words else 0
        
        # Count sentences (naive approach using '.', '!', and '?')
        sentences = re.split(r'[.!?]', text)
        num_sentences = len([s for s in sentences if s.strip()])
        
        # Display results
        print(f"Total words: {total_words}")
        print("Top 5 most frequent words:")
        for word, count in most_common_words:
            print(f"  {word}: {count}")
        print(f"Average word length: {avg_word_length:.2f}")
        print(f"Number of sentences: {num_sentences}")
    
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py <file_path>")
    else:
        analyze_file(sys.argv[1])
