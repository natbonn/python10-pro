"""Χρήση του match-choice για την επιλογή μιας ενέργειας με βάση την είσοδο του χρήστη."""

EXIT_CHOICE = "4"

def decide_on_choice(choice: str) -> str:
    """Επιστρέφει το είδος που επιλέχθηκε από το μενού."""
    match choice:
        case "1":
            return "Κατάθεση"
        case "2":
            return "Ανάληψη"
        case "3":
            return "Υπόλοιπο"
        case _:
            return "Μη έγκυρη επιλογή"


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    while True:
        print("Μενού επιλογών:")
        print("1. Κατάθεση")
        print("2. Ανάληψη")
        print("3. Υπόλοιπο")
        print("4. Έξοδος")

        choice = input("Εισάγετε την επιλογή σας (1-4): ")
        if choice == EXIT_CHOICE:
            print("Έξοδος από το πρόγραμμα.")
            break

        result = decide_on_choice(choice)
        print(f"Επιλέξατε: {result}")


if __name__ == "__main__":
    main()