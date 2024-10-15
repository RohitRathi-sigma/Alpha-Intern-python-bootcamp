#Write a Python program that reverses every alternate word in a sentence while keeping the other words in their original order.

def reverse_alternate_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 == 1:
            words[i] = words[i][::-1]

    return ' '.join(words)

input_sentence = "We Are Jaat Brothers"
result = reverse_alternate_words(input_sentence)
print("Original string:", input_sentence)
print("Modified sentence:", result)