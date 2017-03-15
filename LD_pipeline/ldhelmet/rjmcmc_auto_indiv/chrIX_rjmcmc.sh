#PBS -S /bin/bash
#PBS -q batch
#PBS -N rjmcmc_chrIX
#PBS -l nodes=1:ppn=12:AMD
#PBS -l walltime=40:00:00
#PBS -l mem=20gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/
ldhelmet rjmcmc --num_threads 12 -w 50 -l /lustre1/mz00685/LD_pipeline/LW_ldpipe/lk_tables/LW_chrI.lk -p /lustre1/mz00685/LD_pipeline/LW_ldpipe/pade/LW_chrIX.pade -b 10 --pos_file /lustre1/mz00685/LD_pipeline/LW_ldpipe/rjmcmc_pos/LW_jG_chrIX_pos.txt --snps_file /lustre1/mz00685/LD_pipeline/LW_ldpipe/rjmcmc_sites/LW_jG_chrIX_sites.txt --burn_in 100000 -n 1000000 -o LW_chrIX.output
