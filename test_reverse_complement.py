from reverse_complement import reverse_complement


def test_standard_dna():
    assert reverse_complement("ATGC") == "GCAT"


def test_case_insensitivity():
    assert reverse_complement("atgc") == "gcat"


def test_empty_string():
    assert reverse_complement("") == ""


def test_rna_uracil():
    assert reverse_complement("AUGC") == "GCAU"

from fasta_parser import parse_fasta


def test_parse_fasta_multiline():
    raw_fasta = """>seq1 Homo sapiens
    ATGC
    CGTA
    >seq2 Mus musculus
    AAAA
    """
    records = list(parse_fasta(raw_fasta))
    assert len(records) == 2
    assert records[0] == ("seq1 Homo sapiens", "ATGCCGTA")
    assert records[1] == ("Mus musculus", "AAAA")
