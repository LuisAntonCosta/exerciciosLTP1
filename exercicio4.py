notas = [6.3, 7.5, 9.2, 5.1, 6.8]

media = sum(notas) / len(notas)

print("{:,.2f} é a media da turma".format(media))

for nota in notas:
    if nota > media:
        print(f"o aluno que tirou {nota} foi melhor que a media")