# DNA Sequence Analyzer

A simple, educational command-line application for analyzing DNA sequences, built for a first-year undergraduate Python programming course in Bioengineering.

---

## Project Description

The **DNA Sequence Analyzer** is a terminal-based Python application that allows users to enter, validate, and perform essential analyses on DNA sequences consisting of the four nucleotide bases: **Adenine (A)**, **Thymine (T)**, **Guanine (G)**, and **Cytosine (C)**.

This project was built from scratch to demonstrate fundamental Python programming principles taught in a first-year curriculum. It runs entirely inside standard Python in any terminal, requiring **no third-party packages, no external APIs, no databases, and no graphical interfaces**.

---

## Features

1. **Enter DNA Sequence:** Input raw DNA sequences with automatic whitespace removal and lowercase-to-uppercase conversion.
2. **Validate DNA Sequence:** Check whether all characters belong strictly to the allowed nucleotide bases (`A`, `T`, `G`, `C`) and highlight any invalid characters.
3. **Display Sequence Length:** Count the total number of nucleotides in the sequence.
4. **Count Nucleotides:** Calculate individual counts for `A`, `T`, `G`, and `C` using a Python dictionary.
5. **Calculate GC Content (%):** Compute the percentage of Guanine and Cytosine bases with zero-division safeguards for empty inputs.
6. **Calculate AT Content (%):** Compute the percentage of Adenine and Thymine bases.
7. **Find Complementary Sequence:** Generate the base-paired complementary strand using Watson-Crick rules ($A \leftrightarrow T$, $G \leftrightarrow C$).
8. **Find Reverse Complement:** Generate the reverse complementary strand ($5' \rightarrow 3'$ orientation).
9. **Search for a DNA Pattern:** Locate sub-patterns/motifs, reporting occurrence count and 1-based start positions without using regular expressions.
10. **Compare Two DNA Sequences:** Check if two sequences are equal or different, and calculate position-by-position matching percentages for equal-length sequences.
11. **Display Sequence Information:** Show a comprehensive, readable summary of all sequence metrics.
12. **Show Unique Bases:** Demonstrate the Python `set` and `frozenset` data structures.
13. **Array Representation:** Demonstrate Python's built-in `array` module with unicode character arrays (`'u'`).
14. **Course Concept Demonstrations:** A dedicated sub-menu demonstrating syllabus concepts:
    - Data type inspection using `type()`
    - Identity operators (`is` and `is not`)
    - Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) on small integers
    - Operator precedence and associativity

---

## Technologies and Python Concepts Used

This project strictly adheres to the concepts covered in a first-year Python course:

- **Fundamentals:** Variables, User Input (`input()`), Output formatting (`print()`)
- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Assignment Operators:** `=`, `+=`, `-=`
- **Comparison / Relational Operators:** `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical Operators:** `and`, `or`, `not`
- **Membership Operators:** `in`, `not in`
- **Identity Operators:** `is`, `is not` (used safely for object identity and `None` checks, not string comparison)
- **Bitwise Operators:** `&`, `|`, `^`, `~`, `<<`, `>>` (in an educational demonstration function)
- **Built-in Functions:** `type()`, `len()`, `range()`, `int()`, `str()`, `float()`, `bin()`
- **Data Structures:**
  - `list` (for sequence character manipulation and position tracking)
  - `tuple` (for immutable standard base definitions)
  - `set` (for unique base extraction)
  - `dict` (for nucleotide frequencies and complement mappings)
  - `frozenset` (for valid nucleotide base constants)
  - `array.array` (from Python's standard `array` module)
- **Control Flow:** `if`, `elif`, `else`, `for` loops, and `while` loops
- **Functions & Modularity:** User-defined functions, multi-file modular design
- **Object-Oriented Programming (OOP):**
  - Class definition (`class DNASequence`)
  - Constructor (`__init__`)
  - Instance attributes (`self.sequence`)
  - Instance methods (`validate`, `length`, `gc_content`, etc.)

---

## Project Structure

```
dna-sequence-analyzer/
│
├── README.md              # Project documentation and instructions
├── requirements.txt       # Dependency declaration (Standard library only)
├── main.py                # Main executable application and interactive menu
├── dna_sequence.py        # DNASequence class implementation
├── dna_operations.py      # Core procedural functions and algorithms
├── utilities.py           # Input cleaning and course concept demonstrations
└── report/
    └── project_report.md  # Detailed first-year academic project report
