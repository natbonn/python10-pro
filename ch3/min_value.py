"""Εύρεση της ελάχιστης τιμής μεταξύ 2 αριθμών."""


def min_val(a: int, b: int) -> int:
    """Επιστρέφει την ελάχιστη τιμή μεταξύ δύο αριθμών.

    Args:
        a (int): Ο πρώτος ακέραιος αριθμός.
        b (int): Ο δεύτερος ακέραιος αριθμός.

    Returns:
        int: Η ελάχιστη τιμή μεταξύ των δύο ακέραιων αριθμών.
    """
    if a < b:
        return a
    else:
        return b


def min_val_ternary(a: int, b: int) -> int:
    """Επιστρέφει την ελάχιστη τιμή μεταξύ δύο αριθμών χρησιμοποιώντας τριμερές τελεστή.

    Args:
        a (int): Ο πρώτος ακέραιος αριθμός.
        b (int): Ο δεύτερος ακέραιος αριθμός.

    Returns:
        int: Η ελάχιστη τιμή μεταξύ των δύο ακέραιων αριθμών.
    """
    return a if a < b else b        # conditional expression (ternary operator) in Python


def min_py(a: int, b: int) -> int:
    """Επιστρέφει την ελάχιστη τιμή μεταξύ δύο αριθμών χρησιμοποιώντας τη συνάρτηση min() της Python.

    Args:
        a (int): Ο πρώτος ακέραιος αριθμός.
        b (int): Ο δεύτερος ακέραιος αριθμός.

    Returns:
        int: Η ελάχιστη τιμή μεταξύ των δύο ακέραιων αριθμών.
    """
    return min(a, b)        # built-in function min() in Python