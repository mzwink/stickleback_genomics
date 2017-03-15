#PBS -S /bin/bash
#PBS -q batch
#PBS -N find_confs
#PBS -l nodes=1:ppn=1:mwnode
#PBS -l walltime=8:00:00
#PBS -l mem=10gb

export dir=LW_ldpipe/vcf2fasta/
cd /lustre1/mz00685/LD_pipeline/${dir}

module load ldhelmet/1.7 
module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7

#export chromosomes="chrXXI chrXX chrXIX chrXVIII chrXVII chrXVI chrXV chrXIV chrXIII chrXII chrXI chrX 
#chrIX chrVIII chrVII chrVI chrV chrIV chrIII chrII chrI"
#export populations="Ca_L Lm_M Kob_M Ran_M No_L G2_L"
export populations="LW"
export chromosomes="chrIX"

for pop in ${populations}
do

	for chr in ${chromosomes}
	do
		file=${pop}_${chr}.fasta
		iden=${pop}_${chr}
		ldhelmet find_confs --num_threads 1 -w 50 -o ${iden}.conf ${file}

	done

done
