

def format_fasta_seq(complete_sequence):

    seq_len = len(complete_sequence)
    num_iter = math.ceil(seq_len/60)

    format_seq = ''
    for i in range(num_iter):

        if i == num_iter-1:
            start = i*60
            format_line = complete_sequence[start:] + "\n"
            format_seq += format_line
        else:
            start = i*60
            end = start + 60
            format_line = complete_sequence[start:end] + "\n"
            format_seq += format_line

    return format_seq
