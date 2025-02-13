print ('Bem-vindo a DMAPUTO')

print('=' *10,'Menu','=' *10, '\n'
                              'O que deseja aprender?\n'
                              '1. Doces\n'
                              '2. Salgados\n'
                              ''
                              '________________________________________')

#inicio dos bolos (todos doces)
opcao = int (input('Por favor, escolha a opcao:'))
match opcao:
    case 1:
       print('1. Bolos\n'
             '2. Biscoitos\n'
             '3. Sorvete\n'
             '4. Pudim')
#inicio dos bolos
doces = int(input('Por favor, escolha a opcao:'))
print('_'*20)
match doces:
    case 1:
        print('1. Bolo mil folhas\n'
              '2. Bolo caramelizado\n'
              '3. Bolo de custard\n'
              '4. Bolo gelado\n'
              '5. Bolo floresta negra\n'
              '6. Bolo de chocolate\n'
              '7. Bolo Red Velvet\n'
              '8. Bolo de cenoura\n'
              '9. Bolo ingles')
print('_'*20)
bolos = int (input('Por favor, escolha a opcao:'))
print('_'*20)
match bolos:
    case 1:
        print('Bolo mil folhas\n'
               'INGREDIENTES\n'
              '8 ovos\n'
              '2 xicaras de farinha de trigo\n'
              '1 xicara de acucar\n'
              '1 xicara de agua\n'
              '1 xicara de oleo\n'
              '1 colher de sopa de essencia de vanila\n'
              '1 colher de sopa de fermento em po (royal)\n'
              '500ml de nata doce\n'
              'Morangos para decorar (quantidade que basta)\n'
              '1 pasta de massa folhada assada')
        print('_'*20, '\n'
                      'MODO DE PREPARO\n'
                      '1 passo: pegar em duas tigelas e colocas as claras do ovo em uma tigela e as gemas em outra;\n'
                      '2 passo: na tigela que contem as gemas, vamos colocar o acucar e com a ajuda de uma batedeira vamos bater ate esbranquicar e dobrar de volume\n'
                      '3 passo: de seguida vamos adicionar a colher de essencia e continuar a bater\n'
                      '4 passo: colocamos de seguida a xicara de agua e de oleo e depois as de trigo e a colher de royal\n'
                      '5 passo: deixamos de lado e de seguida pegamos a tigela que colocamos as claras e batemos as claras ate o ponto de neve (ate ficar aquela espuma consistente)\n'
                      '6 passo: de seguida juntamos as claras a mistrura que fizemos anteriormente e misturamos mas de forma delicada para nao tirar o ar das claras\n'
                      '7 passo: colocamos a mistura em uma forma untada e levamos ao forno aquecido a 150C por 45min\n'
                      '8 passo: tiramos o bolo do forno deixamos aferecer\n'
                      '9 passo: batemos as natas ate ficarem consistentes e cobrimos o bolo\n'
                      '10 passo: espalhamos a massa folhada e prontos!') #parei aqui

    case 2:
        print('_'*20,'\n'
                     'Bolo caramelizado\n'
                     'INGREDIENTES\n'
                     '3 xicaras de trigo\n'
                     '250g de manteiga\n'
                     '1 xicara de acucar\n'
                     '1 colher de sopa de essencia\n'
                     '1 xicara de caramelo\n'
                     '1 colher de sopa de fermento em po (royal)\n'
                     '20g de chocolate picado\n'
                     '1 colher de sopa de maizena')
        print('_'*20,'\n'
                     'Modo de preparo\n'
                     '1 passo: Numa bacia vamos colocar a manteiga e o acucar, com ajuda de uma batedeira vamos bater ate atingir o ponto de creme\n'
                     '2 passo: vamos adicionar as gemas e o trigo de forma gradual (uma gema, uma colher de trigo) batendo\n'
                     '3 passo: vamos adicionar a xicara do caramelo, a essencia, o resto da farinha do trigo, a maizena e o fermento em po\n'
                     '4 passo: adicionamos as claras em neve e envolvrmos com delicadeza para nao tirar o ar das claras\n'
                     '5 passo: colocamos a massa numa forma untada com manteiga e trigo e levamos ao forno pre-aquecido a 150C por 59min\n'
                     '6 passo: de seguida tire o bolo do forno e povilhe com o acucar de confeteiro por cima!')
        print('_'*20)
    case 3:
        print('Bolo de custard\n'
              'INGREDIENTES\n'
              '8 ovos\n'
              '3 xicaras de trigo\n'
              '1 xicara de leite (agua caso nao tenha leite)\n'
              '2 colheres de sopa de custard\n'
              '1 colher de sopa de fermento em po (royal)\n'
              '250g de manteiga\n'
              '1 colher de sopa de essencia de vanila\n'
              '1 xicara de acucar\n'
              '_'*20,'\n'
              'Modo de preparo\n'
              '1 passo: separamos as claras das gemas\n'
                     '2 passo: em uma bacia batemos a manteiga com o acucar ate atingir o ponto de creme\n'
                     '3 passo: adicionamos as gemas e o trigo de forma gradual\n'
                     '4 passo: adicionamos o leite, o restante do trigo, o fermento, a essencia e o custard (misturamos)\n'
                     '5 passo: batemos as claras ate atingir o ponto de neve e adicionamos a mistura que fizemos\n'
                     ' anteriormente e mexemos com delicadeza para nao tirar o ar das claras\n'
                     '6 passo: colocamos a massa numa forma untada com manteiga e trigo e levamos ao forno pre-aquecido a 150C por\n'
                     '59min\n'
                     '7 passo: podes decorar o creme de custard e ja esta!')
        print('_'*20)
    case 4:
        print('Bolo gelado\n'
              'INGREDIENTES\n'
              '1 pacote de bolachas champanhe\n'
              'massa de bolo chifon com essencia de laranja\n'
              '500g de nata\n'
              'gelatina de diversas cores\n'
              'Frutas (ao seu gosto)\n'
              '_'*20,'\n'
                     'Modo de preparo\n'
                     '1 passo: depois de fazer o bolo de chifon com a essencia de laranja\n'
                     '2 passo: preparamos as gelatinas em potes separados minsturando com agua quente e levamos ao congelador\n'
                     '3 passo: cortamos as frutas em pedacinhos\n'
                     '4 passo: pintamos o nosso bolo de chifon com as natas e colocamos os biscoitos champanhe ao redor do bolo\n'
                     '5 passo: de seguids tiramos a gelatina dos potes e cortamos em pedacinhos, colocamos no topo do bolo juntamente com as frutas\n'
                     'e prontos!')
        print('_'*20)
    case 5:
        print('Bolo floresta magica\n'
              'INGREDIENTES\n'
              '1 colher de sopa de essencia\n'
              '500g de nata doce\n'
              '1 xicara de oleo\n'
              '1 xicara de leite (ou agua)\n'
              '1 xicara de acucar\n'
              '1 colher de sopa de cacau preto\n'
              '2 xicaras de trigo\n'
              '8 ovos\n'
              'Morangos para decorar\n'
              '100g de chocolate branco\n'
              'porpurina (po de brilho)\n'
              '2 colheres de sopa de cacau castanho'
              '_'*20,'\n'
                     'Modo de preparo\n'
                     '1 passo: vamos primeiramente separar as claras das gemas e vamos juntas as gemas com o acucar e bater\n'
                     'ate o ponto de creme\n'
                     '2 passo: vamos adicionar a essencia, o cacau preto e castanho, o leite (ou agua), o oleo, o trigo\n'
                     'e o royal e vamos bater para deixar a mistura homogenea\n'
                     '3 passo: vamos bater as claras ate atingir o ponto de neve e adicionar a mestura anterior e bater com\n'
                     'cuidado para nao tirar o ar as claras\n'
                     '4 passo: vamos colocar a massa numa forma untada com manteiga e cacau e levar ao forno pre-aquecido\n'
                     'a 150C por 59min\n'
                     '5 passo: quando o bolo estiver pronto vamos cortar o bolo em discos e em cada camada vamos color natas\n'
                     'de seguida vamos pintar o bolo com as natas\n'
                     '6 passo: vamos derreter o chocolate amargo e espanhar sobre o papel vegetal e vamos levar para congelas\n'
                     '7 passo: depois de congelado vamos tirar do papel vegetal e quebrar o chocolate e fazer o mesmo\n'
                     'com o chocolate branco, vamos colocar no topo do bolo juntamente com as frutas cortadas em pedacinhos\n'
                     'e pronto!')
        print('_'*20)
    case 6:
        print('Bolo de chocolate\n'
              'INGREDIENTES\n'
              '8 ovos\n'
              '3 xicaras de trigo\n'
              '1 xicara de leite (ou de agua)\n'
              '1 xicara de oleo\n'
              '1 colher se sopa de fermento em po (royal)\n'
              '3 colheres de sopa de cacau\n'
              '_'*20,'\n'
                     'Modo de preparo')
    #fim dos bolos

    case 2:
        print('1. Biscoitos amanteigados\n'
              '2. Fiosses\n'
              '3. Gulabos\n'
              '4.Biscoitos half\n'
              '5. Biscoitos Roman-cream\n'
              '6. Biscoitos de canela')

    case 3:
        print('Sorvete\n'
              'NB: O sorvete tem um base e so vamos alterando os sabores com as frutas e essencias!')

    case 4:
        print('Pudim\n'
              'NB: a base para o pudim e a mesma e vamos alterando as essencias!')

    case _:
        print('Opcao invalida!')

