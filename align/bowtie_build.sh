module load bowtie2/latest
cd /lustre1/mz00685/LD_pipeline/
#export ref_file_list=`ls -m *.fa`

bowtie2-build Glazer/Glazer.fa Glazer
