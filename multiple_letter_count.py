def multiple_letter_count(word):
    answer = {}
    for one_letter in word:
        answer[one_letter] = word.count(one_letter)
    return answer
print(multiple_letter_count("football"))  