from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


gui = Usuario('gui')
yuri = Usuario('yuri')


lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)


leilao = Leilao('celular')


leilao.lances.append(lance_do_gui)

leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')

