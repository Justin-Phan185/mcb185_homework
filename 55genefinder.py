import sys
import mcb185

orf_length = int(sys.argv[2])
orf_count = 0

print("##gff-version 3\n",end = '')  # GFF header

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	orfs = []
	for frame in range(6):
		if frame < 3:
			frame_seq = seq[frame:]
		else:
			frame_seq = mcb185.anti_seq(seq)[frame-3:]
			
		for i in range(0, len(frame_seq)-2,3):
			codon = frame_seq[i:i+3]
			if codon == 'ATG':
				orf = ''
				for j in range(i, len(frame_seq)-2,3):
					codon = frame_seq[j:j+3]
					orf += mcb185.translate(codon)
					if codon in ['TAA', 'TAG', 'TGA']:
						if len(orf) >= orf_length:
							orfs.append((frame + 1, i, j+3)) #store the frame, start pos, end pos
						break
							
	for frame, start, end in orfs: #unpacks tuples in orfs
		if frame <= 3:
			strand = '+'
			start_pos = start + 1  # GFF coordinates are 1-based
			end_pos = end
		else:
			strand = '-'
			start_pos = len(seq) - end + 1  # Convert to original sequence coordinates for reverse strand
			end_pos = len(seq) - start + 1
		print(f"{defline}\tgene_finder\tgene\t{start_pos}\t{end_pos}\t.\t{strand}\t.\tID=gene{start_pos}_{end_pos}\n")
		orf_count += 1 #thanks to chatgpt for the formatting above
	
print('Total ORFs found:',orf_count)