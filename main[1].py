"""
main.py
-------
Main entry point for the DNA Sequence Analyzer.
A command-line Python application designed for a first-year Python course in Bioengineering.

Author: First-Year Student
Course: Introduction to Python Programming
Module: main.py
"""

import sys
from dna_sequence import DNASequence
import utilities
import dna_operations


def print_menu(current_sequence):
    """
    Displays the interactive command-line menu.
    """
    print("\n" + "=" * 48)
    print("           DNA SEQUENCE ANALYZER")
    print("=" * 48)
    
    if current_sequence:
        preview = current_sequence if len(current_sequence) <= 30 else current_sequence[:27] + "..."
        print(f" Current Sequence: {preview} (Length: {len(current_sequence)})")
    else:
        print(" Current Sequence: [None Loaded]")
    print("-" * 48)
    print("  1. Enter / Change DNA Sequence")
    print("  2. Validate DNA Sequence")
    print("  3. Display Sequence Length")
    print("  4. Count Nucleotides (A, T, G, C)")
    print("  5. Calculate GC Content (%)")
    print("  6. Calculate AT Content (%)")
    print("  7. Find Complementary Sequence")
    print("  8. Find Reverse Complement")
    print("  9. Search for a DNA Pattern")
    print(" 10. Compare Two DNA Sequences")
    print(" 11. Display Full Sequence Information")
    print(" 12. Show Unique Bases (Set & FrozenSet Demo)")
    print(" 13. Show Array Representation (array Module)")
    print(" 14. Course Concept Demos (type, is, bitwise)")
    print(" 15. Exit")
    print("=" * 48)


def menu_enter_sequence(dna_obj):
    """
    Handles user input for entering a new DNA sequence.
    Demonstrates input(), string conversion (.upper()), and object method calls.
    """
    print("\n--- Enter DNA Sequence ---")
    raw_input_seq = input("Enter DNA sequence (e.g. atgcgtaa): ")
    cleaned_seq = utilities.clean_dna_input(raw_input_seq)
    
    if len(cleaned_seq) == 0:
        print("Warning: You entered an empty sequence.")
    else:
        print(f"Sequence stored as: {cleaned_seq}")
        
    dna_obj.set_sequence(cleaned_seq)
    
    # Provide immediate feedback on validity
    is_valid, invalid_chars = dna_obj.validate()
    if is_valid:
        print("Initial Check: Valid DNA sequence (contains only A, T, G, C).")
    else:
        print(f"Initial Check: Contains non-DNA characters: {invalid_chars}")
        print("Note: You can still inspect it or run Option 2 for full validation.")


def menu_validate_sequence(dna_obj):
    """
    Validates the currently loaded DNA sequence.
    """
    print("\n--- Validate DNA Sequence ---")
    seq = dna_obj.get_sequence()
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    print(f"Testing Sequence: {seq}")
    is_valid, invalid_chars = dna_obj.validate()
    
    if is_valid:
        print("Result: Valid DNA sequence.")
        print("Every character belongs to the allowed bases: A, T, G, C.")
    else:
        print("Result: Invalid DNA sequence!")
        print("Only nucleotide bases 'A', 'T', 'G', and 'C' are allowed in DNA.")
        print(f"Invalid character(s) detected: {invalid_chars}")


