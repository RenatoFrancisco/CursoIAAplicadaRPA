# Identifica os ativos que podem ser classificados como "Cash"
cashIdentify = ["caixa", "banco", "conta_corrente", "poupança"]

# Identifica itens de ativos que devem ser classificados como 'Estoque'
inventoryIdentify = ["estoques"]

# Identifica itens de ativos que devem ser classificados como 'Contas a Receber'
arIdentify = ["Contas a Receber", "empréstimo", "creditos", "recebível", "recebíveis"]

# Identifica itens de ativos que são pré-pagos
prepaidIdentify = ["Despesas Pagas Antecipadamente"]

# Identifica itens de ativos que devem estar sujeitos a depreciação
depAssetIdentify = ["Intangivel", "Estoques", "Imobilizado", "automoveis", "predios", "maquinas", "computadores", "carros"]

# Identifica itens de passivo que devem ser classificados como 'empréstimos'
shortLoanIdentify = ["Investimento de Longo Prazo", "Demais Ativos de Longo Prazo"]

# Identifica itens de passivo que devem ser classificados como 'Contas a Pagar'
apIdentify = ["Contas a Pagar", "Taxas Devidas", "Emprestimos Bancarios", "passivos", "pagaveis"]

# Identifica itens de passivo que devem ser classificados como receita não obtida
unearnRevIdentify = ["unearned", "revenue", "advance", "advanced", "prepaid", "pre-paid", "prepay", "pre-pay"]

# Identifique as despesas do programa
pExpenseIdentify = ["program", "project", "operation", "operations"]

# Identificar ganhos de doação
dGainIdentify = ["doacoes", "presentes"]

# Identifica as receitas das atividades
revenueIdentify = ["faturamento", "salário", "fee"]

# Identifica as despesas administrativas
aExpenseIdentify = ["admin", "administrative", "staff", "head office"]

# Identifica itens de despesas que devem ser classificados como custo de financiamento
fExpenseIdentify = ["juros", "banco"]