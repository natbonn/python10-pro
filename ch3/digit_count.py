"""Υπολογισμός του αριθμού των ψηφίων ενός αριθμού"""


def count_digits(n: int) -> int:
    """Υπολογισμός του αριθμού των ψηφίων ενός αριθμού."""
    tmp = abs(n)
    digits = 0

    while True:
        digits += 1
        tmp //= 10
        if tmp == 0:
            break

    return digits

    # return len(str(abs(n)))


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    n = int(input("Εισάγετε έναν ακέραιο αριθμό: "))

    result = count_digits(n)

    print(f"Ο αριθμός των ψηφίων του {n} είναι: {result}")


if __name__ == "__main__":
    main()