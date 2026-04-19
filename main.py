import re
from collections import OrderedDict

def sozlarini_saralash(matn_fayli):
    with open(matn_fayli, 'r') as f:
        matn = f.read()

    sozlar = re.findall(r'\b\w+\b', matn.lower())
    sozlar = sorted(set(sozlar))

    with open('saralangan_sozlar.txt', 'w') as f:
        for soz in sozlar:
            f.write(soz + '\n')

sozlarini_saralash('matn.txt')
```

Bu kodda, `re.findall` funksiyasi orqali matn faylidan so'zlarni o'qib oladi. `sorted` funksiyasi orqali so'zlarni alfabet bo'yicha tartiblaydi. `set` funksiyasi orqali so'zlarning takrorlanishlarini olib tashlaydi. Natijani yangi faylga yozadi.
