# dicionario 
usuario = {
    'nome': "Alex Machado",
    'idade': 41,
    'alutra': 1.72,
    'email': "123.456.789-12",
    'telefone': "(61) 98765-4321"
}
# exibe valor especifico
print(f"Nome: {usuario['nome']}")
print(f"Email: {usuario.get('email')}")

# percorre o dicionario 
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")