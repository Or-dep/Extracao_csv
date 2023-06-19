import glob
import os
import  csv

nome_pasta = "Arquivos"
os.mkdir(nome_pasta)

valores = [5,1,2,10]
ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
date = [1,2,3,4,5,6,7,8,9,10,11,12]
montagem01 = [0,1,4,7,10,13,16,19,22,25,28,31,34,37]
montagem02 = [0,2,5,8,11,14,17,20,23,26,29,32,35,38]
montagem03 = [0,3,6,9,12,15,18,21,24,27,30,33,36,39]

def extracao(ct, arquivo):
    lista01 = csv.reader(open(arquivo),delimiter=";")
    meses = []
    ncms = []
    fobs = []
    x = []
    base = []
    lts = [0]*14
    bd = []
    ind = []
    for itens in lista01:
        if ct == itens[5]:
            for vl in valores:
                if vl == 1:
                    meses.append(int(itens[vl]))
                elif vl == 2:
                    ncms.append(int(itens[vl]))
                elif vl == 10:
                    fobs.append(int(itens[vl]))

    for cz in range(len(meses)):
        x.append(ncms[cz])
        x.append(meses[cz])
        x.append(fobs[cz])
        base.append(x)
        x = []
    x = list(set(ncms))
    ind = x
    for xc in x:
        lts[0] = xc
        for dt in date:
            for eixo in base:
                ncm, data, vale = eixo
                if xc == ncm:
                    if dt == data:
                        lts[dt] += vale
                        lts[13] += vale
                    elif data != date:
                        pass
            if dt == 12:
                bd.append(lts)
                lts = [0]*14
    return bd,ind


def extrair(ct):
    Unico = [["NCM", "Jan_imp", "Jan_exp", "Jan_Net","Fev_imp", "Fev_exp", "Fev_Net", "Mar_imp", "Mar_exp", "Mar_Net",  "Abr_imp", "Abr_exp", "Abr_Net", "Mai_imp", "Mai_exp", "Mai_Net", "Jun_imp", "Jun_exp", "Jun_Net", "Jul_imp", "Jul_exp", "Jul_Net", "Ago_imp", "Ago_exp", "Ago_Net", "Set_imp", "Set_exp", "Set_Net", "Out_imp", "Out_exp", "Out_Net", "Nov_imp", "Nov_exp", "Nov_Net", "Dez_imp", "Dez_exp", "Dez_Net", "Total_imp", "Total_exp", "Total_Net"]]
    # 40 itens
    
    novo_arquivo = str(ct)+".csv"
    dados = []
    fim = []
    ind = []
    caminho = '.'  # Pasta atual
    padrao = '*.csv'  # Padrão de arquivo CSV 
    arquivos_csv = glob.glob(f'{caminho}/{padrao}')
    arquivo = [os.path.basename(arquivo) for arquivo in arquivos_csv]

    for x in range(len(arquivo)):
        if x == 0:
            aa,xy = extracao(ct, arquivo[x])
            fim = aa
            ind += xy
        elif x == 1:
            aa,xy = extracao(ct, arquivo[x])
            dados = aa
            ind += xy

    lts = [0] * 40
    indicadores = list(set(ind))
    xy = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    for ids in indicadores:     #    ids
        lts[0] = ids
        for dt in xy:           #    data
            for dd in dados:    #    dados imp
                item = dd
                teste = dt - 2
                if lts[0] == dd[0] and teste == -1:
                    vl0 = item[teste]
                    lts[montagem01[teste]] = vl0
                    lts[montagem03[teste]] = -vl0
                if lts[0] == dd[0]:
                    if dd[dt] == [0]:
                        vl0 = 0
                        lts[montagem01[dt]] = vl0
                    elif dd[dt] != [0]:
                        vl0 = dd[dt]
                        lts[montagem01[dt]] = vl0
                        lts[montagem03[dt]] = -vl0
                       
            for ff in fim:      #    dados exp
                item = ff
                teste = dt - 2
                if lts[0] == ff[0] and teste ==-1:
                    vl0 = item[teste]
                    lts[montagem02[teste]] = vl0
                    lts[montagem03[teste]] += vl0
                if lts[0] == ff[0]:
                    if ff[dt] == [0]:
                        vl0 = 0
                        lts[montagem02[dt]] = vl0
                    elif ff[dt] != [0]:
                        vl1 = ff[dt]
                        lts[montagem02[dt]] = vl1
                        lts[montagem03[dt]] += vl1

            if dt == 12:
                Unico.append(lts)          
                lts = [0] * 40              
    
    caminho = os.path.join(nome_pasta,novo_arquivo)
    with open(caminho,'w', newline='') as arq_csv:
        esc_csv = csv.writer(arq_csv)
        esc_csv.writerows(Unico)
        
    return print(f'o arquivo {ct} foi!')

for y in range(len(ufs)):
    extrair(ufs[y])
