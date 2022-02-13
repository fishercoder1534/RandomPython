from collections import Counter
from collections import namedtuple
from collections import defaultdict

my_list = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 3, 'a', 'abc', "fish"]
print(Counter(my_list))

sentence = "This is a super cool sentence, how cool is this?"
print(Counter(sentence.split()))

letters = "aaaaaaaabbbbbbbcccccdddddddd"
c = Counter(letters)
print(c.most_common())
print(c.most_common(2))
print(list(c))

d = {'a': 10}
print(d['a'])
# print(d['WRONG_KEY']) # this will throw a key error
d = defaultdict(lambda: 0)
d['correct_key'] = 100
print(d['correct_key'])
print(d['wrong_key']) # this will get the default value instead of throwing a key error


my_tuple = (10,20,30)
print(my_tuple[0])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Sam')
print(type(sammy))
print(sammy)
print(sammy[0])
print(sammy[1])
print(sammy[2])

