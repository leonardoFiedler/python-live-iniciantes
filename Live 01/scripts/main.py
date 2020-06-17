# Python

# a = "Leonardo"
# b = "1"

# print(a)

# a = 1
# print(a)

# b = 4.3
# b = 0.2

# valor = True
# valor = False

# # keyword
# y = complex(5,2)
# print(type(y))
# print(type(valor))

def subtracao(x, y=0):
    # exibicao = 'Valor de X = {0}, valor de Y = {1}'.format(x , y)
    # print(exibicao)
    # print("Valores", x, y)
    return x - y


valor_de_um_numero_bonito = 42


tupla = ('Maçã', 'Banana', 'Pera', 'Morango', 'Melancia')

lista = ['Maçã', 'Banana', 'Pera', 'Morango', 'Melancia']

# print(lista)

# lista.append()

# print(lista)

a = sorted(lista, reverse=True)

# [ 0, 1 [

# print(a)

# print(subtracao(5,2))
# print(subtracao(8))


# print(subtracao(x=3, y=2))
# print(subtracao(y=3, x=2))

pessoas = [
    {
    'nome' : 'Suellen',
    'idade' : 22,
    'escolaridade' : 'Ensino Superior Incompleto'
    },

    {
    'nome' : 'Leonardo',
    'idade' : 24,
    'escolaridade' : 'Ensino Superior Completo'
    },
    
    {
    'nome' : 'Iago',
    'idade' : 26,
    'escolaridade' : 'Ensino Superior Completo'
    },

    {
    'nome' : 'Joaquim',
    'idade' : 12,
    'escolaridade' : 'Ensino Fundamental'
    },

    {
    'nome' : 'Samuca',
    'idade' : 68,
    'escolaridade' : 'Phd'
    }
]

# print(pessoa[0])

# pessoa['nome'] = Obtenha o valor do nome na variavel pessoa

for pessoa in pessoas:
    if pessoa['idade'] >= 65:
        print("A pessoa {} é anciã.".format(pessoa['nome']))
    elif pessoa['idade'] >= 18:
        print("A pessoa {} é maior de idade.".format(pessoa['nome']))
    else:
        print("A pessoa {} é menor de idade.".format(pessoa['nome']))




# print("A pessoa {0}, possui a idade: {1} e esta com a seguinte escolaridade: {2}".format(pessoa['nome'], pessoa['idade'], pessoa['escolaridade']))
# print(pessoa['nome'])



