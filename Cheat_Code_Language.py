import random
import string

word = input("Enter your message: ")
st = word.split(' ')

free_list = []

for words in st:
    if len(words) >= 3:
        r1 = ''.join(random.choices(string.ascii_letters, k=4))
        r2 = ''.join(random.choices(string.ascii_letters, k=4))
        new_word = r1 + words[1:] + words[0] + r2
        free_list.append(new_word)
    else:
        free_list.append(words[::-1])

result = ' '.join(free_list)
print(f"\nEncoded message: {result}\n")

random_number = 8721

print(f"Your code is: {random_number}\n")

decode = input("If you want to decode it, enter your code: ")
print()

if int(decode) == random_number:
    final_list = []
    split_words = result.split(' ')
    for words in split_words:
        if len(words) >= 3:
            answer = words[4:-4]
            answer = answer[-1]+answer[:-1]
            final_list.append(answer)
        else:
            final_list.append(words[::-1])

    final_result = ' '.join(final_list)
    print(f"Decoded message: {final_result}")
else:
    print("Invalid code. Cannot decode.")
print()
