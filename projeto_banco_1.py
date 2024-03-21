menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("Saldo atual: R${:.2f}".format(saldo))
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a depositar: "))
        saldo += valor_deposito
        extrato += f"Depósito: +R${valor_deposito:.2f}\n"
        print("Depósito de R${:.2f} realizado com sucesso.".format(valor_deposito))
    elif opcao == "s":
        valor_saque = float(input("Digite o valor a sacar (limite de R$500 por saque): "))
        if valor_saque > saldo:
            print("Saldo insuficiente.")
        elif valor_saque > limite_saque:
            print("Limite de saque excedido (R$500).")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques excedido para o dia.")
        else:
            saldo -= valor_saque
            extrato += f"Saque: -R${valor_saque:.2f}\n"
            numero_saques += 1
            print("Saque de R${:.2f} realizado com sucesso.".format(valor_saque))
    elif opcao == "e":
        print("Extrato:")
        print(extrato)
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")