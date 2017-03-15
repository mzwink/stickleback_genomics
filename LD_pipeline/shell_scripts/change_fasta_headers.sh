#PBS -S /bin/bash
#PBS -q batch
#PBS -N fasta_header
#PBS -l nodes=1:ppn=1:AMD
#PBS -l walltime=20:00:00
#PBS -l mem=10gb

export chrom="chrXXI chrXX chrXIX chrXVIII chrXVII chrXVI chrXV chrXIV chrXIII chrXII chrXI chrX chrIX chrVIII chrVII chrVI chrV chrIV chrIII chrII chrI"

cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/vcf2fasta/
module load python/3.4.3

for chr in ${chrom}
do
	cd ${chr}/
	files=`ls -m *.fasta | tr -d ','`

	for file in ${files}
	do
		python3 Change_fasta_header.py ${file}
		#mv PS1B.fasta LW_${chr}.fasta
	done
	mv LW_chrI.fasta LW_${chr}.fasta
	cd ..
done
