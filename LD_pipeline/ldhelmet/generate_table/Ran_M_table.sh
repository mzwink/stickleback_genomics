#PBS -S /bin/bash
#PBS -q batch
#PBS -N Ran_M_table
#PBS -l nodes=1:ppn=12:mwnode
#PBS -l walltime=8:00:00
#PBS -l mem=10gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/fasta_files/conf_files/
export theta=0.0014903844815
export pop="Ran_M"
export chr="chrXIX"
#Theta is different for each population - get average from LDhat and divide by seq length

ldhelmet table_gen --num_threads 12 -c ${pop}_${chr}.conf -t ${theta} -r 0.0 0.1 10.0 1.0 100.0 -o ${pop}_${chr}.lk
ldhelmet pade --num_threads 12 -c ${pop}_${chr}.conf -t ${theta} -x 11 -o ${pop}_${chr}.pade

