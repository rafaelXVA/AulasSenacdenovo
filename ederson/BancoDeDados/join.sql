create database clientes;
use clientes;


create table cliente (
	id_cliente int primary key auto_increment,
    nome varchar(50) not null,
    cpf varchar(15),
    rg varchar(15),
    id_cidade int not null,
    id_sexo int not null,
    id_nacionalidade int not null,
    fone varchar(20),
    id_raca int not null,
    id_escolaridade int not null);

create table estado(
	id_estado int primary key auto_increment,
    estado varchar(40) not null);

create table cidade(
	id_cidade int primary key auto_increment,
    cidade varchar(50) not null,
    id_estado int not null);
create table sexo(
	id_sexo int primary key auto_increment,
    sexo varcharacter(1));

create table nacionalidade(
	id_nacionalidade int primary key auto_increment,
    nacionalidade varchar(50));

create table raca(
	id_raca int primary key auto_increment,
    raca varchar(10) not null);
    
create table escolaridade(
	id_escolaridade int primary key auto_increment,
    escolaridade varchar(50));
    
alter table cidade add foreign key (id_estado) references estado(id_estado);
alter table cliente add foreign key (id_cidade) references cidade(id_cidade);
alter table cliente add foreign key (id_sexo) references sexo(id_sexo);
alter table cliente add foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade);
alter table cliente add foreign key (id_raca) references raca(id_raca);
alter table cliente add foreign key (id_escolaridade) references escolaridade(id_escolaridade);

insert into estado (id_estado, estado) values 
	(null, 'Mato Grosso do Sul'),
    (null, 'Mato Grosso'),
    (null, 'Rondônia'),
    (null, 'Amazonas'),
    (null, 'Acrê'),
    (null, 'Amapá'),
    (null, 'Roraima'),
    (null, 'Pará'),
    (null, 'Maranhão'),
    (null, 'Tocantins'),
    (null, 'Pernambuco'),
    (null, 'Paraíba'),
    (null, 'Piauí'),
    (null, 'Ceará'),
    (null, 'Rio Grande do Norte'),
    (null, 'Alagoas'),
    (null, 'Sergipe'),
    (null, 'Bahia'),
    (null, 'Goiás'),
    (null, 'Espírito Santo'),
    (null, 'Rio de Janeiro'),
    (null, 'São Paulo'),
    (null, 'Paraná'),
    (null, 'Santa Catarina'),
    (null, 'Rio Grande do Sul');
