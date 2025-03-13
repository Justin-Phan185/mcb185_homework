import sys
import mcb185
#look for M which is 'ATG'
#end is 'TAA', 'TAG', 'TGA'

aa_length = int(sys.argv[2])
protein_count = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	list_seq = list(seq)
	for frame in range(6):
		if frame < 3:
			frame_seq = seq[frame:]
		else:
			frame_seq = mcb185.anti_seq(seq)[frame-3:]
			
		for i in range(0, len(frame_seq)-2,3):
			codon = frame_seq[i:i+3]
			if codon == 'ATG':
				protein = ''
				for j in range(i, len(frame_seq)-2,3):
					codon = frame_seq[j:j+3]
					protein += mcb185.translate(codon)
					if codon in ['TAA', 'TAG', 'TGA']:
						if len(protein) >= aa_length:
							print(f">{defline}-prot-{protein_count}")
							print(protein)
							protein_count += 1
						break

'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    list_seq = list(seq)
    for i in range(len(seq) - 2,3): #-2 makes sure it only prints by triplets
        codon = seq[i:i+3]
        if codon == 'ATG':
            window = seq[i:(i + aa_length * 3)]
            if len(window) == aa_length * 3:
                translated = mcb185.translate(window)
                print(f">{defline}-prot-{protein_count}")
                print(translated)
                protein_count += 1
'''
'''
			window = seq[i:(aa_length*3)]
	translated = mcb185.translate(window)
	print(translated)
'''
'''	
	codon_list = []
	for i in range(len(window)):
		triplet = (window[i:i+3])
		codon_list.append(triplet)
	#print(codon_list)
'''