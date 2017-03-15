#PBS -S /bin/bash
#PBS -j oe
#PBS -q batch
#PBS -N LW_6_sam2bam
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd /lustre1/mz00685/downsize_read_cov/downsize_trial4/sam/
module load samtools/latest

export samFile=LW_6.sam
samtools view -bh -@ 3 LW_6.sam > LW_6.bam
samtools sort -o LW_6_sort.bam -T samfile_LW_6_s -@ 3 LW_6.bam
mv LW_6_sort.bam LW_6.bam
samtools index -b LW_6.bam
