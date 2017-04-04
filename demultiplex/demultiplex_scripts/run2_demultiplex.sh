# Path to fastq files that need demultiplexed
cd /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/
module load stacks/1.40
# Run number
export runNum=L004

# Restriction enzyme (we're using GBS so only have one)
export rEnz=apeKI

# Path to Stacks' `process_radtags` file (this will change depending on system)
#export process_radtags=/usr/local/apps/stacks/latest/bin/process_radtags
# Tab-delimited text file with 3' barcode, 5' barcode reverse complement, and sample name
export barcodes=barcode_stack_format.txt

# Files to demultiplex
export readOne=GBS-Pool-136653_S1_L004_R1_001.fastq.gz
export readTwo=GBS-Pool-136653_S1_L004_R2_001.fastq.gz

# Log output
export logFile=demultiplex_${runNum}.log

# Make "indiv" folder if it doesn't already exist
if [ ! -d "indiv" ]; then
    mkdir indiv
fi

# Now run
process_radtags \
    -1 ${readOne} \
    -2 ${readTwo} \
    -b ${barcodes} \
    -o ./${runNum}/ \
    --inline_inline --disable_rad_check \
    -e ${rEnz} \
    -c -q -r -i gzfastq

