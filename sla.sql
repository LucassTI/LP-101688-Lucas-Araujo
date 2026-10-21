create database loja ; -- Comando par acriar o banco d dados
use loja; -- comando para usr o banco de dados

create table Clientes (
idcliente int primary key auto_increment,
nome varchar(100) not null,
email varchar(100),
cidade varchar (45) not null
);