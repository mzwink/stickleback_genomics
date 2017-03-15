#PBS -S /bin/bash
#PBS -j oe
#PBS -q batch
#PBS -N LW_13_sam2bam
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd /lustre1/mz00685/downsize_read_cov/downsize_trial4/sam/
module load samtools/latest

export samFile=LW_13.sam
samtools view -bh -@ 3 LW_13.sam > LW_13.bam
samtools sort -o LW_13_sort.bam -T samfile_LW_13_s -@ 3 LW_13.bam
mv LW_13_sort.bam LW_13.bam
samtools index -b LW_13.bam
