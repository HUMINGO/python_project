#coding=utf-8

from deepdiff import DeepDiff

a = [1, 2, 3, 4]
b = [1, 2, 3, 4, 5]
diff = DeepDiff(a, b, ignore_order=True)
print(diff)