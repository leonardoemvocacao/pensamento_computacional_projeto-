preco_frutas = {
    'maçá': 2.5,
    'banana': 1.8,
    'laranja': 3.0
}

fruta_desejada = 'maçá'

resultado = preco_frutas.get(fruta_desejada, 'Fruta não encontrada')
print(f"o preço da {fruta_desejada} é R${resultado}")