import re
import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def count_words(text, positive_words, negative_words):
    words = re.findall(r'\b\w+\b', text)

    positive_count = 0
    negative_count = 0

    for word in words:
        if word.lower() in positive_words:
            positive_count += 1
        elif word.lower() in negative_words:
            negative_count += 1

    return positive_count, negative_count


positive_words = ["amazing", "enjoy", "beautiful"]
negative_words = ["bad", "disappointing", "poor"]

file_path = "travel_blogs.txt"
text = read_file(file_path)

positive_count, negative_count = count_words(text, positive_words, negative_words)


print("Sentiment Analysis Results:")
print(f"Positive words count: {positive_count}")
print(f"Negative words count: {negative_count}")
