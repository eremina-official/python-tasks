# Invert dictionary
# Swap keys and values.
# {"a":1,"b":2} → {1:"a",2:"b"}

data = {"a": 1, "b": 2, "c": 3}
result = {}

# 1. for loop, O(n) comprexity
for key, value in data.items():
    result[value] = key

print("result", result)

# 2. dictionary comprehension
result1 = {value: key for key, value in data.items()}
print("result1", result1)
