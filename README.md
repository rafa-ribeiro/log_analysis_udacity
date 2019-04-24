# Projeto de Análise de Logs

Este é o projeto 'Análise de Logs' do módulo 2 do curso Full-Stack Developer da Udacity.

O projeto tem como missão criar uma aplicação Python para extração de dados de um banco de dados relacional, Postgresql.
A aplicação conecta-se ao banco de dados fornecido pela Udacity e visa responder as questões abaixo:

1. Quais são os três artigos mais populares de todos os tempos? 
2. Quem são os autores de artigos mais populares de todos os tempos?
3. Em quais dias mais de 1% das requisições resultaram em erros?


## Pré-requisitos do projeto:                
Para execução da aplicação é necessário atender aos seguintes requisitos:

- Baixar a máquina virtual fornecida pela Udacity que contém o ambiente Python necessário para execução da aplicação junto com o banco de dados Postgresql.
- Importar os dados também fornecido pela Udacity no banco de dados.
- Criar no banco de dados as views descritas no arquivo 'log_analysis_views.sql'.


## Execução
Para execução do projeto basta executar o comando abaixo dentro da máquina virtual:

| python log_application.py


## Fontes consultadas:
- https://www.python.org/dev/peps/pep-0008/
- https://wiki.postgresql.org/wiki/Psycopg2_Tutorial