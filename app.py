
import os
import re
import math
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    """Preprocess the text: lowercase, remove punctuation, and tokenize."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = text.split()
    return tokens

def generate_ngrams(tokens, n=3):
    """Generate n-grams from tokenized text."""
    return [' '.join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]

def calculate_jaccard_similarity(ngrams1, ngrams2):
    """Calculate Jaccard Similarity between two sets of n-grams."""
    set1, set2 = set(ngrams1), set(ngrams2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def calculate_cosine_similarity(doc1, doc2):
    """Calculate cosine similarity between two documents."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([doc1, doc2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

def check_plagiarism(doc1, doc2):
    """Check plagiarism using Jaccard and Cosine similarity."""
    tokens1, tokens2 = preprocess_text(doc1), preprocess_text(doc2)

    # Jaccard Similarity
    ngrams1, ngrams2 = generate_ngrams(tokens1), generate_ngrams(tokens2)
    jaccard = calculate_jaccard_similarity(ngrams1, ngrams2)

    # Cosine Similarity
    cosine = calculate_cosine_similarity(doc1, doc2)

    return {
        "Jaccard Similarity": jaccard,
        "Cosine Similarity": cosine
    }

def compare_documents_in_directory(directory):
    """Compare all documents in a directory and generate a similarity report."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    report = {}

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            try:
                with open(os.path.join(directory, files[i]), 'r', encoding='utf-8', errors='replace') as f1, \
                     open(os.path.join(directory, files[j]), 'r', encoding='utf-8', errors='replace') as f2:
                    doc1, doc2 = f1.read(), f2.read()
                    similarity = check_plagiarism(doc1, doc2)
                    report[f"{files[i]} vs {files[j]}"] = similarity
            except Exception as e:
                print(f"Error processing {files[i]} and {files[j]}: {e}")

    return report

def list_applications():
    """Display real-world applications of the plagiarism detection system."""
    print("\nReal-World Applications:")
    print("1. Educational Institutions:")
    print("   - Analyze academic papers and assignments to ensure originality.")
    print("2. Publishing Houses:")
    print("   - Verify articles, manuscripts, and scripts to avoid copyright issues.")
    print("3. Content Creators:")
    print("   - Check blogs, social media posts, or scripts for plagiarism before publishing.")
    print("4. Legal Sector:")
    print("   - Examine contracts, patents, and legal documents for intellectual property violations.")

def main():
    print("Plagiarism Detection System")
    directory = "C:\\Users\hp\\Desktop\\DSA LAB\\New folder"

    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return

    list_applications()

    report = compare_documents_in_directory(directory)

    print("\nPlagiarism Report:")
    for comparison, similarity in report.items():
        print(f"\n{comparison}")
        print(f"Jaccard Similarity: {similarity['Jaccard Similarity']:.2f}")
        print(f"Cosine Similarity: {similarity['Cosine Similarity']:.2f}")

main()