select * from estado;
insert into cidade (id_cidade, cidade, id_estado) values
	(null, 'Campo Grande', 1),
    (null, 'Camapuã', 1),
    (null, 'Corguinho', 1),
    (null, 'Bataguassu', 1),
    (null, 'Dourados', 1),
    (null, 'Arapongas', 23),
    (null, 'Curitiba', 23),
    (null, 'Maringá', 23),
    (null, 'Cascavel', 23),
    (null, 'Londrina',23),
    (null, 'São Paulo', 22),
    (null, 'Guarulhos', 22),
    (null, 'Olímpia', 22),
    (null, 'Itapevi', 22),
    (null, 'Campinas', 22),
    (null, 'General Câmara', 25),
    (null, 'Porto Alegre', 25),
    (null, 'Pelotas', 25), 
    (null, 'Gramado', 25),
    (null, 'Progresso', 25),
    (null, 'Florianópolis', 24),
    (null, 'Laguna', 24),
    (null, 'Bombinhas', 24),
    (null, 'Balneário Camboriú', 24),
    (null, 'Blumenau', 24),
	(null, 'Uberlândia', 26),
    (null, 'Belo Horizonte', 26),
    (null, 'Ipatinga', 26),
    (null, 'Araxá', 26),
    (null, 'Araguari', 26),
    (null, 'Rio de Janeiro', 21),
    (null, 'Saquarema', 21),
    (null, 'Angra dos Reis', 21),
    (null, 'Pontal', 21),
    (null, 'Volta Redonda', 21),
    (null, 'Linhares', 20),
    (null, 'Serra', 20),
    (null, 'Vitória', 20),
    (null, 'Pancas', 20),
    (null, 'Guarapari', 20),
    (null, 'Salvador', 18),
    (null, 'Feira de Santana', 18),
    (null, 'Porto Seguro', 18),
    (null, 'Ilhéus', 18),
    (null, 'Itapé', 18),
    (null, 'Goiânia', 19),
    (null, 'Anápolis', 19),
    (null, 'Trindade', 19),
    (null, 'Cristalina', 19),
    (null, 'Goianira', 19),
    (null, 'Brasília', 27),
    (null, 'Planaltina', 27),
    (null, 'Rajadinha', 27),
    (null, 'Boa Vista', 27),
    (null, 'Capão Seco', 27),
    (null, 'Cuiabá', 2),
    (null, 'Várzea Grande', 2),
    (null, 'Abolição', 2),
    (null, 'Guia', 2),
    (null, 'Barracão', 2),
    (null, 'Porto Velhos', 3),
    (null, 'Candeias do Jamari', 3),
    (null, 'Belmont', 3),
    (null, 'Teotônio', 3),
    (null, 'São Carlos', 3),
    (null, 'Manaus', 4),
    (null, 'Nova Esperança', 4),
    (null, 'Tobocal', 4),
    (null, 'Amatari', 4),
    (null, 'Nova Olinda do Norte', 4),
    (null, 'Porto Walter', 5),
    (null, 'Jordão', 5),
    (null, 'Feijó', 5),
    (null, 'Manoel Urbano', 5),
    (null, 'Assis Brasil', 5),
    (null, 'Boa Vista', 7),
    (null, 'Iracema', 7),
    (null, 'Mujaca', 7),
    (null, 'Cantá', 7),
    (null, 'Santa Rita', 7),
    (null, 'Palmas', 8),
    (null, 'Queima', 8),
    (null, 'Cabeceiras', 8),
    (null, 'Taquaruçu', 8),
    (null, 'Belém', 8),
    (null, 'Macapá', 6),
    (null, 'Maruanun', 6),
    (null, 'Maracá', 6),
    (null, 'Santana', 6),
    (null, 'Carmo', 6),
    (null, 'São Luís', 9),
    (null, 'Raposa', 9),
    (null, 'Icatu', 9),
    (null, 'Alcântra', 9),
    (null, 'Rosário', 9),
    (null, 'Fortaleza', 14),
    (null, 'Maracanaú', 14),
    (null, 'Caucaia', 14),
    (null, 'Maranguape', 14),
    (null, 'Canindé', 14),
    (null, 'Teresina', 13),
    (null, 'Parnaíba', 13),
    (null, 'Picos', 13),
    (null, 'Floriano', 13),
    (null, 'Oeiras', 13),
    (null, 'Aracaju', 17),
    (null, 'Nossa Senhora do Socorro', 17),
    (null, 'Lagarto', 17),
    (null, 'Itabaiana', 17),
    (null, 'Estância', 17),
    (null, 'Natal', 15),
    (null, 'Mossoró', 15),
    (null, 'Parnamirim', 15),
    (null, 'Caicó', 15),
    (null, 'Currais Novas', 15),
    (null, 'João Pessoa', 12),
    (null, 'Campina Grande', 12),
    (null, 'Patos', 12),
    (null, 'Bayeux', 12),
    (null, 'Sousa', 12),
    (null, 'Recife', 11),
    (null, 'Olinda', 11),
    (null, 'Caruaru', 11),
    (null, 'Petrolina', 11),
    (null, 'Cabo de Santo Agostinho', 11),
    (null, 'Maceió', 16),
    (null, 'Arapiraca', 16),
    (null, 'Palmeira dos Índios', 16),
    (null, 'Rio Largo', 16),
    (null, 'Delmiro Gouveia', 16);
insert into sexo (id_sexo, sexo) values
	(null, 'Masculino'),
    (null, 'Feminino'),
    (null, 'Não-Binário');
insert into nacionalidade (id_nacionalidade, nacionalidade) values
	(null, 'Brasileiro'),
    (null, 'Estrangeiro');
insert into raca (id_raca, raca) values 
	(null, 'Pardo'),
    (null, 'Branco'),
    (null, 'Ásiatico'),
    (null, 'Preto'),
    (null, 'Índigena');
insert into escolaridade (id_escolaridade, escolaridade) values
	(null, 'Fundamental Inc'),
    (null, 'Fundamental Comp'),
    (null, 'Médio Inc'),
    (null, 'Médio Comp'),
    (null, 'Superior Inc'),
    (null, 'Superior Comp'),
    (null, 'Mestre'),
    (null, 'Doutor');

select * from cidade;
select * from cliente;
	
