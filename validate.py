# 验证结果的正确性
def find_chr():
    with open('result.txt','w') as f:
        for seq_record in SeqIO.parse("Qrob_PM1N.fa", "fasta"):
            q = re.findall('Qrob_Chr',str(seq_record.id))
            if q and q[0] == 'Qrob_Chr':
                f.write(seq_record.id + '\n')
                f.write('完整的序列是\n')
                f.write(str(len(str(seq_record.seq))) + '\n')
                N = str(seq_record.seq).replace('N','')
                f.write('去除N的序列为\n')
                f.write(str(len(N)) + '\n')

find_chr()
