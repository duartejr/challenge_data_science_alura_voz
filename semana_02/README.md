# Semana 02 do Challenge

## Análise Exploratória da Variável Target Churn

<p align="justify"> Nesta semana o objetivo do desafio era explorar a variável Churn. Foram geradas algumas visualizões a fim de identificar as caraceterísticas principais dos clientes que deram Churn. A seguir segue o resumo dos resultados obtidos. </p>

## Qual o percentual de clientes que estamos perdendo?

<div align="center">
<img src="https://i.imgur.com/SEGzMRA.jpg" width="400px" />
</div>

<p align="justify">Nós estamos perdendo pouco mais de 1/4 dos nossos clientes. Precisamos criar campanhas para identificar o perfil dos clientes que estamos perdendo em busca de fidelizá-los.</p>

## Qual o perfil de gasto de nossos clientes?

### Gastos totais
<p align="justify"> A distribuição dos gastos totais de nossos clientes fidelizados e que evadiram é semelhante. Os clientes que evadiram tendem a terem gastos menores mas, isto pode ser devido ao curto tempo que passam conosco. </p>

<div align="center">
<img src="https://imgur.com/fAnR892.jpg" width="800px" />
</div>

### Gastos mensais

<p align="justify"> Quando consideramos a distribuição dos gastos mensais vemos que nossos clientes fidelizados tedem a ter menores gastos mensais que os clientes evadidos. Isto levanta a hipótese de que talvez nossos clientes que evadiram possam ter contratado planos mais caros que não atenderam suas expectativas. Talvez seja uma alternativa ofertar planos com melhor relação custo benefício?</p>

<div align="center">
<img src="https://imgur.com/orMtdWl.jpg" width="800px" />
</div>

## Quanto tempo nosso clientes permanecem conosco?

<p align="justify">Nós temos um bom número de clientes fidelizados com mais de 70 meses. Porém, a maioria dos nossos clientes evadidos abandonam a empresa antes de completarem 1 ano de contrato. Se conseguirmos manter nossos novos clientes por mais de 6 meses é grande a possibilidade de os fidelizarmos por um longo período. Campanhas com preços promocionais e degustação de serviços talvez possam ser estratégias para estimular a permanência de nossos clientes na empresa. </p>

<div align="center">
<img src="https://imgur.com/SpW8kaI.jpg" width="800px" />
</div>

## Qual o perfil de nossos clientes? Quais serviços mais contratatos?

<div align="left">
<img src="https://imgur.com/MtqxOVw.jpg" width="400px" />
<img src="https://imgur.com/AS78pQ5.jpg" width="400px" />
</div>

<p align="justify"> O perfil (em termos pecentuais) dos nossos clientes fidelizados e evadidos é bem semelhante. Algumas diferenças notadas foram:</p>

* Entre os clientes evadidos o público feminino é ligeiramente maior que o público masculino;
* Nossos clientes, em sua maioria, tem idade menor que 65 anos;
* Um maior percentual de clientes fidelizados não utiliza serviços de parceiros;
* O percentual de clientes sem dependentes é menor entre os clientes não fidelizados;
* O percentual de clientes que contratam algum serviço de internet é ligeiramente maior entre os clientes não fidelizados;
* A maiorias dos serviços atrelados a conexão com internet são menos populares entre os clientes não fidelizados;
* Os serviços de streaming são mais populares entre os clientes não fidelizados;
* A maioria dos clientes não fidelizados prefere fatura online.

<p align="justify">Podemos imaginar então que para fidelizar nossos clientes devamos focar nos serviços atrelados a conexão a internet. Quanto aos serviços de streaming podemos investigar quais os motivos que desagradaram os clientes e os fizeram nos deixar. </p>

## Qual o tipo de conexão com a internet de nossos clientes?

<p align="justify">A maioria dos clientes com Churn utiliza conexão por Fibra Óptica enquanto que boa parte dos nossos clientes fidelizados ainda utiliza conexão DSL. Isto justifica-se pelo fato de nossos clientes evadidos serem recentes e preferirem a conexão por fibra óptica. Talvez devamos pensar em promover a migração de nossos antigos clientes que utilizam DSL para a Fibra Óptica. </p>

<div align="left">
<img src="https://imgur.com/B1idQBl.jpg" width="400px" />
<img src="https://imgur.com/1lQzB5f.jpg" width="400px" />
</div>

## Correlação entre as variáveis

A análise a seguir será útil para a elaboração de um futuro modelo de machine learning.

<div align="left">
<img src="https://imgur.com/1lblvbc.jpg" width="800px" />
</div>

<p align="justify">A figura acima mostra um resumo da correlação entre as variáveis disponíveis sobre nossos clientes. Ela é útil para identicar a relação e possível interdependência (ainda que correlação não signifique dependência) entre as variáveis disponíveis. Variáveis altamente correlacionadas podem não ser úteis para um modelo de machine learning por representarem a mesma informação como por exemplo as variáveis: Gastos Diários e Gastos Mensais. As duas variáveis referidas têm correlação igual a 1 portanto nos trazem a mesma informação sobre nossos clientes, a forma como o os gastos diários foram calculados é uma justificativa, neste caso Gastos Diários é dependente de Gastos Mensais. A figura também mostra que os serviços de streaming são fortemente correlacionados com os gastos dos clientes, portanto estes podem ser os serviços de maiores custos. Talvez o custo elevado dos serviços de streaming seja uma possível causa da evasão de nossos clientes. </p>

## Aplicativo

<p style='text-align: justify'>A seguir pode ser acessado um aplicativo onde pode-se avaliar de forma interativa a relação entre todas as variáveis disponíveis sobre nossos clientes.</p>

[APLICATIVO EDA ALURAVOZ](https://share.streamlit.io/duartejr/challenge_data_science_alura_voz/main/semana_02/app_semana02.py)

## Conclusão

<p align='justify'> Conseguimos entender o perfil geral de nossos clientes e possíveis causas do Churn. O nível de churn que temos (superior a 25%) é considerável e precisamos tomar ações para diminuirmos esta taxa. Como o perfil dos clientes com churn e sem churn é muito parecido fica difícil de identificarmos, manualmente, todas as combinações possíveis que podem estimular nossos clientes a evadirem. Assim, precisamos investir em um modelo de Machine Learning que possa avaliar as relações mais complexas entre as variáveis que temos para identificar clientes que potencialmente irão evadir da empresa.</p>
