from reverse_complement import reverse_complement


def test_standard_dna():
    assert reverse_complement("ATGC") == "GCAT"


def test_case_insensitivity():
    assert reverse_complement("atgc") == "gcat"


def test_empty_string():
    assert reverse_complement("") == ""


def test_rna_uracil():
    assert reverse_complement("AUGC") == "GCAU"
