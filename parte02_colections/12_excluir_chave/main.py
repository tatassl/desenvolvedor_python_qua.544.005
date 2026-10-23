# dicionario
usuario = {
    'nome': "Alex Machado",
    'idade': 41,
    'email': "alex@gmail.com",
    'telefone': "(61) 98765-4321",
    'endereço': "Rio de janeiro"
}
# exibe a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# informa a chave a ser deletada 
chave_escolhida = input("Imforme a chave a excluir: ").strip().lower()

# deleta a chave 
del usuario[chave_escolhida]

# re-exibe o novo dicionario 
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
    
