# 011: Calcule a sua area e a quantidade de tinta necessária para pintá-la, sabendo que cada lintro de tinta pinta uma área de 2m².
print('-' * 12)
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, área))

tinta = área / 2
print('Para pintar sua parede serão necessários {}l de tinta.'.format(tinta))
print('-' * 12)
