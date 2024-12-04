import lexicon as lex

class SpanishGrammarChecker:
    def __init__(self):
        self.determiners = lex.determiners
        self.nouns = lex.nouns
        self.adjectives =  lex.adjectives
        self.prepositions = lex.prepositions
        self.verbs = lex.verbs
        self.irregular_verbs = lex.irregular_verbs
        self.endings = lex.endings

    def check_sentence(self, sentence):
        print("Sentence: ", sentence)
        words = sentence.lower().split()
        if not words[-1].endswith(".") :
            return False, "Sentence must end with a period."

        # Remove the final period for grammar validation
        words[-1] = words[-1][:-1]

        try:
            self.parse_sentence(words)
            return True, "The sentence is grammatically correct."
        except ValueError as e:
            return False, str(e)

    def parse_sentence(self, words):
        print("Sentence Breakdown: ",words)
        words = self.parse_noun_phrase(words)
        if words:
            words = self.parse_verb(words)
        if words:  # Optional complement
            words = self.parse_complement(words)
        if words:
            raise ValueError("Extra words at the end of the sentence.")
        return words

    def parse_noun_phrase(self, words):
        if words[0] in self.determiners: # Optional determiner
            words = words[1:]
            if words[0] in self.nouns: # Noun expected after determiner
                words = words[1:]
                if words and words[0] in self.adjectives:  # Optional adjective
                    words = words[1:]
            else:
                raise ValueError("Noun expected after determiner.")
        elif words[0] in self.nouns:  # Allow standalone noun
            words = words[1:]
        else:
            raise ValueError("Noun phrase not found.")
        return words

    def parse_verb(self, words):
        for verb_forms in self.verbs.values():
            if words[0] in verb_forms: # Check for a verb
                return words[1:]
        raise ValueError("Verb not found or not conjugated correctly.")

    def parse_complement(self, words):
        if words[0] in self.determiners or words[0] in self.prepositions: # Optional determiner or preposition
            return self.parse_noun_phrase(words[1:])
        elif words[0] in self.adjectives: # Optional adjective
            return words[1:]
        elif words[0] in self.nouns: # Allow standalone noun
            return words[1:]
        raise ValueError("Invalid complement structure.")