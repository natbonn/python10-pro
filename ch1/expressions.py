""""Expressions demonstration"""
from ch1.data_types import result

num1 = 10
num2 = 5

# Πολλαπλή εκχώρηση
a, b = 5, 7
x = y = 0

# Εκτέλεση αριθμητικών εκφράσεων
total = num1 + num2 + 12
mul = total * 5
div = total / 4     # πάντα επιστρέφει float
floor_div = total   # επιστρέφει integer (ακέραιο πηλίκο)
mod = total % 4     # επιστρέφει το υπόλοιπο της διαίρεσης
result = 2 ** 3     # ύψωση σε δύναμη **