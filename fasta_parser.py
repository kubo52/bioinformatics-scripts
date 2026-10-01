from typing import Iterator, Tuple


def parse_fasta(fasta_text: str) -> Iterator[Tuple[str, str]]:
    """Yield (header, sequence) tuples from raw FASTA text."""
    header = ""
    seq_chunks = []

    for line in fasta_text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if header:
                yield header, "".join(seq_chunks)
                seq_chunks = []
            header = line[1:].strip()
        else:
            seq_chunks.append(line.upper())

    if header:
        yield header, "".join(seq_chunks)