insert into cliente (id_cliente, nome, cpf, rg, id_cidade, id_sexo, id_nacionalidade, fone, id_raca, id_escolaridade) values
(NULL, 'João da Silva', '123.456.789-00', '12.345.678', 45, 1, 1, '(11) 98765-4321', 1, 3),
(NULL, 'Maria Oliveira', '234.567.890-11', '23.456.789', 102, 2, 2, '(21) 99876-5432', 2, 4),
(NULL, 'Carlos Eduardo Santos', '345.678.901-22', '34.567.890', 67, 1, 1, '(31) 91234-5678', 3, 5),
(NULL, 'Ana Beatriz Costa', '456.789.012-33', '45.678.901', 88, 2, 2, '(41) 92345-6789', 1, 6),
(NULL, 'Felipe Pereira', '567.890.123-44', '56.789.012', 55, 1, 1, '(51) 93456-7890', 2, 2),
(NULL, 'Juliana Martins', '678.901.234-55', '67.890.123', 120, 2, 2, '(61) 94567-8901', 3, 4),
(NULL, 'Ricardo Almeida', '789.012.345-66', '78.901.234', 30, 2, 1, '(71) 95678-9012', 1, 3),
(NULL, 'Fernanda Lima', '890.123.456-77', '89.012.345', 115, 1, 2, '(81) 96789-0123', 2, 5),
(NULL, 'Lucas Souza', '901.234.567-88', '90.123.456', 48, 3, 1, '(91) 97890-1234', 3, 6),
(NULL, 'Patrícia Rocha', '012.345.678-99', '01.234.567', 25, 1, 2, '(11) 98901-2345', 1, 4),
(NULL, 'André Oliveira', '123.456.789-01', '12.345.678', 107, 2, 1, '(21) 99012-3456', 2, 2),
(NULL, 'Isabela Santos', '234.567.890-12', '23.456.789', 77, 1, 1, '(31) 91234-5678', 3, 5),
(NULL, 'Tiago Ferreira', '345.678.901-23', '34.567.890', 92, 2, 2, '(41) 92345-6789', 1, 6),
(NULL, 'Juliana Costa', '456.789.012-34', '45.678.901', 64, 3, 1, '(51) 93456-7890', 2, 3),
(NULL, 'Roberto Alves', '567.890.123-45', '56.789.012', 101, 1, 2, '(61) 94567-8901', 3, 4),
(NULL, 'Gabriela Martins', '678.901.234-56', '67.890.123', 19, 2, 1, '(71) 95678-9012', 1, 2),
(NULL, 'Vitor Costa', '789.012.345-67', '78.901.234', 82, 1, 2, '(81) 96789-0123', 2, 5),
(NULL, 'Lúcia Oliveira', '890.123.456-78', '89.012.345', 110, 2, 1, '(91) 97890-1234', 3, 6),
(NULL, 'Eduardo Lima', '901.234.567-89', '90.123.456', 36, 3, 2, '(11) 98901-2345', 1, 4),
(NULL, 'Marta Almeida', '012.345.678-00', '01.234.567', 79, 1, 1, '(21) 99012-3456', 2, 3);
select * from cliente;
select * from cidade;
select * from estado;

select cliente.nome, cidade.cidade
from cliente
inner join cidade
on cliente.id_cidade=cidade.id_cidade;
describe cidade;



select cliente.nome, estado.estado
from cliente
inner join cidade
on cliente.id_cidade=cidade.id_cidade
join estado
on cidade.id_estado=estado.id_estado;

select cliente.nome, cliente.cpf, raca.raca
from cliente
inner join raca
on cliente.id_raca=raca.id_raca;

select cliente.nome, nacionalidade.nacionalidade
from cliente
inner join nacionalidade
on cliente.id_nacionalidade=nacionalidade.id_nacionalidade;

select cliente.nome, escolaridade.escolaridade
from cliente
inner join escolaridade
on cliente.id_escolaridade=escolaridade.id_escolaridade;

select cliente.nome, cidade.cidade, estado.estado
from cliente
inner join cidade
on cliente.id_cidade=cidade.id_cidade
inner join estado
on cidade.id_estado=estado.id_estado;

select cliente.nome, cidade.cidade, estado.estado, cliente.fone, cliente.rg, sexo.sexo, raca.raca, escolaridade.escolaridade
from cliente
inner join cidade
on cliente.id_cidade=cidade.id_cidade
inner join estado
on estado.id_estado=cidade.id_estado
inner join sexo
on cliente.id_sexo=sexo.id_sexo
inner join raca
on cliente.id_raca=raca.id_raca
inner join escolaridade
on cliente.id_escolaridade=escolaridade.id_escolaridade;