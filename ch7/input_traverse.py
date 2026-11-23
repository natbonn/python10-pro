"""Είσοδος str και traverse με for loop"""

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""

    # Είσοδος δεδομένων
    name = input("Εισάγετε το όνομα σας: ")

    # Εκτύπωδη χαρακτήρων με for loop
    print("Οι χαρακτήρες του ονόματος σας είναι: ")
    for char in name:
        print(char, end=" ")    # default end="/n"


if __name__ == "__main__":
    main()