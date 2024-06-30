# Tokens Example

```python
from jaziw import tokenize

text = "Asslawma áleykum! Aqılı pútin, ziyalı qáwim."
tokens = tokenize(text)
print(tokens)

# Result
# [Substring(start=0, stop=8, text='Asslawma'), Substring(start=9, stop=16, text='áleykum'), Substring(start=16, stop=17, text='!'), Substring(start=18, stop=23, text='Aqılı'), Substring(start=24, stop=29, text='pútin'), Substring(start=31, stop=37, text='ziyalı'), Substring(start=38, stop=43, text='qáwim'), Substring(start=43, stop=44, text='.')]
```

# Sentences Example

```python
from jaziw import sentenize

text = "Asslawma áleykum! Aqılı pútin, ziyalı qáwim."
sentences = sentenize(text)
print(sentences)

# Result
# [Substring(start=0, stop=17, text='Asslawma áleykum!'), Substring(start=18, stop=44, text='Aqılı pútin, ziyalı qáwim.')]
```