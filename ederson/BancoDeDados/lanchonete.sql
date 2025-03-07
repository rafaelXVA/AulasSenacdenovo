select * from teste;
describe teste;
create database funcionario;
use funcionario;
create table teste(
	id_funcionario int primary key auto_increment,
    nome varchar(50) not null,
    cpf varchar(15) not null,
    sexo int not null,
    endereco varchar(50) not null,
    telefone varchar(20) not null,
    nascimento date not null,
    usuario varchar(20) not null,
    senha varchar(30) not null);