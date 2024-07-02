def filter_fasta(input_file, output_file):
    seen_species = set()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        write_seq = False
        for line in infile:
            if line.startswith('>'):
                species = extract_species(line)
                if species not in seen_species:
                    seen_species.add(species)
                    write_seq = True
                    outfile.write(line)
                else:
                    write_seq = False
            elif write_seq:
                outfile.write(line)

def extract_species(header):
    start = header.find("OS=")
    if start == -1:
        return ""
    end = header.find(" ", start + 3)
    if end == -1:
        end = len(header)
    return header[start + 3:end]

# Uso del script
input_file = 'uniprot_PTGR1_vertebrata.fasta'  # Reemplaza con el nombre de tu archivo de entrada
output_file = 'uniprot_PTGR1_vertebrata_filtered.fasta'  # Nombre del archivo de salida

filter_fasta(input_file, output_file)















