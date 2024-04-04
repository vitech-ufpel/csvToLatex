# desenvolvido por rafael ferreira
# email:rsferreira@inf.ufpel.edu.br
# desenvolvido durante o doutorado da federal de pelotas
# Ano:2024


import csv
caminho = '/run/media/rsf/vms/python/csv/blocosFixo/'

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

def main():
    csv_files = [        
        caminho + 'tabela01.csv',
        caminho + 'tabela02.csv',
        caminho + 'tabela03.csv',
        caminho + 'tabela04.csv']
    tables = [csv_to_latex_table(file) for file in csv_files]

    # Concatenando as tabelas em duas colunas e duas linhas
    latex_document = r"\begin{table}[htb]"
    latex_document += "\n" + r"\footnotesize"
    latex_document += "\n" + r"\center"
    latex_document += "\n" + r"\captionsetup{justification=centering}"
    latex_document += "\n" + r"\begin{tabular}{cc}"
    
    latex_document += "\n" + tables[0] + "&" + tables[1] + r"\\"
    latex_document += "\n" + tables[2] + "&" + tables[3]

   # latex_document += "\n" + tables[0] + r"\\"
    #latex_document += "\n" + tables[1] 


    #latex_document += "\n" + tables[0] + r"\\"
    #latex_document += "\n" + tables[1] 

    latex_document += "\n" + r"\end{tabular}"
    latex_document += "\n" +r"\caption{Resultados do modulo Corte}"
    latex_document += "\n" +r"\label{tbCorte}"
    latex_document += "\n" + r"\end{table}"

    latex_document =  latex_document.replace('AppS_1','$AppS_{1}$')
    latex_document =  latex_document.replace('AppS_2','$AppS_{2}$')
    latex_document =  latex_document.replace('AppS_3','$AppS_{3}$')
    latex_document =  latex_document.replace('AppS_4','$AppS_{4}$')


    latex_document =  latex_document.replace('AppS 1','$AppS_{1}$')
    latex_document =  latex_document.replace('AppS 2','$AppS_{2}$')
    latex_document =  latex_document.replace('AppS 3','$AppS_{3}$')
    latex_document =  latex_document.replace('AppS 4','$AppS_{4}$')

    latex_document =  latex_document.replace('AppS1','$AppS_{1}$')
    latex_document =  latex_document.replace('AppS2','$AppS_{2}$')
    latex_document =  latex_document.replace('AppS3','$AppS_{3}$')
    latex_document =  latex_document.replace('AppS4','$AppS_{4}$')

    latex_document =  latex_document.replace('AAP.M.','P.M.')
    latex_document =  latex_document.replace('ABG.D.R','G.D.R')



    latex_document =  latex_document.replace('AXCS1_1','$AXCS1_{1}$')
    latex_document =  latex_document.replace('AXCS1_2','$AXCS1_{2}$')
    latex_document =  latex_document.replace('AXCS1_3','$AXCS1_{3}$')
    latex_document =  latex_document.replace('AXCS1_4','$AXCS1_{4}$')


    latex_document =  latex_document.replace('AXCS2_1','$AXCS2_{1}$')
    latex_document =  latex_document.replace('AXCS2_2','$AXCS2_{2}$')
    latex_document =  latex_document.replace('AXCS2_3','$AXCS2_{3}$')
    latex_document =  latex_document.replace('AXCS2_4','$AXCS2_{4}$')

    latex_document =  latex_document.replace('AXCS3_1','$AXCS3_{1}$')
    latex_document =  latex_document.replace('AXCS3_2','$AXCS3_{2}$')
    latex_document =  latex_document.replace('AXCS3_3','$AXCS3_{3}$')
    latex_document =  latex_document.replace('AXCS3_4','$AXCS3_{4}$')

    latex_document =  latex_document.replace('AXCS4_1','$AXCS4_{1}$')
    latex_document =  latex_document.replace('AXCS4_2','$AXCS4_{2}$')
    latex_document =  latex_document.replace('AXCS4_3','$AXCS4_{3}$')
    latex_document =  latex_document.replace('AXCS4_4','$AXCS4_{4}$')

    latex_document =  latex_document.replace('AXCS11','$AXCS1_{1}$')
    latex_document =  latex_document.replace('AXCS12','$AXCS1_{2}$')
    latex_document =  latex_document.replace('AXCS13','$AXCS1_{3}$')
    latex_document =  latex_document.replace('AXCS14','$AXCS1_{4}$')


    latex_document =  latex_document.replace('AXCS21','$AXCS2_{1}$')
    latex_document =  latex_document.replace('AXCS22','$AXCS2_{2}$')
    latex_document =  latex_document.replace('AXCS23','$AXCS2_{3}$')
    latex_document =  latex_document.replace('AXCS24','$AXCS2_{4}$')

    latex_document =  latex_document.replace('AXCS31','$AXCS3_{1}$')
    latex_document =  latex_document.replace('AXCS32','$AXCS3_{2}$')
    latex_document =  latex_document.replace('AXCS33','$AXCS3_{3}$')
    latex_document =  latex_document.replace('AXCS34','$AXCS3_{4}$')

    latex_document =  latex_document.replace('AXCS41','$AXCS4_{1}$')
    latex_document =  latex_document.replace('AXCS42','$AXCS4_{2}$')
    latex_document =  latex_document.replace('AXCS43','$AXCS4_{3}$')
    latex_document =  latex_document.replace('AXCS44','$AXCS4_{4}$')
    

    latex_document =  latex_document.replace('avg_qtd','Média')
    
    #latex_document =  latex_document.replace('%','\%')





    # Salva o documento LaTeX
    with open(caminho + "tabela.latex", 'w') as latex_file:
        latex_file.write(latex_document)

    print("O documento LaTeX foi salvo.")

if __name__ == "__main__":
    main()




