# Randomly select k-mer motif in each sequence
# Loop picking a random sequence
# Calculate a profile without that motif from that sequence
# Pick a random k-mer in that sequence proportionally to that k-mers probability

# Psuedo code from class
# GibbsSampler(Dna, k, t, N)
# t is the number of sequences
# k is the length of the k-mer
# N is the number of iterations

import random
import numpy as np

Dna = ["ttaccttaac", "gatgtctgtc", "ccggcgttag", "cactaacgag", "cgtcagaggt"]
k = 4
t = 5
N = 50

def create_profile_matrix(motifs):
    profile = {}
    motif_length = len(motifs[0])
    for i in range(motif_length):
        column = [motif[i].upper() for motif in motifs]
        profile[i] = {
            'A': (column.count('A') + 1) / (len(motifs) + 4),
            'C': (column.count('C') + 1) / (len(motifs) + 4),
            'G': (column.count('G') + 1) / (len(motifs) + 4),
            'T': (column.count('T') + 1) / (len(motifs) + 4)
        }
    return profile

def profile_randomly_generated_kmer(dna_string, k, profile):
    probabilities = []
    for i in range(len(dna_string) - k + 1):
        kmer = dna_string[i:i+k].upper()
        probability = 1
        for j, nucleotide in enumerate(kmer):
            probability *= profile[j][nucleotide]
        probabilities.append(probability)

    # Normalize probabilities
    total = sum(probabilities)
    if total == 0:  # Avoid division by zero
        return dna_string[:k]
    normalized_probabilities = [p/total for p in probabilities]

    # Choose a k-mer based on the probabilities
    chosen_index = np.random.choice(len(probabilities), p=normalized_probabilities)
    return dna_string[chosen_index:chosen_index+k]

def GibbsSampler(Dna, k, t, N):
    motifs = []
    # randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    for string in Dna:
        start = random.randint(0, len(string) - k)
        motif = string[start:start + k]
        motifs.append(motif)

    print("Initial motifs:", motifs)

    # for j ← 1 to N
    for j in range(N):
        # i ← Random(t) pick random i row or motif
        i = random.randint(0, t-1)

        # Profile ← profile matrix constructed from all strings in Motifs except for Motif
        profile_motifs = motifs.copy()
        removed_motif = profile_motifs.pop(i)

        print(f"\nIteration {j+1}")
        print(f"Removed motif at index {i}: {removed_motif}")
        print("Remaining motifs:", profile_motifs)

        # Create profile matrix
        profile_matrix = create_profile_matrix(profile_motifs)

        print("Profile matrix:")
        print(profile_matrix)

        # Pick a new motif for the removed sequence
        new_motif = profile_randomly_generated_kmer(Dna[i], k, profile_matrix)

        # Update the motifs list
        motifs[i] = new_motif

        print(f"New motif selected: {new_motif}")
        print("Updated motifs:", motifs)

    return motifs

# Run the Gibbs Sampler
final_motifs = GibbsSampler(Dna, k=4, t=5, N=50)
print("\nFinal motifs:", final_motifs)