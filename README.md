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

# Normalize Example

```python
from jaziw import normalize

bad_text = """– Há, júwermek qatqır-aw, tursań bolmay ma, 
mollańa keshiktiń ǵoy! – degen anamnıń sesi tatlı uyqımdı bóldi. 

Ol bunday sózdi tek ashıwı kelgende ǵana aytatuǵın edi. 
                Anamnıń ǵarǵısınan beter «molla» degen sózin esitkennen-aq, quyqam juwlap, uyqım shayday ashıldı. Qorqınısh denemdi qaplap turdı. Bunnan 7-8 kún burın pallaqqa asılǵandaǵı tut shıbıqtan tilingen eki ayaǵım sol qálpinde matalıp jatqanday bolıp sezildi. Haqıyqatında da, ayaǵımnıń tilikleri pite qoyǵan joq edi. Aqsap zorǵa júretuǵın edim.
"""

print(normalize(bad_text))

# Result
# – Há, júwermek qatqır-aw, tursań bolmay ma, mollańa keshiktiń ǵoy! – degen anamnıń sesi tatlı uyqımdı bóldi. Ol bunday sózdi tek ashıwı kelgende ǵana aytatuǵın edi. Anamnıń ǵarǵısınan beter «molla» degen sózin esitkennen-aq, quyqam juwlap, uyqım shayday ashıldı. Qorqınısh denemdi qaplap turdı. Bunnan 7-8 kún burın pallaqqa asılǵandaǵı tut shıbıqtan tilingen eki ayaǵım sol qálpinde matalıp jatqanday bolıp sezildi. Haqıyqatında da, ayaǵımnıń tilikleri pite qoyǵan joq edi. Aqsap zorǵa júretuǵın edim.
```

# Recommended
```python
from jaziw import normalize, tokenize, sentenize


filename = "a-shamuratov-lat.txt"
with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    
    normalized_text = normalize(text)
    tokenized_text = tokenize(normalized_text)
    sentenized_text = sentenize(normalized_text)

    with open("normalized-" + filename, "w", encoding="utf-8") as new_file:
        new_file.write(text)
```