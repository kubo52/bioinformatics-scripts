def reverse_complement(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    trans_table = str.maketrans("ACGTUacgtu", "TGCAAucaaa")
    return sequence.translate(trans_table)[::-1]


if __name__ == "__main__":
    test_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    print(f"Original: {test_dna[:20]}...")
    print(f"RevComp:  {reverse_complement(test_dna)[:20]}...")
