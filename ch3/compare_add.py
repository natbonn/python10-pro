"""Αλυσιδωτές συγκρίσεις"""


MIN_GRADE = 50
MAX_GRADE = 100


def is_passing(grade: int) -> bool:
    """Επιστρέφει True αν η βαθμολογία βρίκσεται μεταξύ 50 και 100, διαφορετικά False"""
    return MIN_GRADE <= grade <= MAX_GRADE   # grade >= MIN_GRADE and grade <= MAX_GRADE


def main() -> None:
    """Διαβάζει μια βαθμολογία από τον χρήστη και ελέγχει αν είναι επιτυχής."""
    for grade in (80, 90, 40, 30):
        is_grade_passing = is_passing(grade)
        print(f"Η βαθμολογία {grade} είναι επιτυχής: {is_grade_passing}")


    print()
    if __name__ == "__main__":
        main()