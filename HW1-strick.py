codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}


def transcribe_coding_strand(DNA_seq):

    # Define the transcription mapping
    transcription = {'A': 'A', 'T': 'U', 'C': 'C', 'G': 'G'}
    
    # Transcribe each DNA nucleotide to its mRNA counterpart
    mRNA_seq = ''.join(transcription[nucleotide] for nucleotide in DNA_seq)
    
    return mRNA_seq

def translate(mRNA_seq):

    # Initialize the protein sequence
    protein_seq = []
    
    # Process the mRNA sequence in chunks of three nucleotides (codons)
    for i in range(0, len(mRNA_seq) - 2, 3):
        codon = mRNA_seq[i:i+3]
        amino_acid = codon_table.get(codon)
        if amino_acid == 'Stop': # Stop translation if we encounter a stop codon
            break
        protein_seq.append(amino_acid)
    
    return ''.join(protein_seq)


def generate_proteins(DNA_seq):
    
    # Write code to find proteins for all open reading frames
    mRNA_seq = transcribe_coding_strand(DNA_seq)
    proteins = translate(mRNA_seq)

    # Look for start codon
    start_codon = proteins.find('M')
    
    # Return proteins after start codon
    return proteins[start_codon + 1:]


# Test one
print(generate_proteins("ATGATTATGTAATAG"))
# Test two
print(generate_proteins("ATGAAATGCCCGTGCTTACCGGACGATTGAGCAGTGATTGCCAGACGACCTGAATGGGAGTAA"))