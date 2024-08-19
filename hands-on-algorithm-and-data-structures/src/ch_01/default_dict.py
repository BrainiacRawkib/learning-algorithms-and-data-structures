from collections import defaultdict


default_dict_ = defaultdict(int)

words: list[str] = str.split('data python data data structure data python')

for word in words:
    default_dict_[word] += 1

if __name__ == '__main__':
    print(default_dict_)
