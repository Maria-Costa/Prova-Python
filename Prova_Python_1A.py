# Beatriz Magnaboschi Azevedo N°06
# Felipe Muller Maus N°12
# Gabriel Liondas N°14
# Lorena dos Anjos Manojo N°22
# Maria Eduarda Costa dos Santos N°26
# Nicole Fernanda Rodrigues Carrillo N°29

print("="*40)
print("-"*11, "Calculo de notas", "-"*11)
print("="*40)

def validaNota(nota):
    if nota >= 7:
        return nota
    else:
        nota_rec= float(input("Insira a nota da \033[4mrecuperação\033[m: "))
    if nota_rec >=7:
        return 7
    else:
        return nota


def calculo_media(lista_media):
    soma = sum(lista_media) + lista_media[1] + lista_media[2]
    quantidade = len(lista_media) + 2
    return soma/quantidade

alunos_aprovados = []
alunos_reprovados = []

while True:
    nome_aluno = str(input("Nome do aluno: ")).capitalize()
    nota_prim = float(input("Insira a média do primeiro tri: "))
    nota_segundo = float(input("Insira a média do segundo tri: "))
    if nota_prim < 7 and nota_segundo >= 7:
        nota_prim = 7

    nota_segundo = validaNota(nota_segundo)
    nota_terceiro = validaNota(float(input("Insira a média do terceiro tri: ")))

    media_final = calculo_media([nota_prim,nota_segundo,nota_terceiro])

    tupla_aluno= (nome_aluno,media_final)

    print("")
    print(f'Estudante: {nome_aluno}\n'
          f'1° nota = {nota_prim:.2f}\n'
          f'2° nota = {nota_segundo:.2f}\n'
          f'3° nota = {nota_terceiro:.2f}\n'
          f'Ficou com média = {media_final}')
    print("")

    if media_final >= 7:
        alunos_aprovados.append(tupla_aluno)
    else:
        alunos_reprovados.append(tupla_aluno)

    terminar = input("Deseja incluir um novo estudante [S/N]? ").lower()
    print("-" * 40)
    if terminar == "n":
        break
    elif terminar == "s":
        continue
    else:
        print("Entrada inválida, confirme os resultados")
        print("-" * 40)
        break


print(f'RELAÇÃO DOS ALUNOS APROVADOS: \n \33[32m{alunos_aprovados}\33[m')
print(f'RELAÇÃO DOS ALUNOS REPROVADOS: \n \33[31m{alunos_reprovados}\33[m')