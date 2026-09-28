"""
utilities.py
------------
Helper functions and educational concept demonstrations for the DNA Sequence Analyzer.
This module covers syllabus topics including:
- Input cleaning and type conversion
- Checking data types with type()
- Identity operators (is, is not)
- Bitwise operators (&, |, ^, ~, <<, >>)
- Operator precedence demonstration
"""

import array


def clean_dna_input(user_input):
    """
    Cleans raw user input by removing leading/trailing whitespace
    and converting all characters to uppercase.
    
    Demonstrates:
    - string methods (.strip(), .upper())
    - basic type handling
    """
    if user_input is None:
        return ""
    # Strip whitespace and convert to uppercase
    cleaned = str(user_input).strip().upper()
    return cleaned


def is_valid_choice(choice_str, min_val, max_val):
    """
    Validates a menu choice string against numeric bounds.
    
    Demonstrates:
    - type conversion (int())
    - comparison operators (>=, <=)
    - logical AND
    - membership operator (in)
    
    Returns:
        tuple: (bool is_valid, int or None parsed_choice)
    """
    cleaned = choice_str.strip()
    
    # Check if the string consists of digits only
    if not cleaned.isdigit():
        return False, None
    
    val = int(cleaned)
    if val >= min_val and val <= max_val:
        return True, val
    else:
        return False, None


def demonstrate_types(sequence_obj):
    """
    Educational demonstration of the type() function and Python data structures.
    Examines each variable and prints its official Python type.
    
    Demonstrates:
    - type() function
    - str, int, float, list, tuple, set, dict, frozenset, array
    """
    print("\n" + "=" * 55)
    print("      PYTHON DATA TYPES DEMONSTRATION: type()")
    print("=" * 55)
    
    seq_str = sequence_obj.get_sequence()
    seq_len = sequence_obj.length()
    counts = sequence_obj.count_nucleotides()
    gc = sequence_obj.gc_content()
    bases_tuple = ('A', 'T', 'G', 'C')
    bases_set = sequence_obj.unique_bases()
    bases_frozenset = frozenset({'A', 'T', 'G', 'C'})
    seq_list = list(seq_str)
    seq_array = sequence_obj.to_array()
    
    items = [
        ("Sequence String", seq_str, type(seq_str)),
        ("Sequence Length", seq_len, type(seq_len)),
        ("GC Content (%)", gc, type(gc)),
        ("Nucleotide Counts", counts, type(counts)),
        ("Standard Bases Tuple", bases_tuple, type(bases_tuple)),
        ("Unique Bases Set", bases_set, type(bases_set)),
        ("Valid Bases FrozenSet", bases_frozenset, type(bases_frozenset)),
        ("Sequence as List", seq_list, type(seq_list)),
        ("Standard Array ('u')", seq_array, type(seq_array)),
        ("DNASequence Object", sequence_obj, type(sequence_obj))
    ]
    
    print(f"{'Variable Description':<25} | {'Value / Preview':<15} | {'type() Result':<25}")
    print("-" * 70)
    for desc, val, t in items:
        val_str = str(val)
        if len(val_str) > 14:
            val_str = val_str[:11] + "..."
        print(f"{desc:<25} | {val_str:<15} | {str(t):<25}")
    print("=" * 55)


def demonstrate_identity_operators(sequence_obj):
    """
    Educational demonstration of identity operators: 'is' and 'is not'.
    Explains that 'is' checks memory identity (same object),
    while '==' checks value equality.
    
    Demonstrates:
    - identity operators (is, is not)
    - checking None with 'is'
    - comparison between object identity and value equality
    """
    print("\n" + "=" * 55)
    print("   IDENTITY OPERATORS DEMONSTRATION: 'is' / 'is not'")
    print("=" * 55)
    print("Note: In Python:")
    print("  - '==' checks if two objects have equal values.")
    print("  - 'is' checks if two variables refer to the exact same object in memory.\n")
    
    # 1. Checking None safely
    test_var = None
    print(f"1. Variable test_var = None")
    print(f"   test_var is None     -> {test_var is None}   (Correct way to check for None)")
    print(f"   test_var is not None -> {test_var is not None}\n")
    
    # 2. Object identity with lists
    list_a = ['A', 'T', 'G', 'C']
    list_b = ['A', 'T', 'G', 'C']
    list_c = list_a  # Same reference
    
    print("2. Comparing two separate lists with identical values:")
    print("   list_a = ['A', 'T', 'G', 'C']")
    print("   list_b = ['A', 'T', 'G', 'C']")
    print("   list_c = list_a")
    print(f"   list_a == list_b     -> {list_a == list_b}  (Values are equal)")
    print(f"   list_a is list_b     -> {list_a is list_b} (Different objects in memory!)")
    print(f"   list_a is list_c     -> {list_a is list_c}  (list_c references list_a)")
    print(f"   list_a is not list_b -> {list_a is not list_b}\n")
    
    # 3. DNASequence instance check
    print("3. Checking Current DNASequence Object:")
    seq_ref = sequence_obj
    print(f"   seq_ref is sequence_obj     -> {seq_ref is sequence_obj}")
    print(f"   sequence_obj is not None    -> {sequence_obj is not None}")
    print("=" * 55)


