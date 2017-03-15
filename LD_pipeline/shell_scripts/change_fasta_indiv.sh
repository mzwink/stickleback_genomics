#PBS -S /bin/bash
#PBS -q batch
#PBS -N fasta_header
#PBS -l nodes=1:ppn=1:AMD
#PBS -l walltime=20:00:00
#PBS -l mem=1gb

export chrom="chrXXI chrXX chrXIX chrXVIII chrXVII chrXVI chrXV chrXIV chrXIII chrXII chrXI chrX chrIX chrVIII chrVII chrVI chrV chrIV chrIII chrII chrI"
export dir=change_fasta_indiv
mkdir ${dir}

for chr in ${chrom}
do
	sub_script=${dir}/${chr}_change_fasta.sh
	touch ${sub_script}
	
	echo -e "#PBS -S /bin/bash\n#PBS -q batch\n#PBS -N ${chr}_fasta_header\n#PBS -l nodes=1:ppn=1:AMD\n#PBS -l mem=5gb\n#PBS -l walltime=96:00:00\n#PBS -m ae\n#PBS -j oe\n" >> ${sub_script}
	echo -e "module load python/3.4.3" >> ${sub_script}

	echo -e "cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/vcf2fasta/${chr}/
	
	python3 Change_fasta_header.py 