print('_' *20)
 #fim dos bolos (todos doces)



'''  
  case 2:
      print ('1. Arroz\n'
             '2. Temperos para cernes\n'
             '3. Caris\n'
             '4. Pastas')
    case _:
      print('Opcao invalida!')

print('_' *20)

bolos = int(input('Por favor, escolha a opcao:'))
match bolos:
    case 1:
        print('1. Bolo mil folhas\n'
              '2. Bolo caramelizado\n'
              '3. Bolo de custard\n'
              '4. Bolo gelado\n'
              '5. Bolo floresta negra\n'
              '6. Bolo de chocolate\n'
              '7. Bolo Red Velvet\n'
              '8. Bolo de cenoura\n'
              '9. Bolo ingles')

    case 2:
        print('1. Biscoitos amanteigados\n'
              '2. Fiosses\n'
              '3. Gulabos\n'
              '4.Biscoitos half\n'
              '5. Biscoitos Roman-cream\n'
              '6. Biscoitos de canela')

    case 3:
        print('Sorvete\n'
              'NB: O sorvete tem um base e so vamos alterando os sabores com as frutas e essencias!')

    case 4:
        print('Pudim\n'
              'NB: a base para o pudim e a mesma e vamos alterando as essencias!')

    case _:
        print('Opcao invalida!')

print('_' *20)
'''''