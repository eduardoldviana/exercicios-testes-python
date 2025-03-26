# 17. Faça uma funçao que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
# Exemplos de saídas com as entradas "user" "user" "user123" respectivamente
# "Erro: A senha não pode ser igual ao nome de usuário. Tente novamente."
# "Usuário e senha cadastrados com sucesso!"
def validar_usuario_senha():
    user = input()
    while True:
        password = input()
        if password != user:
            break
        else:
            print('Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.')
    return 'Usuário e senha cadastrados com sucesso!'
print(validar_usuario_senha())
