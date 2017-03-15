#PBS -S /bin/bash
#PBS -q batch
#PBS -N samtobam
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=20:00:00
#PBS -l mem=10gb

export dir=downsize_trial4
#cd /lustre1/mz00685/downsize_read_cov/${dir}/sam/

export outDir=samtobam_sub/
mkdir ${outDir}

export indiv="LW_10 LW_11 LW_1 LW_12 LW_13 LW_14 LW_15 LW_16 LW_17 LW_18 LW_19 LW_20 LW_2 LW_3 LW_4 LW_5 LW_6 LW_7 LW_8 LW_9"
for i in ${indiv}
do
	sub_script=${outDir}/${i}_sambam_sub.sh
	touch ${sub_script}
	
	echo -e "#PBS -S /bin/bash\n#PBS -j oe\n#PBS -q batch\n#PBS -N ${i}_sam2bam\n#PBS -l nodes=1:ppn=4:AMD\n#PBS -l walltime=48:00:00\n#PBS -l mem=10gb\n">> ${sub_script}
	echo -e "cd /lustre1/mz00685/downsize_read_cov/${dir}/sam/" >> ${sub_script}
	echo -e  "module load samtools/latest\n" >> ${sub_script}

	#echo -e "export cores=4" >> ${sub_script}
	echo -e "export samFile=${i}.sam" >> ${sub_script}

	#echo -e "name=`basename ${samFile} .sam`" >> ${sub_script} 
	echo -e "samtools view -bh -@ 3 ${i}.sam > ${i}.bam" >> ${sub_script}
	echo -e "samtools sort -o ${i}_sort.bam -T samfile_${i}_s -@ 3 ${i}.bam" >> ${sub_script} 
	echo -e "mv ${i}_sort.bam ${i}.bam" >> ${sub_script}
	echo -e	"samtools index -b ${i}.bam" >> ${sub_script}

done
