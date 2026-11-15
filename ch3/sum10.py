"""Υπολογισμός του αθροίσματος των n πρώτων αριθμών."""


def sum_first_n(n: int) -> int:
    """Επιστρέφει το άθροισμα των n πρώτων αριθμών.

    Args:
        n (int): Ο αριθμός των πρώτων αριθμών που θα αθροιστούν.

    Returns:
        int: Το άθροισμα των n πρώτων αριθμών.
    """
    total_sum = 0
    i = 1

    while i <= n:
        total_sum += i
        i += 1

    return total_sum
    # return n * (n + 1) // 2 επιστρέφει int ενώ με απλό / επιστρέφει float


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    n = 10

    result = sum_first_n(n)
    print(f"Το άθροισμα των {n} πρώτων αριθμών είναι: {result}")


if __name__ == "__main__":
    main()