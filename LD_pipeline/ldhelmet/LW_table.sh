#PBS -S /bin/bash
#PBS -q batch
#PBS -N LW_table_chrXIX
#PBS -l nodes=1:ppn=24:mwnode
#PBS -l walltime=480:00:00
#PBS -l mem=10gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/conf/

#export theta=0.0018599402659327958
export theta=0.002019060323434503
export chr=chrXIX


ldhelmet table_gen --num_threads 12 -c LW_${chr}.conf -t ${theta} -r 0.0 0.1 10.0 1.0 100.0 -o LW_${chr}.lk
