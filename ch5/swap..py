"""Ανταλλαγή τιμών δύο μεταβλητών."""


# def swap(a: int, b: int) -> None:
#   tmp = a
#   a = b
#   b = tmp


def swap(a: int, b: int) -> tuple[int, int]:
    """Ανταλλάσσει τις τιμές των α και β."""
    return b, a

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    num1 = int(input("Εισάγετε την πρώτη τιμή: "))
    num2 = int(input("Εισάγετε τη δεύτερη τιμή: "))

    # num1, num2 = swap(num1, num2)
    num1, num2 = num2, num1       # tuple unpacking για ανταλλαγή τιμών

    print(f"Μετά την ανταλλαγή: num1 = {num1}, num2 = {num2}")

if __name__ == "__main__":
    main()