import SpanishGrammarChecker as checker

def main():

    print("Starting grammar check...")

    # Create a SpanishGrammerChecker object
    sp = checker.SpanishGrammarChecker()

    # Check the grammar of a sentence
    test1 = sp.check_sentence("Hola, como estas?") # Hello, how are you?
    print(test1)
    print("\n")

    test2 = sp.check_sentence("El gato grande come pescado.") # The big cat eats fish.
    print(test2)
    print("\n")

    test3 = sp.check_sentence("El niño come una manzana.") # The boy eats an apple.
    print(test3)
    print("\n")

    test4 = sp.check_sentence("La niña corre en el parque.") # The girl runs in the park.
    print(test4)
    print("\n")

    test5 = sp.check_sentence("El libro es interesante.") # The book is interesting.
    print(test5)
    print("\n")

    test6 = sp.check_sentence("El habla rápidamente.") # He speaks quickly.
    print(test6)
    print("\n")

    test7 = sp.check_sentence("La casa es bonita.") # The house is pretty.
    print(test7)
    print("\n")

    test8 = sp.check_sentence("El perro pequeño corre rápido.") # The small dog runs fast.
    print(test8)
    print("\n")

    test9 = sp.check_sentence("El árbol grande está en el jardín.") # The big tree is in the garden.
    print(test9)
    print("\n")

    test10 = sp.check_sentence("La escuela sin niños está cerrada.") # The school without children is closed.
    print(test10)

    test11 = sp.check_sentence("La casa grande.") # The big house.
    print(test11)

main()