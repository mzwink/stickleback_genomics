from Bio import SeqIO

protein_seq = "/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/PRDM9_stickleback/prdm9_stickleback_domain.fasta"
output = open("/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/PRDM9_stickleback/ssxrd_protein_domain.fasta", 'w')
protein_seq = SeqIO.parse(open(protein_seq), 'fasta')

for fasta in protein_seq:
    fasta_id = fasta.id
    sequence = str(fasta.seq)

    domains = sequence[171:202]

    output.write(">"+fasta_id + " histone-lysine N-methyltransferase PRDM9 isoform PRDM9 A [Homo sapiens]"+ "\n" + domains + "\n")
