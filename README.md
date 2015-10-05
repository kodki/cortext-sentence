#cortext-sentence

generates a set of pictures for a sentence.

##usage

```python

import cortext_sentence

cortext_sentence.visualize_single("I drink beer.", filename='beer') 

# Image(src='beer.png')
```

###the shoulder of giants

uses `nltk`, `numpy`, `Pillow`(`PIL`).

depends on `cortext-word` and `cortext-context` for classifying the words 

