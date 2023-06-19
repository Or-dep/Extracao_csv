-----------------------
        PT-BR
-----------------------

Este é um projeto de extração que fiz recentemente.

É um projeto feito sem fins lucrativos.

Somente para meu desenvolvimento intelectual com a linguagem python.

Todos os dados extraídos dos arquivos csv foram obtidos no site da base comércio exterior brasil 

----------------------------------------------------
http://comexstat.mdic.gov.br/pt/home
----------------------------------------------------

Para executar o programa baixe dois arquivos csv do site acima
Um importação e outro de exportação


O arquivo script_completo.py executa as seguintes funções:

1 - Coleta e unifica os seguintes dados "CO_MES", "CO_NCM", "SG_UF_NCM", "VL_FOB".
Dos arquivos EX: "EXP_2022.csv" & "IMP_2022.csv"

2 - Identificação do valores por "NCM"

3 - Separa e soma valores de "VL_FOB" que referentes ao mesmo mês

4 - Processa os dados de "VL_FOB" separando a soma total de cada mês em colunas, tendo uma coluna para cada mês e um total somado ao final do ciclo anual. EX: "Total_imp", "Total_exp", "Total_Net"

5 - Subtrai os valores de exportação e importação e cria uma coluna com o nome do mês. EX: "Jan_Net"

6 - Separação dos valores de cada mês sendo estabelecido como IMPORTAÇÃO, EXPORTAÇÃO, NET. EX: "Jan_imp","Jan_exp","Jan_Net"



-----------------------
            EN
-----------------------

This is an extraction project I recently worked on.

It is a non-profit project.

It was developed solely for my intellectual development using the Python language.

All the data extracted from the CSV files was obtained from the Brazilian foreign trade database website.

----------------------------------------------------
http://comexstat.mdic.gov.br/pt/home
----------------------------------------------------

To run the program, download two CSV files from the website mentioned above.
One for imports and another for exports.


The script_completo.py file performs the following functions:

1 - Collects and consolidates the following data: "CO_MES" (month code), "CO_NCM" (NCM code), "SG_UF_NCM" (state code), "VL_FOB" (FOB value) from the files "EXP_2022.csv" and "IMP_2022.csv".

2 - Identifies values by "NCM" code.

3 - Separates and sums the "VL_FOB" values that correspond to the same month.

4 - Processes the "VL_FOB" data by separating the total sum for each month into columns, with one column for each month and a total sum at the end of the annual cycle. Example: "Total_imp" (total imports), "Total_exp" (total exports), "Total_Net" (net total).

5 - Subtracts the export and import values and creates a column with the month name. Example: "Jan_Net" (January net).

6 - Separates the values for each month, categorizing them as IMPORT, EXPORT, and NET. Example: "Jan_imp" (January imports), "Jan_exp" (January exports), "Jan_Net" (January net).
