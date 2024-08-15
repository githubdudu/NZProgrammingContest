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

I wrote a piece of IO.
```python
class IO():
    def getStr():
        return input()
    
    def getInt():
        return int(input())
    
    def getStrList():
        return input().split(' ')

    def getIntList():
        return [int(x) for x in input().split(' ')]
    
io = IO()
```