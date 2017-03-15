#PBS -S /bin/bash
#PBS -q batch
#PBS -N Ca_L_table
#PBS -l nodes=1:ppn=12:AMD
#PBS -l walltime=8:00:00
#PBS -l mem=10gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/fasta_files/conf_files/
#export conf_files=`ls -m *chrI.conf | tr -d ','`
export theta=0.00228832695469
export pop="Ca_L"
export chr="chrI"
#Theta is different for each population - get average from LDhat and divide by seq length


#iden=`basename ${file} .conf`
ldhelmet table_gen --num_threads 12 --conf_file ${pop}_${chr}.conf -t ${theta} -r 0.0 0.1 10.0 1.0 100.0 --output_file ${pop}_${chr}.lk

 

