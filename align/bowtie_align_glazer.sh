cd /lustre1/mz00685/LD_pipeline/

export cores=4
export outDir=bam/
module load bowtie2/latest

export btBuild=/lustre1/mz00685/LD_pipeline/Glazer/Glazer

export read1_list=`ls -m *_R1_* | tr -d ' \n'`
export read2_list=`ls -m *_R2_* | tr -d ' \n'`

bowtie2 -p ${cores} --no-unal -x ${btBuild} \
	-1 ${read1_list} \
	-2 ${read2_list} \
	-S ${outDir}





