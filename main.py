import random
import time
from paragraphs import paragraphs


random_keys = ["1", "2", "3", "4"]
random_para = random.choice(random_keys)
print(paragraphs.get(random_para))
random_sentence = paragraphs.get(random_para)
user_input = input("Copy out the sentence above: ")

count = 0
score = 0
for char in user_input:
    count += 1
    if user_input[count-1].lower() == random_sentence[count-1].lower():
        score += 1

if score == len(random_sentence):
    print("you were successful!")
else:
    print(f"You copied {score} characters correctly. The correct number you should have copied was {len(random_sentence)}")

seconds = 60
while seconds > 0:
    time.sleep(1)
    seconds -= 1
