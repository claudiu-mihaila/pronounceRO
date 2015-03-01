# pronounceRO

This script generates the pronunciation of syllabified words in Romanian passed as arguments. Syllables are separated using full stops, e.g., '*carte*' is syllabified as '*car.te*'.
The script cannot currently handle words containing syllables in which the letter *x* is followed by vowels (a, ă, â, e, i, î, o, u).
The output is given using the International Phonetic Alphabet notation, including the stressed syllables if it can be found.
This is a rule based approach, which does not guarantee 100% accuracy due to the etymological complexities of the Romanian language.

## usage
```sh
$ pronounceRO.py <syllabified-word>
```

