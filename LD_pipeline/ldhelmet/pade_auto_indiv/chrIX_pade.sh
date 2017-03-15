#PBS -S /bin/bash
#PBS -q batch
#PBS -N pade_chrIX
#PBS -l nodes=1:ppn=24:mwnode
#PBS -l walltime=8:00:00
#PBS -l mem=20gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/conf/
ldhelmet pade --num_threads 24 -c LW_chrIX.conf -t 0.0018599402659327958 -x 11 -o LW_chrIX.pade
