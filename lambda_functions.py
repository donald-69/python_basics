from functools import reduce


def add_two_numbers(a,b):
    return a+b


print(add_two_numbers(5,10))

add_two = lambda a,b: a+b

print(add_two(5,6))
"""Calculates sum of two numbers"""
scores = [{"eng":56,"mat":60},
          {"eng":46,"mat":70},
          {"eng":88,"mat":12},
          {"eng":70,"mat":72}]

sorted_by_maths = sorted(scores, key=lambda s: s["mat"])

print(sorted_by_maths)

def get_english_score(score):
    return score["eng"]

sorted_by_english = sorted(scores, key=get_english_score)

print(sorted_by_english)


ages = [55,12,13,70,120,65,84,36,22,11,47,90,40,99]

total_age = reduce(lambda x,y: x+y, ages, 0)
print(total_age)

new_ages = map(lambda x:x+1,ages)
print(list(new_ages))

above_60 = filter(lambda age: age > 60, ages)
print(list(above_60))
