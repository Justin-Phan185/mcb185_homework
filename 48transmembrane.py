import sys
import mcb185

aa = [ "I", "V", "L", "F", "C", "M", "A", "G", "T", "S", "W", "Y", 
    "H", "E", "Q", "D", "N", "K", "R"] #remove P(proline)

hydropathy = [ 4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3,
 -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

def kd(seq):
    total = 0
    for nt in seq:
        if nt in aa:
            total += hydropathy[aa.index(nt)]
    return total / len(seq)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    signal_pep = False
    transmem = False
    N_term = seq[0:30]
    C_term = seq[30:]
    for i in range(0, len(N_term)-8+1):
        if kd(N_term[i:i+8]) >= 2.5:
            signal_pep = True
    for i in range(0, len(C_term)-11+1):
        if kd(C_term[i:i+11]) >= 2.0:
            transmem = True 
    if signal_pep == True and transmem == True:
        print(defline)

