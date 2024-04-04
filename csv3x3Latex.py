# desenvolvido por rafael ferreira
# email:rsferreira@inf.ufpel.edu.br
# desenvolvido durante o doutorado da federal de pelotas
# Ano:2024

import csv

def csv_to_latex_table(csv_file_path):
    latex_code = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        # Processa o cabeçalho
        header = next(csv_reader)
        num_columns = len(header)
        latex_code.append(r"\begin{tabular}{" + "l" * num_columns + "}")
        latex_code.append(r"\hline")
        latex_code.append(" & ".join([f"\\multicolumn{{1}}{{c}}{{\\cellcolor[HTML]{{EFEFEF}}\\textbf{{{cell.strip()}}}}}" for cell in header if cell.strip()]) + r" \\ \hline")
        
        # Processa as linhas com efeito zebrado
        row_count = 1
        for row in csv_reader:
            if row_count % 2 == 1:  # Linhas ímpares                
                latex_code.append(" & ".join([cell.strip() for cell in row]) + r" \\ ")                
            else:  # Linhas pares
                latex_code.append(r"\cellcolor[HTML]{EFEFEF} " + " & \cellcolor[HTML]{EFEFEF}".join([cell.strip() for cell in row]) + r" \\ ")
                
            row_count += 1
        
        # Finaliza a tabela
        latex_code.append(r"\end{tabular}")
    
    return "\n".join(latex_code)

def replace_markers(latex_document):
    replacements = {
       'AppS_1':'$AppS_{1}$','AppS_2':'$AppS_{2}$','AppS_3':'$AppS_{3}$','AppS_4':'$AppS_{4}$',
'AppS 1':'$AppS_{1}$','AppS 2':'$AppS_{2}$','AppS 3':'$AppS_{3}$','AppS 4':'$AppS_{4}$',
'AXCS1_1':'$AXCS1_{1}$','AXCS1_2':'$AXCS1_{2}$','AXCS1_3':'$AXCS1_{3}$','AXCS1_4':'$AXCS1_{4}$',
'AXCS2_1':'$AXCS2_{1}$','AXCS2_2':'$AXCS2_{2}$','AXCS2_3':'$AXCS2_{3}$','AXCS2_4':'$AXCS2_{4}$',
'AXCS3_1':'$AXCS3_{1}$','AXCS3_2':'$AXCS3_{2}$','AXCS3_3':'$AXCS3_{3}$','AXCS3_4':'$AXCS3_{4}$',
'AXCS4_1':'$AXCS4_{1}$','AXCS4_2':'$AXCS4_{2}$','AXCS4_3':'$AXCS4_{3}$','AXCS4_4':'$AXCS4_{4}$' }
    for old, new in replacements.items():
        latex_document = latex_document.replace(old, new)
    return latex_document
def main():
    csv_files = ['./csv/tabela01.csv', './csv/tabela02.csv', './csv/tabela03.csv', 
                 './csv/tabela04.csv', './csv/tabela05.csv', './csv/tabela06.csv']
    tables = [csv_to_latex_table(file) for file in csv_files]

    latex_document = r"\begin{table}[]"
    latex_document += "\n" + r"\footnotesize"
    latex_document += "\n" + r"\center"
    latex_document += "\n" + r"\captionsetup{justification=centering}"
    latex_document += "\n" + r"\begin{tabular}{ccc}"

    for i in range(0, len(tables), 3):
        latex_document += "\n" + " & ".join(tables[i:i+3]) + r" \\"

    latex_document += "\n" + r"\end{tabular}"
    latex_document += "\n" + r"\caption{Resultados do modulo Corte}"
    latex_document += "\n" + r"\label{tbCorte}"
    latex_document += "\n" + r"\end{table}"

    latex_document = replace_markers(latex_document)

    with open("./csv/tabela.latex", 'w') as latex_file:
        latex_file.write(latex_document)

    print("O documento LaTeX foi salvo.")

if __name__ == "__main__":
    main()
    print("./csv/tabela.latex")
