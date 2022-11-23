from collections import defaultdict
test_dict = defaultdict(lambda: [])
key = "aoeu"
test_dict[key].append("test")
test_dict[key].append("test2")
print(test_dict)
