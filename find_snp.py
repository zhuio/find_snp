from Bio import SeqIO
from Bio.Seq import Seq


def find_snp(scaffold,geno):
    with open('result.txt','w') as f:
        for seq_record in SeqIO.parse("Ginkgo_biloba.scaf.fa", "fasta"):
            for i in range(0,len(scaffold)):
                if seq_record.id == scaffold[i]:
                        f.write(str(seq_record.id))
                        f.write('\t')
                        f.write(geno[i])
                        f.write('\n')
                        f.write(str(seq_record.seq[int(geno[i])-301:int(geno[i])]))
                        f.write('\n')
                        f.write(str(seq_record.seq[int(geno[i]):int(geno[i])+300]))
                        f.write('\n')


def read_geno(file):
    with open(file,'r') as f:
        scaffold = []
        geno = []
        for line in f.readlines():
            items = line.strip('\r\n').split('\t')
            scaffold.append(items[0])
            geno.append(items[1])
        return scaffold,geno

s , g = read_geno('Sex.sig_snp.geno')
find_snp(s,g)
