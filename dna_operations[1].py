"""
dna_operations.py
-----------------
Module containing core procedural functions for DNA sequence analysis.
This module uses only standard Python concepts taught in a first-year course:
- frozenset and tuple for valid base constants
- dictionary for counting nucleotides and base-pairing
- list for sequence manipulation
- loops (for, while) and conditionals (if, elif, else)
- standard array module for array representation
"""

import array

# Frozen set representing the immutable set of standard DNA nucleotide bases
# Demonstrates: frozenset
VALID_BASES = frozenset({'A', 'T', 'G', 'C'})

# Tuple representing the fixed order of DNA bases
# Demonstrates: tuple
BASE_TUPLE = ('A', 'T', 'G', 'C')

# Dictionary mapping each DNA base to its complementary base
# Demonstrates: dictionary
COMPLEMENT_MAP = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}


def validate_dna(sequence):
    """
    Validates whether every character in the sequence is a valid DNA nucleotide (A, T, G, C).
    
    Demonstrates:
    - for loop
    - membership operator (in, not in)
    - list collection for invalid characters
    - logical not
    
    Returns:
        tuple: (bool is_valid, list invalid_characters)
    """
    if not sequence:
        return False, []
    
    invalid_chars = []
    
    for base in sequence:
        # Check membership against the valid bases frozenset
        if base not in VALID_BASES:
            if base not in invalid_chars:
                invalid_chars.append(base)
                
    # If invalid_chars is empty, sequence is valid
    is_valid = (len(invalid_chars) == 0)
    return is_valid, invalid_chars


def calculate_length(sequence):
    """
    Calculates the total number of nucleotides in the sequence.
    
    Demonstrates:
    - len() function and simple counting
    """
    return len(sequence)


def count_nucleotides(sequence):
    """
    Counts the occurrences of each nucleotide (A, T, G, C) in the sequence.
    
    Demonstrates:
    - dictionary creation and updating
    - for loop
    - assignment operator (+=)
    
    Returns:
        dict: A dictionary with nucleotide counts {'A': int, 'T': int, 'G': int, 'C': int}
    """
    # Initialize count dictionary using the fixed base tuple
    counts = {}
    for base in BASE_TUPLE:
        counts[base] = 0
        
    for base in sequence:
        if base in counts:
            counts[base] += 1
            
    return counts


def get_unique_bases(sequence):
    """
    Finds the unique set of bases present in the sequence.
    
    Demonstrates:
    - set data structure
    """
    return set(sequence)


def calculate_gc_content(sequence):
    """
    Calculates the GC content percentage of the sequence.
    Formula: GC Content = (G + C) / Total Length * 100
    
    Demonstrates:
    - arithmetic operators (+, /, *)
    - division by zero safety check using comparison operator (==)
    - float return type
    
    Returns:
        float: GC content as a percentage (0.0 to 100.0)
    """
    total_length = len(sequence)
    if total_length == 0:
        return 0.0
    
    counts = count_nucleotides(sequence)
    gc_count = counts['G'] + counts['C']
    gc_percentage = (gc_count / total_length) * 100.0
    return gc_percentage


def calculate_at_content(sequence):
    """
    Calculates the AT content percentage of the sequence.
    Formula: AT Content = (A + T) / Total Length * 100
    
    Demonstrates:
    - arithmetic operators (+, /, *)
    - division by zero safety check
    
    Returns:
        float: AT content as a percentage (0.0 to 100.0)
    """
    total_length = len(sequence)
    if total_length == 0:
        return 0.0
    
    counts = count_nucleotides(sequence)
    at_count = counts['A'] + counts['T']
    at_percentage = (at_count / total_length) * 100.0
    return at_percentage


def generate_complement(sequence):
    """
    Generates the complementary DNA sequence according to standard base-pairing:
    A <-> T and G <-> C
    
    Demonstrates:
    - list manipulation (.append())
    - for loop
    - dictionary lookup
    - string .join()
    
    Returns:
        str: Complementary DNA sequence
    """
    complement_list = []
    
    for base in sequence:
        if base in COMPLEMENT_MAP:
            complement_list.append(COMPLEMENT_MAP[base])
        else:
            # If an unknown base is encountered, keep as is
            complement_list.append(base)
            
    return "".join(complement_list)


def generate_reverse_complement(sequence):
    """
    Generates the reverse complement of the DNA sequence:
    first complements the sequence, then reverses it.
    
    Demonstrates:
    - function reuse
    - string slicing for reversal ([::-1])
    
    Returns:
        str: Reverse complement DNA sequence
    """
    complement_seq = generate_complement(sequence)
    # Reverse string using standard Python step slicing
    reverse_complement_seq = complement_seq[::-1]
    return reverse_complement_seq


def search_pattern(sequence, pattern):
    """
    Searches for a sub-pattern in the DNA sequence.
    Finds whether the pattern exists, the total count, and all starting positions (1-based index).
    
    Demonstrates:
    - comparison operators
    - membership operator (in)
    - for loop with range()
    - string slicing
    - list of integer positions
    
    Returns:
        tuple: (bool found, int count, list positions)
    """
    if not sequence or not pattern:
        return False, 0, []
    
    seq_len = len(sequence)
    pat_len = len(pattern)
    
    if pat_len > seq_len:
        return False, 0, []
    
    positions = []
    
    # Iterate through all possible starting indices
    limit = (seq_len - pat_len) + 1
    for i in range(limit):
        sub_string = sequence[i:i + pat_len]
        if sub_string == pattern:
            # Store 1-based position for user-friendly display
            positions.append(i + 1)
            
    found = (len(positions) > 0)
    count = len(positions)
    return found, count, positions


def compare_sequences(seq1, seq2):
    """
    Compares two DNA sequences.
    Determines if they are equal or different.
    If they are equal in length, calculates identical positions and similarity percentage.
    
    Demonstrates:
    - comparison operators (==, !=, <, >)
    - if, elif, else branching
    - for loop with range()
    - arithmetic operators (+, /, *)
    
    Returns:
        dict: Summary containing comparison results
    """
    result = {
        'equal': (seq1 == seq2),
        'len1': len(seq1),
        'len2': len(seq2),
        'same_length': (len(seq1) == len(seq2)),
        'matching_positions': 0,
        'similarity_percentage': 0.0
    }
    
    if result['same_length'] and result['len1'] > 0:
        matches = 0
        for i in range(result['len1']):
            if seq1[i] == seq2[i]:
                matches += 1
        result['matching_positions'] = matches
        result['similarity_percentage'] = (matches / result['len1']) * 100.0
        
    return result


def create_nucleotide_array(sequence):
    """
    Demonstrates Python arrays using the standard 'array' module.
    Converts the sequence into a standard Python unicode character array ('u').
    
    Demonstrates:
    - standard array module (array.array)
    - type conversion
    
    Returns:
        array.array: A standard Python array of unicode characters
    """
    return array.array('u', sequence)
