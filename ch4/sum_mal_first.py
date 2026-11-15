"""Υπολογίζει τους n πρώτους αριθμούς και επιστρέφει το άθροισμά τους."""


def sum_first_int(n: int) -> int:
    """Υπολογίζει το άθροισμα των n πρώτων αριθμών."""
    total_sum = 0
    for i in range(1, n + 1):       # range(start, end + 1, step) -> end is exclusive, so we add 1 to include n
        total_sum += i

    # for i in range(n):
    #     total_sum += i + 1

    return total_sum


def multiply_first_ints(n: int) -> int:
    """Υπολογίζει το γινόμενο των n πρώτων αριθμών."""
    product = 1
    for i in range(1, n + 1):
        product *= i

    return product


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    n = 10
    sum_result = sum_first_int(n)
    product_result = multiply_first_ints(n)

    print(f"Το άθροισμα των {n} πρώτων αριθμών είναι: {sum_result}")
    print(f"Το γινόμενο των {n} πρώτων αριθμών είναι: {product_result}")


if __name__ == "__main__":
    main()