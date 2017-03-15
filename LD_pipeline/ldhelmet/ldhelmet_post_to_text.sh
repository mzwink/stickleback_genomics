#PBS -S /bin/bash
#PBS -q batch
#PBS -N post_to_text
#PBS -l nodes=1:ppn=12:mwnode
#PBS -l walltime=8:00:00
#PBS -l mem=10gb

module load boost/1.59.0/gcc447
module load gsl/1.16/gcc/4.4.7
module load ldhelmet/1.7

cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/rjmcmc_output/

export output_files=`ls -m *.output | tr -d ','`

for file in ${output_files}
do
	iden=`basename ${file} .output`
	ldhelmet post_to_text -m -p0.5 -p0.025 -p0.0975 -o ${iden}_recombrates.txt ${file}

done
