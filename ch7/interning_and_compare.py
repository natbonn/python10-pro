"""String interning and comparison examples."""

s1 = "Hello"
s2 = "Hello"
s3 = "Hello World"

are_equal = s1  == s2     # ελέγχει το περιεχόμενο
are_same = s1 is s2       # ελέγχει το reference / True λόγω interning


s1_s2_equal = s1 == s3    # False, διαφορετικό περιεχόμενο
s1_s3_same = s1 is s3     # False, διαφορετικά αντικείμενα στη μνήμη


# case-insensitive comparison
# normalize both strings to the same case (upper to lower) before comparison
s4 = "hello"
are_equal_case_insensitive = s1.upper() == s4.upper()     # True