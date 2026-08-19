# Pricing & Sales Manager

Projeto de portfólio inspirado em uma solução operacional real de precificação e análise comercial criada para um pequeno negócio. A versão original contém receitas, preços e dados comerciais privados; por isso, este repositório publica apenas uma reconstrução genérica com dados fictícios.

## O problema

Pequenos negócios frequentemente controlam custos de ingredientes, rendimento de produtos, margem, preços e vendas em arquivos separados. Isso dificulta responder perguntas simples: quanto custa produzir cada item, qual preço preserva a margem desejada, quais canais vendem melhor e quais produtos geram mais lucro?

## O que a solução automatiza

- Cadastro centralizado de insumos e custo por unidade de medida.
- Estrutura de receitas e componentes reutilizáveis.
- Cálculo de custo do lote, rendimento e custo unitário.
- Precificação por margem-alvo e taxa do canal de venda.
- Comparação entre preço sugerido e preço praticado.
- Registro de vendas em múltiplos canais.
- Cálculo automático de faturamento, custo e lucro.
- Dashboard com volume vendido, receita, custo, lucro e margem.
- Comparação de desempenho por canal e por produto.
- Evolução mensal de receita e lucro.

## Demo pública

O arquivo [`demo/small-business-pricing-manager-demo.xlsx`](demo/small-business-pricing-manager-demo.xlsx) reproduz a lógica do projeto com produtos, canais e valores totalmente fictícios. Ele foi criado para demonstrar a modelagem sem revelar informações do negócio que originou o case.

### Estrutura da demo

| Aba | Finalidade |
|---|---|
| Config | Margem-alvo e parâmetros comerciais |
| Ingredients | Base de insumos e custo unitário |
| Recipes | Composição, rendimento e custo de produção |
| Pricing | Preço sugerido, preço praticado e margem |
| Sales | Registro consolidado de vendas por canal |
| Dashboard | KPIs e comparações comerciais |

## Validação em Python

O protótipo Python do repositório carrega a própria demo pública e verifica se a estrutura esperada está presente.

```bash
git clone https://github.com/GabrielSantanaBR/bakery-manager.git
cd bakery-manager
pip install -r requirements.txt
python main.py
```

O comando valida as seis abas principais e mostra quantas linhas não vazias existem em cada módulo operacional.

## Competências demonstradas

- Modelagem de dados em planilhas
- Excel avançado e fórmulas encadeadas
- Automação de cálculos
- Análise de custos e precificação
- Business intelligence para pequenos negócios
- Criação de dashboards
- Normalização de dados operacionais
- Integração entre Excel e Python/Pandas
- Transformação de uma necessidade real em ferramenta utilizável

## Evolução do projeto

A planilha é o artefato mais maduro do case. O código Python representa a etapa inicial de uma migração gradual da lógica operacional para uma aplicação, começando pela leitura e validação estruturada dos dados.

## Privacidade

Nenhuma receita real, lista de clientes, preço interno, volume de vendas ou identidade visual do negócio original é publicada neste repositório.

## Autor

Gabriel Santana — Software, Dados e Automação.
