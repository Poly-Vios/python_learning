filename = "Example DNA - sequence.fasta"
with open("Example DNA - sequence.fasta") as f:
    for line in f:
        line = line.strip()
        print(line)