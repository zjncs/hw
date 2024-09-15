# Question

sort函数和sorted函数的区别

# Answer

在 Python 中，`sort()` 函数和 `sorted()` 函数都有排序列表的功能，但它们有几个主要区别：

1. **适用对象**：
   - `sort()` 是列表对象的方法，只能用于列表。调用这个函数会在原地对列表进行排序。
   - `sorted()` 是一个内置函数，可以接受任何可迭代对象（如列表、元组、字符串等），并返回一个新的有序列表。

2. **返回值**：
   - `sort()` 方法会修改原始列表，并且没有返回值（返回 `None`）。
   - `sorted()` 函数返回一个新的列表，原始数据保持不变。

3. **使用方式**：
   - `sort()` 的使用方式是：`list.sort()`。
   - `sorted()` 的使用方式是：`sorted(iterable)`，其中 `iterable` 是要排序的对象。

4. **参数**：
   - 两者都可以接受 `key` 和 `reverse` 参数，以定制排序方式，但具体调用方式有差异。
   - `sort()` 方法的调用示例：`list.sort(key=..., reverse=...)`。
   - `sorted()` 函数的调用示例：`sorted(iterable, key=..., reverse=...)`。

### 示例代码：

```python
# 使用 sort() 方法
my_list = [3, 1, 2]
my_list.sort()  # 原地排序
print(my_list)  # 输出: [1, 2, 3]

# 使用 sorted() 函数
my_list = [3, 1, 2]
new_list = sorted(my_list)  # 返回新的已排序列表
print(new_list)  # 输出: [1, 2, 3]
print(my_list)   # 原始列表仍为: [3, 1, 2]
```

希望这个解释有助于你理解这两个函数的区别！