def menu_display_length(dna_obj):
    """
    Displays the length of the currently loaded sequence.
    """
    print("\n--- Display Sequence Length ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    seq = dna_obj.get_sequence()
    seq_len = dna_obj.length()
    print(f"Sequence: {seq}")
    print(f"Length  : {seq_len} nucleotides")


def menu_count_nucleotides(dna_obj):
    """
    Counts each nucleotide base in the sequence.
    """
    print("\n--- Count Nucleotides ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    counts = dna_obj.count_nucleotides()
    print(f"Sequence: {dna_obj.get_sequence()}")
    print("Nucleotide Frequencies (Dictionary):")
    for base in ('A', 'T', 'G', 'C'):
        print(f"  {base}: {counts[base]}")
    total_valid = counts['A'] + counts['T'] + counts['G'] + counts['C']
    print(f"Total counted standard bases: {total_valid}")


def menu_gc_content(dna_obj):
    """
    Calculates and displays GC content percentage.
    """
    print("\n--- Calculate GC Content ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    gc = dna_obj.gc_content()
    counts = dna_obj.count_nucleotides()
    g_plus_c = counts['G'] + counts['C']
    total = dna_obj.length()
    
    print(f"Sequence: {dna_obj.get_sequence()}")
    print(f"Formula : (G + C) / Total Length * 100")
    print(f"Values  : ({counts['G']} + {counts['C']}) / {total} * 100")
    print(f"GC Content: {gc:.2f}%")


def menu_at_content(dna_obj):
    """
    Calculates and displays AT content percentage.
    """
    print("\n--- Calculate AT Content ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    at = dna_obj.at_content()
    counts = dna_obj.count_nucleotides()
    a_plus_t = counts['A'] + counts['T']
    total = dna_obj.length()
    
    print(f"Sequence: {dna_obj.get_sequence()}")
    print(f"Formula : (A + T) / Total Length * 100")
    print(f"Values  : ({counts['A']} + {counts['T']}) / {total} * 100")
    print(f"AT Content: {at:.2f}%")


def menu_complement(dna_obj):
    """
    Displays the complementary sequence.
    """
    print("\n--- Complementary DNA Sequence ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    orig = dna_obj.get_sequence()
    comp = dna_obj.complement()
    print("Base-pairing rule: A <-> T, G <-> C")
    print(f"Original  : {orig}")
    print(f"Complement: {comp}")


def menu_reverse_complement(dna_obj):
    """
    Displays the reverse complementary sequence.
    """
    print("\n--- Reverse Complementary DNA Sequence ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    orig = dna_obj.get_sequence()
    comp = dna_obj.complement()
    rev_comp = dna_obj.reverse_complement()
    print(f"Original          : {orig}")
    print(f"Complement        : {comp}")
    print(f"Reverse Complement: {rev_comp}")


def menu_search_pattern(dna_obj):
    """
    Searches for a sub-pattern in the current sequence.
    """
    print("\n--- Search for DNA Pattern ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    raw_pat = input("Enter DNA pattern to search (e.g. ATG): ")
    pattern = utilities.clean_dna_input(raw_pat)
    
    if len(pattern) == 0:
        print("Error: Search pattern cannot be empty.")
        return
        
    found, count, positions = dna_obj.find_pattern(pattern)
    print(f"\nTarget Sequence: {dna_obj.get_sequence()}")
    print(f"Search Pattern : {pattern}")
    
    if found:
        print("Pattern found: Yes")
        print(f"Total occurrences: {count}")
        print(f"1-based starting position(s): {positions}")
    else:
        print("Pattern found: No")
        print("The pattern does not occur in the loaded DNA sequence.")


def menu_compare_sequences(dna_obj):
    """
    Compares two DNA sequences.
    """
    print("\n--- Compare Two DNA Sequences ---")
    current_seq = dna_obj.get_sequence()
    seq1 = ""
    
    if not dna_obj.is_empty():
        print(f"Currently loaded sequence: {current_seq}")
        use_current = input("Use current sequence as Sequence 1? (Y/N): ").strip().upper()
        if use_current == "Y":
            seq1 = current_seq
            
    if not seq1:
        raw1 = input("Enter Sequence 1: ")
        seq1 = utilities.clean_dna_input(raw1)
        
    raw2 = input("Enter Sequence 2: ")
    seq2 = utilities.clean_dna_input(raw2)
    
    if len(seq1) == 0 or len(seq2) == 0:
        print("Error: Both sequences must contain at least one character to compare.")
        return
        
    result = dna_operations.compare_sequences(seq1, seq2)
    
    print("\nComparison Results:")
    print(f"  Sequence 1: {seq1} (Length: {result['len1']})")
    print(f"  Sequence 2: {seq2} (Length: {result['len2']})")
    
    if result['equal']:
        print("  Status: Sequences are EQUAL.")
    else:
        print("  Status: Sequences are DIFFERENT.")
        
    if result['same_length']:
        print(f"  Same Length: Yes ({result['len1']} nucleotides)")
        print(f"  Identical Positions: {result['matching_positions']} / {result['len1']}")
        print(f"  Position Match Rate : {result['similarity_percentage']:.2f}%")
    else:
        print("  Same Length: No (Sequences have different lengths, position-by-position comparison skipped)")


def menu_display_information(dna_obj):
    """
    Displays a comprehensive summary of the current sequence.
    """
    print("\n" + "=" * 48)
    print("          SEQUENCE INFORMATION SUMMARY")
    print("=" * 48)
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    summary = dna_obj.get_summary()
    seq = summary['sequence']
    counts = summary['counts']
    
    print(f"Sequence     : {seq}")
    print(f"Length       : {summary['length']} nucleotides")
    print(f"A Count      : {counts['A']}")
    print(f"T Count      : {counts['T']}")
    print(f"G Count      : {counts['G']}")
    print(f"C Count      : {counts['C']}")
    print(f"GC Content   : {summary['gc_content']:.2f}%")
    print(f"AT Content   : {summary['at_content']:.2f}%")
    print(f"Unique Bases : {summary['unique_bases']}")
    
    if summary['is_valid']:
        print("Validation   : Valid DNA sequence")
    else:
        print(f"Validation   : Invalid (contains: {summary['invalid_chars']})")
        
    print(f"Complement   : {dna_obj.complement()}")
    print(f"Rev. Compl.  : {dna_obj.reverse_complement()}")
    print("=" * 48)


def menu_unique_bases(dna_obj):
    """
    Demonstrates sets and frozensets by displaying unique bases.
    """
    print("\n--- Unique Bases (Set & FrozenSet Demonstration) ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    unique_set = dna_obj.unique_bases()
    standard_frozenset = dna_operations.VALID_BASES
    
    print(f"Current Sequence : {dna_obj.get_sequence()}")
    print(f"Unique Bases Set : {unique_set} (type: {type(unique_set)})")
    print(f"Standard Base Set: {standard_frozenset} (type: {type(standard_frozenset)})")
    print(f"Is subset of valid bases? {unique_set.issubset(standard_frozenset)}")


def menu_array_representation(dna_obj):
    """
    Demonstrates standard array module usage.
    """
    print("\n--- Array Representation (Standard 'array' Module) ---")
    if dna_obj.is_empty():
        print("Error: No DNA sequence loaded. Please choose Option 1 first.")
        return
        
    arr = dna_obj.to_array()
    print(f"Sequence String   : {dna_obj.get_sequence()}")
    print(f"Array Object      : {arr}")
    print(f"Array Typecode    : '{arr.typecode}' (unicode character array)")
    print(f"Array Item Count  : {len(arr)}")
    print(f"First element arr[0]: {arr[0]}")


def menu_concept_demos(dna_obj):
    """
    Runs educational demonstrations for course concepts:
    type(), identity operators, bitwise operators, and operator precedence.
    """
    while True:
        print("\n" + "-" * 48)
        print("       PYTHON COURSE CONCEPTS SUB-MENU")
        print("-" * 48)
        print("  1. Data Types Inspection with type()")
        print("  2. Identity Operators ('is' and 'is not')")
        print("  3. Bitwise Operators Demonstration (&, |, ^, ~, <<, >>)")
        print("  4. Operator Precedence & Associativity")
        print("  5. Return to Main Menu")
        print("-" * 48)
        sub_choice = input("Enter choice (1-5): ").strip()
        
        if sub_choice == "1":
            utilities.demonstrate_types(dna_obj)
        elif sub_choice == "2":
            utilities.demonstrate_identity_operators(dna_obj)
        elif sub_choice == "3":
            utilities.demonstrate_bitwise_operators()
        elif sub_choice == "4":
            utilities.demonstrate_operator_precedence()
        elif sub_choice == "5":
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")


def main():
    """
    Main application loop.
    Demonstrates:
    - while loop
    - if, elif, else branches
    - function calls
    - class instantiation
    """
    print("\n" + "=" * 55)
    print(" Welcome to the DNA Sequence Analyzer (Python Project)")
    print(" Developed for First-Year Bioengineering Python Course")
    print("=" * 55)
    
    # Create the central DNASequence instance
    dna = DNASequence()
    
    # Initial sample sequence or start empty
    running = True
    while running:
        print_menu(dna.get_sequence())
        user_choice_str = input("Enter your choice (1-15): ")
        
        valid_choice, choice = utilities.is_valid_choice(user_choice_str, 1, 15)
        
        if not valid_choice:
            print("\n>> Invalid input! Please enter a valid number between 1 and 15.")
            continue
            
        if choice == 1:
            menu_enter_sequence(dna)
        elif choice == 2:
            menu_validate_sequence(dna)
        elif choice == 3:
            menu_display_length(dna)
        elif choice == 4:
            menu_count_nucleotides(dna)
        elif choice == 5:
            menu_gc_content(dna)
        elif choice == 6:
            menu_at_content(dna)
        elif choice == 7:
            menu_complement(dna)
        elif choice == 8:
            menu_reverse_complement(dna)
        elif choice == 9:
            menu_search_pattern(dna)
        elif choice == 10:
            menu_compare_sequences(dna)
        elif choice == 11:
            menu_display_information(dna)
        elif choice == 12:
            menu_unique_bases(dna)
        elif choice == 13:
            menu_array_representation(dna)
        elif choice == 14:
            menu_concept_demos(dna)
        elif choice == 15:
            print("\nThank you for using the DNA Sequence Analyzer. Goodbye!")
            running = False
            

if __name__ == "__main__":
    main()
