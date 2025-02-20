create table continente(
	id_con int primary key auto_increment,
    nome_con varchar(50) not null);
create table país(
	id_p int primary key auto_increment,
    nome_p varchar(50) not null,
    id_con int);
create table estado(
	id_e int primary key auto_increment,
	nome_e varchar(50) not null,
    id_p int not null);
create table cidade(
	id_c int primary key auto_increment,
    nome_c varchar(50) not null,
    id_e int not null);
create table bairro(
	id_b int primary key auto_increment,
    nome_b varchar(50) not null,
    id_c int not null);
create table rua(
	id_r int primary key auto_increment,
    nome_r varchar(50) not null,
    id_b int not null);
describe cidade;
alter table país add foreign key (id_con) references continente(id_con);
alter table estado add foreign key (id_p) references país(id_p);
alter table cidade add foreign key (id_e) references estado(id_e);
alter table bairro add foreign key (id_c) references cidade(id_c);
alter table rua add foreign key (id_b) references bairro(id_b);

insert into continente (id_con, nome_con) values 
	(null, "America"),
    (null, "Europa"),
    (null, "Oceania"),
    (null, "Ásia"),
    (null, "Africa");
insert into país (id_p, nome_p, id_con) values
	(null, "Brasil", 1),
    (null, "Chile", 1),
    (null, "Suriname", 1),
    (null, "Reino Unido", 2),
    (null, "França", 2),
    (null, "Irlanda", 2),
    (null, "Nova Zelândia", 3),
    (null, "Indonêsia", 3),
    (null, "Austrália", 3),
    (null, "Japão", 4),
    (null, "Coreia do Sul", 4),
    (null, "Russia", 4),
    (null, "Angola", 5),
    (null, "Marrocos", 5),
    (null, "Cabo verde", 5);
insert into estado (id_e, nome_e, id_p) values 
	(null, "Mato Grosso do Sul", 1),
    (null, "Rio de Janeiro", 1),
    (null, "Santiago", 2),
    (null, "Valparaíso", 2),
    (null, "Paramaribo", 3),
    (null, "Marowijne", 3),
    (null, "Inglaterra", 4),
    (null, "Escócia", 4),
    (null, "Île-de-France", 5),
    (null, "Provence-Alpes-Côte d'Azur", 5),
    (null, "Leinster", 6),
    (null, "Ulster", 6),
    (null, "Auckland", 7),
    (null, "Canterbury", 7),
    (null, "Java  Ocidental", 8),
    (null, "Bali", 8 ),
    (null, "Nova Gales do Sul", 9),
    (null, "Queensland", 9),
    (null, "Tóquio", 10),
    (null, "Osaka", 10),
    (null, "Gyeonggi-do", 11),
    (null, "Jeollanam-do", 11),
    (null, "Moscovo", 12),
    (null, "Tartaristão", 12),
    (null, "Luanda", 13),
    (null, "Benguela", 13),
    (null, "Rabat-Salé-Kénitra", 14),
    (null, "Marrakech-Safi", 14),
    (null, "Ilhas de Barlavento", 15),
    (null, "Ilhas de Sotavento", 15);
select * from estado;
insert into cidade (id_c, nome_c, id_e) values
	(null, "Campo Grande", 1),
    (null, "Rio de Janeiro", 2),
    (null, "Santiago", 3),
    (null, "Valparaíso", 4),
    (null, "Paramaribo", 5),
    (null, "Albina", 6),
    (null, "Londres", 7),
    (null, "Portree", 8),
    (null, "Paris", 9),
    (null, "Marselha", 10),
    (null, "Dublin", 11),
    (null, "Belfast", 12),
    (null, "Auckland", 13),
    (null, "Chirstchurch", 14),
    (null, "Bandung", 15),
    (null, "Denpasar", 16),
    (null, "Sydney", 17),
    (null, "Brisbane", 18),
    (null, "Tóquio", 19),
    (null, "Osaka", 20),
    (null, "Seul", 21),
    (null, "Suncheon", 22),
    (null, "Moscou", 23),
    (null, "Kazan", 24),
    (null, 'Launda', 25),
    (null, 'Condado de Muan', 26),
    (null, 'Rabat', 27),
    (null, 'Safim', 28),
    (null, 'São Jorge', 29),
    (null, 'Pedra Badejo', 30);
select * from cidade;
insert into cidade (id_b, nome_b, id_c) values 
	(null, 