def demonstrate_bitwise_operators():
    """
    Educational demonstration of Python bitwise operators:
    & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift).
    
    Note: As noted in course guidelines, DNA sequence analysis uses standard
    character logic. This function is an isolated educational demonstration
    to satisfy the Python course curriculum requirement for bitwise operators.
    
    Demonstrates:
    - Bitwise AND (&)
    - Bitwise OR (|)
    - Bitwise XOR (^)
    - Bitwise NOT (~)
    - Bitwise Left Shift (<<)
    - Bitwise Right Shift (>>)
    - Binary formatting with bin()
    """
    print("\n" + "=" * 55)
    print("     BITWISE OPERATORS DEMONSTRATION (&, |, ^, ~, <<, >>)")
    print("=" * 55)
    print("Educational syllabus demo on small integer values (5 and 3):")
    
    a = 5   # Binary: 0101
    b = 3   # Binary: 0011
    
    print(f"Let a = {a} (binary: {bin(a)})")
    print(f"Let b = {b} (binary: {bin(b)})\n")
    
    and_res = a & b
    print(f"1. Bitwise AND  (a & b)  : {a} & {b}  = {and_res:<3} | binary: {bin(and_res):>8}")
    print("   (Bit is 1 only if both bits are 1)")
    
    or_res = a | b
    print(f"2. Bitwise OR   (a | b)  : {a} | {b}  = {or_res:<3} | binary: {bin(or_res):>8}")
    print("   (Bit is 1 if either bit is 1)")
    
    xor_res = a ^ b
    print(f"3. Bitwise XOR  (a ^ b)  : {a} ^ {b}  = {xor_res:<3} | binary: {bin(xor_res):>8}")
    print("   (Bit is 1 if bits are different)")
    
    not_a = ~a
    print(f"4. Bitwise NOT  (~a)     : ~{a}     = {not_a:<3} | binary: {bin(not_a):>8}")
    print("   (Inverts all bits: formula -(x + 1))")
    
    shl = a << 1
    print(f"5. Left Shift   (a << 1) : {a} << 1 = {shl:<3} | binary: {bin(shl):>8}")
    print("   (Shifts bits left by 1, equivalent to multiplying by 2)")
    
    shr = a >> 1
    print(f"6. Right Shift  (a >> 1) : {a} >> 1 = {shr:<3} | binary: {bin(shr):>8}")
    print("   (Shifts bits right by 1, equivalent to integer division by 2)")
    print("=" * 55)


def demonstrate_operator_precedence():
    """
    Educational demonstration of operator precedence and associativity.
    Shows how parentheses alter calculation flow in GC content and arithmetic.
    
    Demonstrates:
    - Precedence: Parentheses () > Exponentiation ** > Multiplication/Division *, / > Addition/Subtraction +, -
    - Associativity: Left-to-right vs Right-to-left
    """
    print("\n" + "=" * 55)
    print("    OPERATOR PRECEDENCE & ASSOCIATIVITY DEMO")
    print("=" * 55)
    print("Rule: () has higher precedence than * and /, which precede + and -.\n")
    
    # Example 1: DNA GC content formula precedence
    g = 3
    c = 2
    length = 10
    
    # Correct with parentheses
    gc_correct = (g + c) / length * 100
    # Incorrect without parentheses: g + (c / length * 100)
    gc_without_parens = g + c / length * 100
    
    print(f"DNA Formula Example: G = {g}, C = {c}, Total Length = {length}")
    print(f"  With Parentheses:    (G + C) / Length * 100 = ({g} + {c}) / {length} * 100 = {gc_correct:.2f}%")
    print(f"  Without Parentheses: G + C / Length * 100   = {g} + ({c} / {length} * 100) = {gc_without_parens:.2f}%")
    print("  Notice how () forces addition before division!\n")
    
    # Example 2: Arithmetic operators
    res1 = 2 + 3 * 4
    res2 = (2 + 3) * 4
    res3 = 2 ** 3 ** 2  # Right-to-left associativity of **: 2 ** (3 ** 2) = 2 ** 9 = 512
    
    print("General Arithmetic Examples:")
    print(f"  2 + 3 * 4     = {res1}    (Multiplication has higher precedence than Addition)")
    print(f"  (2 + 3) * 4   = {res2}    (Parentheses override default precedence)")
    print(f"  2 ** 3 ** 2   = {res3}   (Exponentiation is right-to-left: 2 ** (3 ** 2) = 2 ** 9)")
    print("=" * 55)
