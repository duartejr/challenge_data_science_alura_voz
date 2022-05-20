# Semana 02 do Challenge

## Análise Exploratória da Variável Targe Churn

Nesta semana o objetivo do desafio era explorar a variável Churn. Foram geradas algumas visualizões a fim de identificar as caraceterísticas principais dos clientes que deram Churn. A seguir segume o resumo dos resultados obtidos.

## Qual o percentual de clientes que estamos perdendo?

<div align="center">
<img src="https://i.imgur.com/SEGzMRA.jpg" width="400px" />
</div>

Nós estamos perdendo pouca mais de 1/4 dos nossos clientes. Precisamos criar campanhas para identificar o perfil dos clientes que estamos perdendo em busca de fidelizá-los.

## Qual o perfil de gasto de nossos clientes?

### Gastos totais
A distribuição dos gastos totais de nossos clientes fidelizados e que evadiram é semelhante. Os clientes que evadiram tendem a terem gastos menores mas isto pode ser devido ao curto tempo que passam conosco.

<div align="center">
<img src="https://imgur.com/fAnR892.jpg" width="800px" />
</div>

### Gastos mensais

Quando consideramos a distribuição dos gastos mensais vemos que nossos clientes fidelizados tedem a terem menores gastos mensais que os clientes evadidos. Isto levanta a hipótese de que talvez nossos clientes que evadiram possam ter contratados planos mais caros que não atenderam suas expectativas. Talvez seja uma alternativa buscar planos com melhor relação custo benefício?

<div align="center">
<img src="https://imgur.com/orMtdWl.jpg" width="800px" />
</div>

## Quanto tempo nosso clientes permanecem conosco?

Nos temos um bom número de clientes fidelizados com mais de 70 meses. Porém, a maioria dos nossos clientes evadidos abandonam a empresa antes de completarem 1 ano de contrato. Se conseguirmos manter nossos novos clientes por mais de 6 meses é grande a possibilidade de os fidelizarmos por um longo período. Campanhas de preços promocionais e degustação de serviços talvez possam ser estratégias para estimular a permanência de nossos clientes na empresa.

<div align="center">
<img src="https://imgur.com/SpW8kaI.jpg" width="800px" />
</div>

## Qual o perfil de nossos clientes? Quais serviços mais contratatos?

<div align="left">
<img src="https://imgur.com/MtqxOVw.jpg" width="400px" />
<img src="https://imgur.com/AS78pQ5.jpg" width="400px" />
</div>

O perfil (em termos pecentuais) dos nossos clientes fidelizados e evadidos é bem semelhante. Algumas diferenças notadas são:

* Entre os clientes evadidos o público feminino é ligeiramente maior que o público masculino;
* Nossos clientes em sua maiores tem idade menor que 65 anos;
* O maior percentual de clientes fidelizados não utiliza serviços de parceiros;
* O percentual de clientes sem dependentes é menor entre os não clientes não fidelizados;
* O percentual de clientes que utilizam algum serviço de internet é ligeiramente entre os clientes não fidelizados;
* A maiorias dos serviços atrelados a conexão com internet são menos populares entre os clientes não fidelizados;
* Os serviços de streaming são mais populares entre os clientes não fidelizados;
* A maioria dos clientes não fidelizado prefere fatura online.

Podemos imaginar então que para fidelizar nossos clientes devamos focar nos serviços atrelados a conexão a internet. Quanto aos serviços de streaming podemos investigar quais os motivos que desagradaram os clientes e os fizeram nos deixar.

## Qual o tipo de conexão com a internet de nossos clientes?

A maioria dos clientes com Churn utiliza conexão por Fibra Óptica enquanto que boa parte dos nossos clientes fidelizados ainda utiliza conexão DSL. Isto justifica-se pelo fato de nossos clientes evadidos serem recentes e preferem a conexão por fibra óptica. Talvez devamos pensar em promover a migração de nossos antigos clientes que utilizam DSL para a Fibra Óptica.

<div align="left">
<img src="https://imgur.com/B1idQBl.jpg" width="400px" />
<img src="https://imgur.com/1lQzB5f.jpg" width="400px" />
</div>

## Correlação entre as variáveis

A análise a seguir será útil para a elaboração de um futuro modelo de machine learning.

<div align="left">
<img src="https://imgur.com/1lblvbc.jpg" width="800px" />
</div>

A figura acima mostra um resumo da correlação entre as variáveis disponíveis sobre nossos clientes. Ela é útil para identicar a relação e possível interdepencia (ainda que correlação não signifique dependência) entre as variáveis disponíveis. Variáveis altamente correlacionadas podem não ser úteis para um modelo de machine learning por representarem a mesma informação como por exemplo as variáveis: Gastos Diários e Gastos Mensais. As duas variáveis referidas têm correlação igual a 1 portanto nos trazem a mesma informação sobre nossos clientes, a forma como o os gastos diários foram calculados é uma justificativa, neste caso Gastos Diários é dependente de Gastos Mensais. A figura também mostra que os serviços de streaming são fortemente correlacionados com os gastos dos clientes, portanto estes podem ser os serviços de maiores custos. Talvez o custo elevados dos serviços de streaming seja uma possível causa da evasão de nossos clientes. 

## Aplicativo

A seguir pode ser acessado um aplicativo onde pode-se avaliar de forma interativa a relação entre todas as variáveis disponíveis sobre nossos clientes.
