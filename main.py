from fastapi import FastAPI
app=FastAPI(title="Api do Felps")
receitas=[
    {
        'nome':'Bolo de Morango',

        'ingredietes':['1 xícara (chá) de água','1 xícara (chá) de Nesquick®','4 colheres (sopa) de manteiga','3 ovos','1 e 1/2 xícaras (chá) de açúcar',
                       '3 xícaras (chá) de farinha de trigo','1 colher (sopa) de fermento em pó químico','Manteiga e farinha de trigo para untar',
                       '10 morangos cortados ao meio para decorar','1 caixa de morangos picados (300g)','1 xícara (chá) de açúcar','Suco de 1 limão'],
        'utensílios':['Tigela','Forma','Panela','colher','Liquidificador'],

        'Modo de Preparo':'No liquidificador, bata a água, o Nesquick®, a manteiga, os ovos e o açúcar até ficar homogêneo. Transfira para uma tigela, adicione a farinha e o fermento e misture com uma colher. Despeje em uma fôrma de buraco no meio de 30 cm de diâmetro untada e enfarinhada e leve ao forno médio, preaquecido, por 35 minutos ou até dourar. Retire e deixe esfriar. Para a cobertura, em uma panela misture o morango, o açúcar e o suco de limão. Leve ao fogo baixo e deixe levantar fervura. Cozinhe por 5 minutos e deixe esfriar. Desenforme o bolo, cubra com metade da cobertura, arrume os morangos cortados ao meio sobre o bolo e cubra com a cobertura restante.'
    },
    {
        'nome':'Baião de dois Tradicional',
        'ingredientes':['500g de feijão-de-corda seco','300 g de charque dessalgada e desfiada (carne seca ou carne de sol)','2 colheres (sopa) de manteiga de garrafa','meia xícara (chá) de bacon picado','1 cebola ralada','2 dentes de alho amassados','1 tomate sem sementes picado','meia colher (sopa) de coentro picado','2 xícaras (chá) de arroz lavado e escorrido','2 tabletes de MAGGI® Caldo Carne','1 colher (chá) de sal','1 xícara (chá) de queijo coalho picado','Meio pimentão verde picado'],
        'utensílios':['Taboa de Corte','Panela','Faca','Colher de pau','Panela de Pressão','Bowl'],
        'Modo de preparo':'1.Coloque o feijão-de-corda em um recipiente, cubra com água e deixe de molho por 8 horas. 2.Escorra a água, transfira o feijão para uma panela de pressão e adicione 3 litros de água. Tampe e cozinhe por cerca de 15 minutos após pegar pressão. Desligue, espere a pressão sair naturalmente, abra e verifique se os grãos estão macios. Reserve com parte do caldo (aproximadamente 2 xícaras). 3.Corte a charque em pedaços médios, coloque em uma panela e cubra com água. Leve ao fogo e ferva por 10 minutos. Escorra, troque a água e repita o processo mais uma ou duas vezes para dessalgar bem. Em seguida, cozinhe na panela de pressão por 25 minutos com água limpa até ficar macia. Desfie e reserve. 4. Em uma panela grande, aqueça a manteiga de garrafa em fogo médio. Adicione o bacon e frite até começar a dourar. Acrescente a cebola, o alho, o tomate e o pimentão. Refogue por cerca de 3 minutos até os vegetais ficarem levemente macios e perfumados. 5. Adicione o arroz lavado e escorrido ao refogado, mexendo bem. Coloque a charque desfiada e os tabletes de MAGGI Caldo Carne picados. Misture por alguns minutos para que os sabores se integrem. 6. Acrescente o feijão cozido com parte do caldo e o sal. Misture bem. Cozinhe em fogo baixo, com a panela semi-tampada, por cerca de 15 minutos ou até o arroz cozinhar completamente, ficando úmido, mas não encharcado. Se necessário, adicione mais caldo do feijão aos poucos. 7. Desligue o fogo, misture delicadamente o queijo coalho em cubos, o coentro e a cebolinha. Tampe a panela por 3 a 5 minutos para que o calor derreta levemente o queijo. ',
    },
    {
        'nome':'Brigadeiro',
        'ingredientes':['1 Leite MOÇA® (lata ou caixinha)','3 colheres (sopa) de Chocolate em Pó NESTLÉ CHOCOLATERIA','1 colher (sopa) de manteiga','1 xícara (chá) de chocolate granulado'],
        'utensílios':['Panela'],
        'Modo de Preparo':'1.Em uma panela, coloque o Leite MOÇA com o Chocolate em Pó CHOCOLATERIA e a manteiga. 2.Misture bem e leve ao fogo baixo, mexendo sempre até desprender do fundo da panela (cerca de 10 minutos). 3.Retire do fogo, passe para um prato untado com manteiga e deixe esfriar. 4.Com as mãos untadas, enrole em bolinhas e passe-as no granulado. Sirva em forminhas de papel.',
    },
    {
        'nome':'Lasanha Quatro Queijos',
        'ingredientes':['Molho Branco:','2 colheres (sopa) de manteiga','1 colher (sopa) de farinha de trigo','500 ml de Leite Líquido NINHO® Forti+ Integral','1 copo de Requeijão NESTLÉ® Tradicional','Sal a gosto','Pimenta do reino preta a gosto','1 pitada de noz-noscada','200ml de Creme De Leite NESTLÉ® (lata ou caixinha)','Montagem:','500 g de massa fresca de lasanha','250 g de queijo muçarela','250 g de provolone','250 g de queijo parmesão','250 g de queijo prato','1 pitada de orégano'],
        'utensílios':['Refratario','Frigideira','Tigela','Colher','Batedor'],
        'Modo de Receita':'Molho Branco:1. Em uma panela, derreta a manteiga ou margarina em fogo médio. 2.Adicione a farinha de trigo à manteiga derretida e mexa bem até formar uma mistura homogênea. 3.Em seguida, adicione o Leite Líquido NINHO Fort+ Integral à mistura, mexendo constantemente até que o molho engrosse e fique com uma textura cremosa. 4.Adicione o Requeijão NESTLÉ Tradicional e continue mexendo até incorporar completamente. 5.Tempere o molho com sal, pimenta-do-reino e a pitada de noz-moscada ralada a gosto. 6.Por fim, acrescente o Creme de Leite NESTLÉ e mexa até que o molho esteja bem misturado e reserve. Montagem: 7.Em uma forma refratária, coloque uma camada fina de molho branco no fundo da forma. 8.Em seguida, faça uma camada de massa de lasanha fresca sobre o molho branco. 9.Cubra a massa com uma porção dos queijos ralados (muçarela, provolone, parmesão e prato) temperados com o orégano, espalhando-os uniformemente. 10.Repita as camadas, alternando entre molho branco, massa de lasanha e queijos ralados, deixando a última camada de molho branco e queijos. 11.Leve ao forno pré-aquecido a 180º por cerca de 30-40 minutos. 12.Retire a lasanha do forno e deixe descansar por alguns minutos antes de servir. Corte em porções e sirva quente'
    },
    {
        'nome':'Humburger',
        'ingredientes':['1 kg de patinho moído','1 envelope de MAGGI® Creme de Cebola','1 pitada de sal','2 colheres (sopa) de páprica defumada,','50 g de bacon,','1 cebola roxa','1 tomate','1 pitada de sal','1 colher (chá) de orégano','1 colher (sopa) de cheiro-verde','100 g de queijo muçarela','6 pães de hambúrguer'],
        'Utensílios':['Tigela','Frigideira'],
        'Modo de Preparo':'1.Em um recipiente, coloque o patinho moído, adicione o MAGGI Creme de Cebola, o sal e a páprica defumada. Mexa bem para incorporar tudo e molde os hambúrgueres. Reserve. 2.Em uma frigideira, frite o bacon, e em seguida, coloque a cebola já picada. Quando a cebola estiver murcha, coloque o tomate (reserve 2 fatias para a montagem), o sal, o orégano, e continue fritando tudo. Reserve. 3.Na mesma frigideira, frite os hambúrgueres, ao seu ponto favorito, e monte os lanches. Abra o pão, coloque a salada, a carne, o bacon, o queijo, o cheiro verde e o tomate.'
    },
    {
        'nome':'Torta de calabresa',
        'ingredientes':['200 g de linguiça calabresa defumada picada','1 cebola média picada','1 tomate médio picado, sem sementes','1 colher (sopa) de cheiro-verde picado','1 pitada de pimenta-do-reino','3 ovos','1 xícara (chá) de Leite Líquido NINHO® Forti+ Integral','meia xícara (chá) de óleo','1 xícara (chá) e meia de farinha de trigo','1 colher (sopa) de amido de milho','1 colher (chá) de sal','1 colher (sopa) de fermento em pó','1 xícara (chá) de queijo muçarela ralado'],
        'utensílios':['Frigideira','Forno','Peneira','Colher de pau','Frigideira','Liquidificador','Bowl','Panela de molho','Molde retangular','Panqueca'],
        'modo de preparo':'Recheio 1.Em uma panela, leve a calabresa ao fogo médio até começar a dourar. Acrescente a cebola e refogue por mais 3 minutos. Adicione o tomate, o cheiro-verde, a pimenta-do-reino e misture bem. Desligue o fogo e deixe esfriar. Massa 2.Em um liquidificador, bata os ovos, o Leite Líquido NINHO Forti+ Integral e o óleo até ficar homogêneo. Em um recipiente, peneire a farinha de trigo com o amido de milho e o sal. Junte aos poucos a mistura do liquidificador, mexendo até formar uma massa lisa. Adicione o fermento e misture delicadamente. Montagem 3.Em uma forma retangular (30 x 20 cm), untada com óleo e polvilhada com farinha de trigo, despeje metade da massa. Distribua o recheio por cima e cubra com o restante da massa. Finalize com a muçarela ralada. 4.Leve ao forno preaquecido a 180°C por cerca de 35 minutos, ou até dourar e firmar ao toque. Deixe amornar antes de cortar.'
    }

]

@app.get("/")
def hello():
    return{"title": "Livro de Receitas"}
@app.get("/receitas/{receita}")
def get_receita(receita: str):
    for i in receitas:
        if i['nome']==receita:
            return{i['ingredientes']}