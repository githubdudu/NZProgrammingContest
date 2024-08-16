If you read guide.pdf, the start code of python3 is like this.

```python
# python3
x = int(input())
print(x*2)
Page 4

```

This is python 2.
```python
# python2
x = int(raw_input())
print x*2
Page 5

```

We should test our code in this way
```bash
python3 code.py
python code.py
```

Test code with input test case file

```bash
python3 code.py < test.txt
python code.py < test.txt
```

I wrote a piece of IO. It is IO.py file.
```python
class IO():
    def getStr(self):
        return input().strip()
    def getInt(self):
        return int(input())
    def getStrList(self):
        return self.getStr().split(' ')
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    def strTuple(self, tuple):
        return "%s %s" % tuple
    def strList(self, li):
        return " ".join(map(str, li))
io = IO()
```