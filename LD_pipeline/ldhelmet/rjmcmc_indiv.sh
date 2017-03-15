#PBS -S /bin/bash
#PBS -q batch
#PBS -N rjmcmc
#PBS -l nodes=1:ppn=1:AMD
#PBS -l walltime=480:00:00
#PBS -l mem=10gb

export outDir=rjmcmc_auto_indiv
mkdir ${outDir}

export autosomes="chrI chrII chrIII chrIV chrV chrVI chrVII chrVIII chrIX chrX chrXI chrXII chrXIII chrXIV chrXV chrXVI chrXVII chrXVIII chrXX chrXXI"

for i in ${autosomes}
do
	sub_script=${outDir}/${i}_rjmcmc.sh
	touch ${sub_script}

	echo -e "#PBS -S /bin/bash\n#PBS -q batch\n#PBS -N rjmcmc_${i}\n#PBS -l nodes=1:ppn=12:AMD\n#PBS -l walltime=40:00:00\n#PBS -l mem=20gb\n" >> ${sub_script}

	echo -e "module load boost/1.59.0/gcc447" >> ${sub_script}
	echo -e "module load gsl/1.16/gcc/4.4.7" >> ${sub_script}
	echo -e "module load ldhelmet/1.7\n" >> ${sub_script}

#export chrom="chrI chrII chrIII chrIV chrV chrVI chrVII chrVIII chrIX chrX chrXI chrXII chrXIII chrXIV chrXV chrXVI chrXVII chrXVIII chrXX chrXXI"
#export populations="Kob_M Lm_M Ran_M Ca_L G2_L No_L"


	echo -e "cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/" >> ${sub_script}

	export conf=/lustre1/mz00685/LD_pipeline/LW_ldpipe/conf/LW_${i}.conf
	export sites=/lustre1/mz00685/LD_pipeline/LW_ldpipe/rjmcmc_sites/LW_jG_${i}_sites.txt
	export pos=/lustre1/mz00685/LD_pipeline/LW_ldpipe/rjmcmc_pos/LW_jG_${i}_pos.txt
	export pade=/lustre1/mz00685/LD_pipeline/LW_ldpipe/pade/LW_${i}.pade
	export lk=/lustre1/mz00685/LD_pipeline/LW_ldpipe/lk_tables/LW_chrI.lk
	export threads=12
		
	echo -e "ldhelmet rjmcmc --num_threads ${threads} -w 50 -l ${lk} -p ${pade} -b 10 --pos_file ${pos} --snps_file ${sites} --burn_in 100000 -n 1000000 -o LW_${i}.output" >> ${sub_script}

done
