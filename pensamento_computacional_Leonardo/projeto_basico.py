# sistema_acaiteria.py

clientes = []
cardapio = {
    "pequeno": {"preco":15, "ml": 250},
    "medio": {"preco": 20, "ml": 330},
    "grande": {"preco": 25, "ml": 600}
}

def cadastrar_cliente():
    print("\n=== Cadastro de Cliente ===")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    clientes.append({"nome": nome, "telefone": telefone})
    print("✅ Cliente cadastrado com sucesso!")

def ver_cardapio():
    print("\n=== Cardápio ===")
    for tamanho, preco in cardapio.items():
        print(f"{tamanho.capitalize()} - R${preco}")

def fazer_pedido():
    print("\n=== Fazer Pedido ===")
    tamanho = input("Escolha (pequeno/médio/grande): ").lower()

    if tamanho in cardapio:
        preco = cardapio[tamanho]
        print(f"🛒 Pedido confirmado: Açaí {tamanho} - R${preco}")
    else:
        print("❌ Opção inválida")

def chat():
    print("\n=== Chat da Loja ===")
    while True:
        msg = input("Você: ").lower()

        if msg == "sair":
            print("Loja: Até logo!")
            break
        elif msg == "oi":
            print("Loja: Olá! Bem-vindo 🍧")
        elif msg == "cardapio":
            ver_cardapio()
        else:
            print("Loja: Não entendi 😅")

def menu():
    while True:
        print("\n=== 🧊 AÇAITÉRIA 🧊 ===")
        print("1 - Cadastro de clientes")
        print("2 - Ver cardápio")
        print("3 - Fazer pedido")
        print("4 - Chat")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            ver_cardapio()
        elif opcao == "3":
            fazer_pedido()
        elif opcao == "4":
            chat()
        elif opcao == "0":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida")

# executar sistema
menu()