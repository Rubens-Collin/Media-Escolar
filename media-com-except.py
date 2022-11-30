
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        n1 = int(input('Nota do PRIMEIRO BIMESTRE de 0 a 10:'))
        if n1 > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif n1 < 0:
            raise InputError('Nota não pode ser menor que 0')

        n2 = int(input('Nota do SEGUNDO BIMESTRE de 0 a 10:'))
        if n2 > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif n2 < 0:
            raise InputError('Nota não pode ser menor que 0')

        n3 = int(input('Nota do TERCEIRO BIMESTRE de 0 a 10:'))
        if n3 > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif n3 < 0:
            raise InputError('Nota não pode ser menor que 0')

        n4 = int(input('Nota do QUARTO BIMESTRE de 0 a 10:'))
        if n4 > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif n4 < 0:
            raise InputError('Nota não pode ser menor que 0')

        media = (n1+n2+n3+n4) / 4
        if media >= 6:
            print(f'A média do aluno foi:{media} O aluno foi aprovado')
        else:
            print(f'A media do aluno foi:{media} O aluno foi reprovado')

        break
    except ValueError:
        print('Valor invalido. Deve-se digitar somente número.')
    except InputError as ex:
        print(ex)

