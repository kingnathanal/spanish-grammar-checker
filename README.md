# Spanish Grammar Checker

The SpanishGrammarChecker class is designed to check the grammatical correctness of Spanish sentences. It initializes with various sets of Spanish grammar rules, such as determiners, nouns, adjectives, prepositions, verbs, irregular verbs, and sentence endings, sourced from the lexicon module. 

The check_sentence method validates if a sentence ends with a proper punctuation mark and then parses the sentence to ensure it adheres to Spanish grammar rules. If the sentence is grammatically correct, it returns a success message; otherwise, it returns an error message.

Sample output 

```
Sentence:  Hola, como estas?
(False, 'Sentence must end with a period.')


Sentence:  El gato grande come pescado.
Sentence Breakdown:  ['el', 'gato', 'grande', 'come', 'pescado']
(True, 'The sentence is grammatically correct.')


Sentence:  El niño come una manzana.
Sentence Breakdown:  ['el', 'niño', 'come', 'una', 'manzana']
(True, 'The sentence is grammatically correct.')


Sentence:  La niña corre en el parque.
Sentence Breakdown:  ['la', 'niña', 'corre', 'en', 'el', 'parque']
(True, 'The sentence is grammatically correct.')


Sentence:  El libro es interesante.
Sentence Breakdown:  ['el', 'libro', 'es', 'interesante']
(True, 'The sentence is grammatically correct.')


Sentence:  El habla rápidamente.
Sentence Breakdown:  ['el', 'habla', 'rápidamente']
(True, 'The sentence is grammatically correct.')


Sentence:  La casa es bonita.
Sentence Breakdown:  ['la', 'casa', 'es', 'bonita']
(True, 'The sentence is grammatically correct.')


Sentence:  El perro pequeño corre rápido.
Sentence Breakdown:  ['el', 'perro', 'pequeño', 'corre', 'rápido']
(True, 'The sentence is grammatically correct.')


Sentence:  El árbol grande está en el jardín.
Sentence Breakdown:  ['el', 'árbol', 'grande', 'está', 'en', 'el', 'jardín']
(True, 'The sentence is grammatically correct.')


Sentence:  La escuela sin niños está cerrada.
Sentence Breakdown:  ['la', 'escuela', 'sin', 'niños', 'está', 'cerrada']
(False, 'Verb not found or not conjugated correctly.')
```