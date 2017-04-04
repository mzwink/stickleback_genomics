# Path to fastq files that need demultiplexed
cd /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/
module load stacks/1.40

# Restriction enzyme (we're using GBS so only have one)
export rEnz=apeKI

# Path to Stacks' `process_radtags` file (this will change depending on system)
#export process_radtags=/usr/local/apps/stacks/latest/bin/process_radtags
# Tab-delimited text file with 3' barcode, 5' barcode reverse complement, and sample name
export barcodes=barcode_stack_format.txt

export runNum="L001 L002 L003 L004"
#export logFile=demultiplex_${runNum}.log

for run in ${runNum}
do
	# Files to demultiplex
	export readOne=`ls -m *${run}*R1_001.fastq.gz | tr -d ','`
	export readTwo=`ls -m *${run}*R2_001.fastq.gz | tr -d ','`

	# Log output
	#export logFile=demultiplex_${run}.log

	# Make "indiv" folder if it doesn't already exist


	# Now run
	process_radtags \
    	-1 ${readOne} \
    	-2 ${readTwo} \
    	-b ${barcodes} \
    	-o ./${run}/ \
    	--inline_inline --disable_rad_check \
    	-e ${rEnz} \
    	-c -q -r -i gzfastq

done
