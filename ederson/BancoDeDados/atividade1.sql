create database atividade1;
use atividade1;

create table departamento (
	idDepartamento int auto_increment primary key,
    nome varchar(30) not null,
    telefone int not null,
    centro int not null);
create table aluno (
	idAluno int auto_increment primary key,
	nome varchar(30) not null,
    cpf int not null,
    rua varchar(30) not null,
    cidade varchar(30) not null,
    cep int not null,
    telefone_fixo int not null,
    telefone_celular int not null,
    dataNasc date not null,
    departamento int not null,
    curso int);
    
create table curso (