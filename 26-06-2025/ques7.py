def repeated_words(paragraph):
    from collections import Counter
    words = paragraph.lower().split()
    freq = Counter(words)
    return [word for word, count in freq.items() if count > 1]
