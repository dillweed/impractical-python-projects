from collections import defaultdict
test_dict = defaultdict(lambda: [])
key = "aoeu"
test_dict[key].append("test")
test_dict[key].append("test2")
test_dict["single"].append("test3")
print(test_dict.items())
new_dict = {k: v for k, v in test_dict.items() if len(v) > 1}
print(new_dict)
sum = 0
for k, v in test_dict.items():
    sum += len(v)
print(sum)
