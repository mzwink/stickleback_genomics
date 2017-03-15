## Combine Population Hotspots and fasta headers ##
from Bio import SeqIO
import glob

hotspot_dir="/Volumes/MW_18TB/Alice_Shanfelter/LD_Files/Consensus_Seqs/Conseqs/"

hotspots = glob.glob(hotspot_dir + "*coldspots_con.fa")
#PS_hotspot = glob.glob(hotspot_dir + "PS*hotspots_con.fa")

for fasta_file in hotspots:

    chrom = fasta_file.replace(hotspot_dir, "").replace("_coldspots_con.fa", "")

    output = fasta_file.replace(".fa", "_format.fa")
    output = open(output, "w")
    fasta = SeqIO.parse(open(fasta_file), 'fasta')

    for line in fasta:
        header = str(line.id)
        seq = str(line.seq)

        #seq = format_fasta_seq(seq)

        header += "_" + chrom

        output.write(">" + header + "\n" + seq + "\n")
