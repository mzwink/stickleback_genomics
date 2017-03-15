#PBS -S /bin/bash
#PBS -q batch
#PBS -N rjmcmc
#PBS -l nodes=1:ppn=24:mwnode
#PBS -l walltime=480:00:00
#PBS -l mem=10gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

export chrom="chrI chrII chrIII chrIV chrV chrVI chrVII chrVIII chrIX chrX chrXI chrXII chrXIII chrXIV chrXV chrXVI chrXVII chrXVIII chrXX chrXXI"
#export populations="Kob_M Lm_M Ran_M Ca_L G2_L No_L"


cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/

export conf=/lustre1/mz00685/LD_pipeline/LW_ldpipe/conf/
export sites=/lustre1/mz00685/LD_pipeline/vcf/rjmcmc_sites/
export pos=/lustre1/mz00685/LD_pipeline/vcf/rjmcmc_pos/
export pade=/lustre1/mz00685/LD_pipeline/fasta_files/pade/
export lk=/lustre1/mz00685/LD_pipeline/fasta_files/lk_tables/
export threads=24
export pop="LW"


for chr in ${chrom}
do
		
	ldhelmet rjmcmc --num_threads ${threads} -w 50 -l ${lk}${pop}_chrI.lk -p ${pade}${pop}_chrI.pade -b 10 --pos_file ${pos}${pop}_jG_${chr}_pos.txt --snps_file ${sites}${pop}_jG_${chr}_sites.txt --burn_in 100000 -n 1000000 -o ${pop}_${chr}.output

done 

