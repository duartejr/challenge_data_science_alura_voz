# Alura Voz - Challenge de Data Science

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

Primeiro Challenge de Data Science da Alura

* [Base De Dados Original](https://raw.githubusercontent.com/sthemonica/alura-voz/main/Dados/Telco-Customer-Churn.json)
* [Dicionário de Dados Original](https://github.com/sthemonica/alura-voz/blob/main/dicionario.md)

## Índice 

* [Objetivo](#objetivo)
* [Semana 1 do Challenge](#semana-1-do-Challenge)
* [Semana 2 do Challenge](#semana-2-do-Challenge)
* [ Semana 3 do Challenge](#semana-3-do-Challenge)
* [Semana 4 do Challenge](#semana-4-do-Challenge)

# Objetivo

<p align='justify'>Na reunião inicial com as pessoas responsáveis pela área de vendas da empresa, foi explicada a importância de se reduzir a Taxa de Evasão de Clientes, conhecido como Churn Rate. Basicamente, o Churn Rate indica o quanto a empresa perdeu de receita ou clientes em um período de tempo.</p>
<p align='justify'> Como cientista de dados da operadora de telecomunicações Alura Voz sugeri, como passo inicial, a identificação de clientes que teriam uma maior chance de deixar a empresa. Para isso, seria necessário investigar algumas características de clientes ou dos planos de clientes para tentar classificar estas pessoas como potenciais candidatas a deixar a empresa ou não.</p>
<p align='justify'> Portanto soliciteu o conjunto de dados para começar a explorar, tratar e modelar a partir de agora. Em seguida, o foco será na otimização de cada um dos modelos com a finalidade de obter o melhor resultado para a tomada de decisão da Alura Voz. </p>

# Semana 1 do Challenge

<p align='justify'> Na primeira semana do Challenge foi feita a entrega da base de dados, obtidada por meio de API, dos clientes da AluraVoz. O dataset fornecido contém, em sua maioria, dados categóricos. Também há variáveis numéricas referentes aos gastos dos clientes e o tempo de contrato. Foram encontradas as seguintes inconsistência nos dados: preenchimento de dados números como string, células em branco e coluna referente a senioridade estava prenchida com valores numéricos enquanto deveria estar com valores de texto. Também havia registros sem a informaçã de churn do cliente. Tais incosistências foram removidas com: remoção dos registros sem informação de churn, conversão de valores do tipo string para float, padrozinação da coluna de senioridade. Também foi realizada a tradução dos dados que originalmente estavam em inglês. Fez-se ainda a estimativa do gasto médio diário dos clientes.

- [Notebook da Primeira Semana](https://github.com/duartejr/challenge_data_science_alura_voz/blob/main/semana_01/semana_1_explorando_dados.ipynb)
- [Dicionário de Dados Atualizado](https://github.com/duartejr/challenge_data_science_alura_voz/blob/main/dados/novo_dicionario_dados.md)

# Semana 2 do Challenge

<p align='justify'>Nesta semana o objetivo era analisar a variável Churn. Foi verificada a distribuição da variável churn, e geradas visualizações que facilitem a intepretação do comportamento dos clientes. Traçou-se o perfil médio dos clientes que evadem da empresa, descobrindo-se que a maioria evade da empresa antes de completar 1 ano de contrato. Também é comum ao clientes evadidos o contrato de serviço de internet por fibra óptica e assinatura de pacotes de streaming. Várias visualizações foram geradas e um relatório construídos para descrever o perfil dos clientes da empresa para a equipe de Vendas.</p>

- [Resultados da Segunda Semana](https://github.com/duartejr/challenge_data_science_alura_voz/tree/main/semana_02)
- [Notebook da Segunda Semana](https://github.com/duartejr/challenge_data_science_alura_voz/blob/main/semana_02/semana_2_analise_variavel_churn.ipynb)


# Semana 3 do Challenge

Nesta semana foi feita a construção de um modelo de Machine Learning para identificação de clientes potenciais a saírem da empresa.</br>
Foram testados os seguintes modelos: Random Forest, AdaBoost, Regressão Logística, Naive Bayes, KNN e Suport Vector Machine.</br>
<p aligh='justify'>A análise exploratória dos dados, feita na etapa anterior, permitiu a redução de dimensionalidade e consequentemente a complexidade do mmodelo. Utilizando-se a técnica de undersampling consegui equilibrar as classes, assim diminuiu-se a probabilidade do modelo tornar-se tendencioso para uma determinada classe. Todos os modelos testador obtiveram resultados próximos de acurácia, apenas o KNN ficou mais distante dos demais. O modelo de AdaBoost destacouse por ser o de melhor desempenho tanto em recall (0,813) e Acurácia (0,766). Após aplicar-se técnicas de otimização pode-se obter um pequeno incremento no recall do AdaBoost (0,816). Talvez possa-se ter um incremento maior na performance do modelo mas limitações de hardware não permitiram testar esta hípotese. Ao utilizar os dados sem realizar técnica de balanceamento a acurácia foi bem elevada (0,803), porém, este resultado alto deve ao próprio desbalanceamento dos dados que faz o modelo tender a jogar mais valores para a classe dominante. Com a técnica de OverSampling, neste caso, foram obtidos resultados próximos aos do uso de Undersampling. Contudo, a técncia de oversampling deve ser utilizada com cuidado pois, quando o desbalanceamento entre as classes é muito grande, a quantidade de valores sintéticos pode comprometer as análises.</p>

- [Notebook da Terceira Semana](https://github.com/duartejr/challenge_data_science_alura_voz/blob/main/semana_03/semana_3_analise_machine_learning.ipynb)

# Semana 4 do Challenge

:construction: Em construção :construction:

