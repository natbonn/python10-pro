"""Ανάληψη από ΑΤΜ."""


EXIT_VALUE = 0
BANKNOTE = 20
INITIAL_BALANCE = 1000


def main() -> None:
    """Εκτελεί αναλήψεις ελέγχοντας πρώτα τα error states."""
    balance = INITIAL_BALANCE

    while True:
        print(f"Υπόλοιπο: {balance}€")
        amount = int(input(f"Εισάγετε το ποσό ανάληψης (0 για έξοδο): "))

        if amount == EXIT_VALUE:
            print("Έξοδος από το πρόγραμμα.")
            break

        if amount > balance:
            print("Σφάλμα: Το ποσό ανάληψης υπερβαίνει το διαθέσιμο υπόλοιπο.")
            continue

        if amount % BANKNOTE != 0:
            print(f"Σφάλμα: Το ποσό ανάληψης πρέπει να είναι πολλαπλάσιο των {BANKNOTE}€.")
            continue

        balance -= amount
        print(f"Ανάληψη {amount}€ επιτυχής. Νέο υπόλοιπο: {balance}€\n")


if __name__ == "__main__":
    main()