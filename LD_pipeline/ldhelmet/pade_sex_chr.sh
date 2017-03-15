#PBS -S /bin/bash
#PBS -q batch
#PBS -N pade_sex_chr
#PBS -l nodes=1:ppn=12:AMD
#PBS -l walltime=8:00:00
#PBS -l mem=10gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/conf/
export sex_chr="chrXIX"
export theta=0.002019060323434503

for chr in ${sex_chr}
do
	conf=LW_${chr}.conf
	iden=LW_${chr}
	ldhelmet pade --num_threads 12 -c ${conf} -t ${theta} -x 11 -o ${iden}.pade 

done
 

