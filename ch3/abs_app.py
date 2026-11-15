"""Απόλυτη τιμή ενός αριθμού με conditional expression."""


def abs_value(x: int) -> int:
    """Επιστρέφει την απόλυτη τιμή ενός αριθμού χρησιμοποιώντας conditional expression.

    Args:
        x (int): Ο ακέραιος αριθμός.

    Returns:
        int: Η απόλυτη τιμή του αριθμού.
    """
    return x if x >= 0 else -x


def abs_python(x: int) -> int:
    """Επιστρέφει την απόλυτη τιμή ενός αριθμού χρησιμοποιώντας τη συνάρτηση abs() της Python.

    Args:
        x (int): Ο ακέραιος αριθμός.

    Returns:
        int: Η απόλυτη τιμή του αριθμού.
    """
    return abs(x)        # built-in function abs() in Python


if __name__ == "__main__":
    num = int(input("Εισάγετε έναν ακέραιο αριθμό: "))

    result_conditional = abs_value(num)
    result_builtin = abs_python(num)

    print(f"Η απόλυτη τιμή του {num} (conditional expression) είναι: {result_conditional}")
    print(f"Η απόλυτη τιμή του {num} (built-in function) είναι: {result_builtin}")