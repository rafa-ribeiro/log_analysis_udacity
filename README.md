# Projeto de Análise de Logs

Este é o projeto 'Análise de Logs' do módulo 2 do curso Full-Stack Developer da Udacity.

O projeto tem como missão criar uma aplicação Python para extração de dados de um banco de dados relacional, Postgresql.
A aplicação conecta-se ao banco de dados fornecido pela Udacity e visa responder as questões abaixo:

1. Quais são os três artigos mais populares de todos os tempos? 
2. Quem são os autores de artigos mais populares de todos os tempos?
3. Em quais dias mais de 1% das requisições resultaram em erros?


## Pré-requisitos do projeto:                
Para execução da aplicação é necessário efetuar o download/instalação dos seguintes itens:

- VirtualBox: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
- Vagrant: https://www.vagrantup.com/downloads.html
- Arquivos de configuração da VM: https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
- Massa de dados para execução da aplicação: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 

A aplicação roda dentro de uma máquina virtual que contém o ambiente Python necessário para sua execução juntamente com a instalação do banco de dados Postgresql. Para isso, é necessário efetuar os passos abaixo:

1. Instalar as ferramentas VirtualBox e Vagrant.

2. Efetuar o download dos arquivos de configuração da VM:
- Extraia o arquivo baixado 'fsnd-virtual-machine.zip'. Ao extrair, você terá o diretório '../fsnd-virtual-machine/FSND-Virtual-Machine' e nele há o diretório 'vagrant'. Nesse diretório existe um arquivo chamado 'Vagrantfile' que descreve todas as dependências necessárias para a criação da VM. Ele pode descrever, por exemplo, o sistema operacional da VM, a versão do ambiente Python utilizada, as libs que esse ambiente deverá conter, a criação do banco de dados, entre outros.

3. Para criar a VM, estando dentro do diretório 'vagrant', execute o comando: 

| vagrant up

Obs: Esse processo pode demorar alguns minutos na primeira vez em que for executado devido ao download das dependências da VM.

4. Em caso de sucesso do comando acima, sua VM já estará em execução, portanto execute o comando abaixo para entrar na VM:

| vagrant ssh

- Dentro da VM, o diretório 'vagrant' que citamos anteriormente, é compartilhado entre seu SO e a VM, portanto o diretório pode ser acessado com:

| cd /vagrant/

5. Como o diretório 'vagrant' é compartilhado, copie para ele o arquivo de massa de dados da aplicação, o arquivo newsdata.zip e o descompacte. Ao descompactar, você terá o arquivo 'newsdata.sql'. Esse arquivo contém a criação das estruturas das tabelas utilizadas pela aplicação mais uma massa de dados para execução da aplicação. Use o comando abaixo para carregar os dados no Postgresql:

| psql -d news -f newsdata.sql

- Com a estrutura e os dados carregados no banco de dados, é necessário conectar-se ao banco para executar a criação das views. Utilize o comando abaixo para conectar-se ao banco:

| psql -d news

- Uma vez conectado ao banco, execute o conteúdo do arquivo 'log_analysis_views.sql' para a criação das Views utilizadas na aplicação de Análise de Logs. Copie o conteúdo do arquivo e tecle 'Enter'. Para cada view criada, será retornada a mensagem 'CREATE VIEW'. 


## Execução
Para execução do projeto, coloque-o dentro do diretório 'vagrant' que é compartilhado entre o SO e a VM e, estando dentro da VM, execute o comando abaixo:

| python log_application.py


## Fontes consultadas:
- https://www.python.org/dev/peps/pep-0008/
- https://wiki.postgresql.org/wiki/Psycopg2_Tutorial