```

---

## Requirements

- **Python Version:** Python 3.8 or higher.
- **Third-Party Libraries:** **None.** Uses only the Python Standard Library (`sys`, `array`).

---

## Installation & Setup Instructions

1. Ensure Python 3 is installed on your computer. You can check by opening a terminal and running:
   ```bash
   python --version
   ```
2. Navigate to the project directory:
   ```bash
   cd dna-sequence-analyzer
   ```
3. No virtual environment or pip installation is required because only the standard library is used.

---

## How to Run the Program

Start the interactive terminal application with:

```bash
python main.py
```

You will see the main menu:

```text
================================================
           DNA SEQUENCE ANALYZER
================================================
 Current Sequence: [None Loaded]
------------------------------------------------
  1. Enter / Change DNA Sequence
  2. Validate DNA Sequence
  3. Display Sequence Length
  4. Count Nucleotides (A, T, G, C)
  5. Calculate GC Content (%)
  6. Calculate AT Content (%)
  7. Find Complementary Sequence
  8. Find Reverse Complement
  9. Search for a DNA Pattern
 10. Compare Two DNA Sequences
 11. Display Full Sequence Information
 12. Show Unique Bases (Set & FrozenSet Demo)
 13. Show Array Representation (array Module)
 14. Course Concept Demos (type, is, bitwise)
 15. Exit
================================================
Enter your choice (1-15):
```

---

## Input Format

- DNA sequences should be entered as text (e.g., `atgcgtaa` or `ATGCGTAA`).
- Leading and trailing spaces are automatically trimmed.
- Lowercase letters are automatically converted to uppercase.
- Valid DNA characters are: **`A`**, **`T`**, **`G`**, and **`C`**.

---

## Verification & Testing Examples

### Test 1: Standard Valid Sequence
- **Input:** `ATGC`
- **Output:**
  - Length: `4`
  - Validation: `Valid DNA sequence`
  - Counts: `A: 1`, `T: 1`, `G: 1`, `C: 1`
  - GC Content: `50.00%`
  - AT Content: `50.00%`
  - Complement: `TACG`
  - Reverse Complement: `GCAT`

### Test 2: Sequence with Invalid Characters
- **Input:** `ATGXYZ`
- **Output:**
  - Validation: `Invalid DNA sequence!`
  - Feedback: `Only nucleotide bases 'A', 'T', 'G', and 'C' are allowed in DNA.`
  - Invalid characters detected: `['X', 'Y', 'Z']`

### Test 3: Homopolymeric Sequence
- **Input:** `AAAA`
- **Output:**
  - Counts: `A: 4`, `T: 0`, `G: 0`, `C: 0`
  - GC Content: `0.00%`
  - AT Content: `100.00%`
  - Complement: `TTTT`
  - Reverse Complement: `TTTT`

### Test 4: Pattern Search
- **Target Sequence:** `ATGCGTATG`
- **Pattern:** `ATG`
- **Output:**
  - Pattern found: `Yes`
  - Total occurrences: `2`
  - 1-based starting position(s): `[1, 7]`

### Test 5: Empty Sequence Boundary Handling
- **Input:** `""` (Empty string)
- **Output:** Handled safely with friendly error messages and `0.00%` calculations without program crashes or `ZeroDivisionError`.

---

## Limitations

- **Educational Focus:** This is a course project designed for beginners. It does not perform advanced biological predictions, genomic simulations, or statistical alignments.
- **In-Memory Storage:** DNA sequences are stored in memory while the application runs and are not saved to a persistent database.
- **Single Machine:** Operates purely in local terminals without networking or web services.

---

## Author & Academic Information

- **Student:** First-Year Undergraduate
- **Department:** Bioengineering
- **Course:** Introduction to Python Programming
- **Project Name:** DNA Sequence Analyzer
- **Academic Integrity Statement:** This project was developed from scratch using fundamental programming principles taught in class. No code has been plagiarized or taken from third-party repositories.
