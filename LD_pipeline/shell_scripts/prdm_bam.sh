module load samtools/latest
cd /lustre1/mz00685/prdm_variance/sam
export bam_files=`ls -m *.bam | tr -d ','`

for bam in ${bam_files}
do
  name=`basename ${bam} .bam`
#  samtools view -b ${bam} 'groupXX:3319389-3324634' > ${name}_prdm13.bam
  samtools view -b ${bam} 'groupXX:3318389-3325634' > ${name}_prdm13.bam
#  samtools view -b ${bam} 'groupVI:8321996-8323887' > ${name}_prdm8.bam
  samtools view -b ${bam} 'groupVI:8320996-8324887' > ${name}_prdm8.bam

#  samtools view -b ${bam} 'groupI:5465852-5488747' > ${name}_mecom_1.bam
  samtools view -b ${bam} 'groupI:5464852-5489747' > ${name}_mecom.bam
#  samtools view -b ${bam} 'groupI:5472464-5488747' > ${name}_mecom_2.bam

  samtools view -b ${bam} 'groupXVIII:9013111-9022843' > ${name}_prdm1c.bam

#  samtools view -b ${bam} 'groupXVIII:9014111-9021843' > ${name}_prdm1c.bam

  samtools view -b ${bam} 'groupI:15504384-15515157' > ${name}_prdm10.bam

#  samtools view -b ${bam} 'groupI:15505384-15514157' > ${name}_prdm10.bam

  samtools view -b ${bam} 'groupXIV:5445284-5450247' > ${name}_prdm12b.bam
#  samtools view -b ${bam} 'groupXIV:5446284-5449247' > ${name}_prdm12b.bam

  samtools view -b ${bam} 'groupIV:19741262-19747434' > ${name}_prdm4.bam

#  samtools view -b ${bam} 'groupIV:19742262-19746434' > ${name}_prdm4.bam
  samtools view -b ${bam} 'groupV:3410473-3415373' > ${name}_prdm9.bam
#  samtools view -b ${bam} 'groupV:3411473-3414373' > ${name}_prdm9.bam

  samtools view -b ${bam} 'groupXXI:6959347-6964454' > ${name}_prdm14.bam

  samtools view -b ${bam} 'scaffold_27:3386789-3397946' > ${name}_prdm2b.bam
  samtools view -b ${bam} 'scaffold_122:86160-94332' > ${name}_prdm1a.bam

#  samtools view -b ${bam} 'groupXXI:6960347-6963454' > ${name}_prdm14.bam
done


  #samtools view -b ${bam} 'scaffold_27:3387789-3396946' > ${name}_prdm2b.bam
  #samtools view -b ${bam} 'scaffold_122:87160-93332' > ${name}_prdm1a.bam
