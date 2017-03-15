#PBS -S /bin/bash
#PBS -q batch
#PBS -N ldhelmet_pad
#PBS -l nodes=1:ppn=12:AMD
#PBS -l walltime=8:00:00
#PBS -l mem=10gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/fasta_files/conf_files/
export conf_files=`ls -m *.conf | tr -d ','`
export Ran_M_theta=
export Kob_M_theta=
export Lm_M_theta=
export Ca_L_theta=
export Ran_M_theta=


for file in ${conf_files}
do
	iden=`basename ${file} .conf`
	ldhelmet pade --num_threads 12 -c ${file} -t 0.00 -x 11 -o ${iden}.pade 

done
 

