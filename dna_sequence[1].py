"""
dna_sequence.py
---------------
Defines the DNASequence class representing a biological DNA sequence.
Demonstrates basic Object-Oriented Programming (OOP) concepts:
- class definition
- constructor (__init__)
- instance attributes (self.sequence)
- instance methods (validate, length, count_nucleotides, gc_content, etc.)
- encapsulation of data and related operations
"""

import dna_operations


class DNASequence:
    """
    A class used to represent and analyze a DNA Sequence.
    
    Attributes:
        sequence (str): The uppercase DNA nucleotide sequence.
    """
    
    def __init__(self, sequence=""):
        """
        Constructor to initialize a DNASequence object.
        
        Demonstrates:
        - __init__ constructor
        - default parameter
        - instance attribute assignment (self.sequence)
        """
        self.sequence = sequence.strip().upper() if sequence else ""
        
    def set_sequence(self, new_sequence):
        """
        Updates the stored DNA sequence.
        """
        self.sequence = new_sequence.strip().upper() if new_sequence else ""
        
    def get_sequence(self):
        """
        Returns the stored DNA sequence string.
        """
        return self.sequence
        
    def is_empty(self):
        """
        Checks whether the sequence is empty.
        
        Demonstrates:
        - comparison operator (==)
        - boolean return
        """
        return len(self.sequence) == 0
        
    def validate(self):
        """
        Validates whether all characters in the sequence are valid bases (A, T, G, C).
        
        Returns:
            tuple: (bool is_valid, list invalid_characters)
        """
        return dna_operations.validate_dna(self.sequence)
        
    def length(self):
        """
        Returns the total number of nucleotides in the sequence.
        """
        return dna_operations.calculate_length(self.sequence)
        
    def count_nucleotides(self):
        """
        Returns a dictionary containing counts of A, T, G, and C.
        """
        return dna_operations.count_nucleotides(self.sequence)
        
    def unique_bases(self):
        """
        Returns a set of unique bases present in the sequence.
        """
        return dna_operations.get_unique_bases(self.sequence)
        
    def gc_content(self):
        """
        Calculates and returns the GC content percentage (0.0 - 100.0).
        """
        return dna_operations.calculate_gc_content(self.sequence)
        
    def at_content(self):
        """
        Calculates and returns the AT content percentage (0.0 - 100.0).
        """
        return dna_operations.calculate_at_content(self.sequence)
        
    def complement(self):
        """
        Generates and returns the complementary DNA sequence string.
        """
        return dna_operations.generate_complement(self.sequence)
        
    def reverse_complement(self):
        """
        Generates and returns the reverse complementary DNA sequence string.
        """
        return dna_operations.generate_reverse_complement(self.sequence)
        
    def find_pattern(self, pattern):
        """
        Searches for a sub-pattern in the stored sequence.
        
        Returns:
            tuple: (bool found, int count, list positions)
        """
        clean_pat = pattern.strip().upper() if pattern else ""
        return dna_operations.search_pattern(self.sequence, clean_pat)
        
    def compare(self, other_sequence):
        """
        Compares the current sequence with another DNA sequence string.
        
        Returns:
            dict: Comparison metrics
        """
        clean_other = other_sequence.strip().upper() if other_sequence else ""
        return dna_operations.compare_sequences(self.sequence, clean_other)
        
    def to_array(self):
        """
        Converts the sequence into a standard Python unicode array ('u').
        """
        return dna_operations.create_nucleotide_array(self.sequence)
        
    def get_summary(self):
        """
        Compiles a summary dictionary of all major sequence metrics.
        """
        counts = self.count_nucleotides()
        is_valid, invalid_chars = self.validate()
        return {
            'sequence': self.sequence,
            'length': self.length(),
            'is_valid': is_valid,
            'invalid_chars': invalid_chars,
            'counts': counts,
            'gc_content': self.gc_content(),
            'at_content': self.at_content(),
            'unique_bases': self.unique_bases()
        }
