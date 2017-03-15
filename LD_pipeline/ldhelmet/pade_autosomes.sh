#PBS -S /bin/bash
#PBS -q batch
#PBS -N pade_auto
#PBS -l nodes=1:ppn=1:AMD
#PBS -l walltime=8:00:00
#PBS -l mem=10gb

export outDir=pade_auto_indiv
mkdir ${outDir}

export autosomes="chrI chrII chrIII chrIV chrV chrVI chrVII chrVIII chrIX chrX chrXI chrXII chrXIII chrXIV chrXV chrXVI chrXVII chrXVIII chrXX chrXXI"

for i in ${autosomes}
do
	sub_script=${outDir}/${i}_pade.sh
	touch ${sub_script}

	echo -e "#PBS -S /bin/bash\n#PBS -q batch\n#PBS -N pade_${i}\n#PBS -l nodes=1:ppn=12:AMD\n#PBS -l walltime=8:00:00\n#PBS -l mem=20gb\n" >> ${sub_script}
	echo -e "module load boost/1.59.0/gcc447" >> ${sub_script}
	echo -e "module load gsl/1.16/gcc/4.4.7" >> ${sub_script}
	echo -e "module load ldhelmet/1.7\n" >> ${sub_script}

	echo -e "cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/conf/" >> ${sub_script}
	export theta=0.0018599402659327958

	export threads=12
	export conf=LW_${i}.conf
	export iden=LW_${i}
	echo -e "ldhelmet pade --num_threads ${threads} -c ${conf} -t ${theta} -x 11 -o ${iden}.pade" >> ${sub_script} 

done
 

