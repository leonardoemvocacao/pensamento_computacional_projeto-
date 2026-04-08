from datetime import datetime


print("=" * 40)
print("✨ BEM-VINDO AO PROGRAMA ✨")
print("=" * 40)


print("\n🔎 Testando tipos de dados:")
print("Número inteiro:", type(10).__name__)
print("Texto:", type("Python").__name__)
print("Número decimal:", type(3.14).__name__)

print("\n" + "-" * 40)

nome = input("👤 Digite seu nome: ")

# Hora atual
agora = datetime.now()
hora = agora.strftime("%H:%M:%S")

# Saudação
print("\n" + "=" * 40)
print(f"👋 Olá, {nome}!")
print(f"⏰ Agora são {hora}")
print("🎉 Seja muito bem-vindo(a)!")
print("=" * 40)