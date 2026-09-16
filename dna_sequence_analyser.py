"""
DNA Sequence Analyser
----------------------
Features I need to add:
    - DNA sequence input
    - DNA sequence validation
    - Sequence length calculation
    - Nucleotide frequency analysis
    - GC content calculation (count and percentage)
"""

# Valid DNA bases
VALID_BASES = {"A", "T", "C", "G"}


def get_sequence_input():
    """
    Prompt the user for a DNA sequence and return it in uppercase,
    with any surrounding whitespace removed.
    """
    sequence = input("Enter a DNA sequence: ").strip().upper()
    return sequence


def is_valid_dna(sequence):
    """
    Check whether a sequence contains only valid DNA bases (A, T, C, G).

    Returns True if valid, False otherwise.
    """
    if len(sequence) == 0:
        return False

    for base in sequence:
        if base not in VALID_BASES:
            return False

    return True


def sequence_length(sequence):
    """Return the length of the DNA sequence."""
    return len(sequence)


def nucleotide_frequency(sequence):
    """
    Count how many times each nucleotide (A, T, C, G) appears
    in the sequence. Returns a dictionary, e.g. {"A": 5, "T": 3, "C": 2, "G": 4}.
    """
    frequencies = {"A": 0, "T": 0, "C": 0, "G": 0}

    for base in sequence:
        frequencies[base] += 1

    return frequencies


def gc_content(sequence):
    """
    Calculate the GC content of the sequence.

    Returns a tuple: (gc_count, gc_percentage)
    """
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count / len(sequence)) * 100
    return gc_count, gc_percentage


def print_report(sequence):
    """Print a full analysis report for a given valid DNA sequence."""
    length = sequence_length(sequence)
    frequencies = nucleotide_frequency(sequence)
    gc_count, gc_percentage = gc_content(sequence)

    print("\n----- DNA Sequence Report -----")
    print(f"Sequence: {sequence}")
    print(f"Length: {length} bases")

    print("\nNucleotide Frequency:")
    for base, count in frequencies.items():
        print(f"  {base}: {count}")

    print(f"\nGC Content: {gc_count} bases ({gc_percentage:.2f}%)")
    print("--------------------------------\n")


def main():
    """Main program loop."""
    print("=== DNA Sequence Analyser ===")

    sequence = get_sequence_input()

    if not is_valid_dna(sequence):
        print("\nError: Invalid DNA sequence.")
        print("A valid sequence can only contain the letters A, T, C, and G.")
        return

    print_report(sequence)


if __name__ == "__main__":
    main()
