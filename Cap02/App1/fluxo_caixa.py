import csv
import classificaListas as listas

def main():
    try:
        arquivo = csv.reader(open('planilhas/Balanco_Patrimonial.csv', encoding = 'UTF-8'))
    except IOError:
        pass

    linhas = []

    for linha in arquivo:
        linhas.append(linha)


    balanceDict = {}
    curDict = {}

    curList = []

    ativos, patrimonio_liquido, pl = geraBalancoPatrimonial(geraBalancoDict(linhas, balanceDict, curDict, curList))
    print(cashAccountingTransform(ativos))

def geraBalancoDict(linhas, balanceDict, curDict, curList):
    count = 0

    while (count < len(linhas)):
        if (linhas[count][0] != '' or 'Total' not in linhas[count][0]):
            name = linhas[count][0]
            categoryList = []
            count = count + 1

            if (count + 1 >= len(linhas)):
                break
            else:
                while (linhas[count][0] == '' and linhas[count][len(linhas[count]) - 1] != ''):
                    resultList = []
                    for s in linhas[count]:
                        if (s != ''):
                            resultList.append(s)
                    categoryList.append(resultList)
                    count = count + 1

        balanceDict[name.lower()] = categoryList

        count = count + 1

    return balanceDict    

def geraBalancoPatrimonial(balanceDict):
    ativos = {}
    passivos = {}
    patrimonio_liquido = {}

    for key in balanceDict:
        if key == 'ativos':
            cashDict = {}
            inventoryDict = {}
            acctsReceivable = {}
            ppe = {}
            prepaidExp = {}
            other = {}

            for value in balanceDict[key]:
                for tword in listas.cashIdentify:
                    if (tword.lower() in value[0].lower()):
                        cashDict[value[0]] = float(value[1])

                for tword in listas.inventoryIdentify:
                    if (tword.lower() in value[0].lower()):
                        inventoryDict[value[0]] = float(value[1])
                
                for tword in listas.arIdentify:
                    if (tword.lower() in value[0].lower()):
                        acctsReceivable[value[0]] = float(value[1])
                
                for tword in listas.depAssetIdentify:
                    if (tword.lower() in value[0].lower()):
                        ppe[value[0]] = float(value[1])

                for tword in listas.prepaidIdentify:
                    if (tword.lower() in value[0].lower()):
                        prepaidExp[value[0]] = float(value[1])

            ativos['Caixa'] = cashDict
            ativos['Inventario'] = inventoryDict
            ativos['Recebíveis'] = acctsReceivable
            ativos['Imobilizado'] = ppe
            ativos['Antecipados'] = prepaidExp
            ativos['Outros'] = other

        if key == 'passivos':
            loanDict = {}
            acctsPayable = {}
            unearnedRev = {}
            others = {}

            for value in balanceDict[key]:

                for tword in listas.shortLoanIdentify:
                    if (tword.lower() in value[0].lower()):
                        loanDict[value[0]] = float(value[1])

                for tword in listas.apIdentify:
                    if (tword.lower() in value[0].lower()):
                        acctsPayable[value[0]] = float(value[1])
                        
                for tword in listas.unearnRevIdentify:
                    if (tword.lower() in value[0].lower()):
                        unearnedRev[value[0]] = float(value[1])

            passivos['Emprestimos'] = loanDict
            passivos['A Pagar'] = acctsPayable
            passivos['Faturados'] = unearnedRev
            passivos['Outros'] = others

        if key == 'patrimonio liquido':

            retainedEarnings = {}

            for value in balanceDict[key]:
                    retainedEarnings[value[0]] = value[1]

                    
            patrimonio_liquido['Lucros'] = retainedEarnings

    print ('Ativos: ', ativos)
    print ('Passivos: ', passivos)   
    print ('Patrimonio Liquido: ', patrimonio_liquido)       

    return ativos, passivos, patrimonio_liquido

def cashAccountingTransform(ativos):
    cashAccounting = True
    novoAtivos = {}

    for entry in ativos:
        novoAtivos[entry] = ativos[entry]

    print('\nAutomação do Fluxo de Caixa para a DRE\n')

    if cashAccounting:
        for key in ativos:
            while True:
                strPaymentInPeriod = input(f'Algum pagamento foi recebido para <{key}> durante este período? (S/N): ')
                if strPaymentInPeriod.lower() != 's' and strPaymentInPeriod.lower() != 'n':
                    print('Por favor digite S ou N.')
                    continue
                else:
                    break
            
            paymentInPeriod = strPaymentInPeriod == 's'
            while True:
                
                strGSInPeriod = input(f'Foi < {key} > entregue dentro deste período? (S/N): ')
                
                if strGSInPeriod.lower() != 's' and strGSInPeriod.lower() != 'n':
                    print('Por favor digite S ou N.')
                    continue
                else:
                    break

            gsInPeriod = strGSInPeriod == 's'
            
            if paymentInPeriod == False and gsInPeriod == False:
                del novoAtivos[key]
            else:
                continue
        return novoAtivos

    print("\nFim\n")   

main()