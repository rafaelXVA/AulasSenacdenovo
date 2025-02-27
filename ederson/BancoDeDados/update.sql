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
    id_escolaridade int not null,
    id_estadocivil int not null,
    idade int not null);
    
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
    
create table estadocivil(
	id_estadocivil int primary key auto_increment,
    estadocivil varchar(20));
    
alter table cidade add foreign key (id_estado) references estado(id_estado);
alter table clientes add foreign key (id_cidade) references cidade(id_cidade);
alter table clientes add foreign key (id_sexo) references sexo(id_sexo);
alter table clientes add foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade);
alter table clientes add foreign key (id_raca) references raca(id_raca);
alter table clientes add foreign key (id_escolaridade) references escolaridade(id_escolaridade);
alter table clientes add foreign key (id_estadocivil) references estadocivil(id_estadocivil);

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
    (null, 'Rio Grande do Sul'),
    (null, 'Minas Gerais'),
    (null, 'Distrito Federal');

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
insert into estadocivil (id_estadocivil, estadocivil) values
	(null, 'Solteiro'),
    (null, 'Cadaso'),
    (null, 'Divorciado'),
    (null, 'Viúvo');
insert into cliente (id_cliente, nome, cpf, rg, id_cidade, id_sexo, id_nacionalidade, fone, id_raca, id_escolaridade, id_estadocivil, idade) values
(NULL, 'Lucas Martins', '33.456.789-01', '56.789.012', 45, 1, 1, '(11) 98765-4321', 1, 3, 2, 28),
(NULL, 'Ana Souza', '45.678.901-22', '67.890.123', 102, 2, 2, '(21) 99876-5432', 2, 4, 1, 56),
(NULL, 'Ricardo Lima', '56.789.012-33', '78.901.234', 67, 1, 1, '(31) 91234-5678', 3, 5, 3, 34),
(NULL, 'Beatriz Costa', '67.890.123-44', '89.012.345', 88, 2, 2, '(41) 92345-6789', 1, 6, 2, 41),
(NULL, 'Felipe Oliveira', '78.901.234-55', '90.123.456', 55, 1, 1, '(51) 93456-7890', 2, 2, 4, 16),
(NULL, 'Juliana Pereira', '89.012.345-66', '01.234.567', 120, 2, 2, '(61) 94567-8901', 3, 4, 1, 73),
(NULL, 'Ricardo Ferreira', '90.123.456-77', '12.345.678', 30, 2, 1, '(71) 95678-9012', 1, 3, 2, 59),
(NULL, 'Fernanda Alves', '01.234.567-88', '23.456.789', 115, 1, 2, '(81) 96789-0123', 2, 5, 3, 45),
(NULL, 'Lucas Costa', '12.345.678-99', '34.567.890', 48, 3, 1, '(91) 97890-1234', 3, 6, 1, 12),
(NULL, 'Patrícia Lima', '23.456.789-00', '45.678.901', 25, 1, 2, '(11) 98901-2345', 1, 4, 4, 68),
(NULL, 'André Santos', '34.567.890-11', '56.789.012', 107, 2, 1, '(21) 99012-3456', 2, 2, 2, 54),
(NULL, 'Isabela Rocha', '45.678.901-22', '67.890.123', 77, 1, 1, '(31) 91234-5678', 3, 5, 3, 39),
(NULL, 'Tiago Almeida', '56.789.012-33', '78.901.234', 92, 2, 2, '(41) 92345-6789', 1, 6, 4, 25),
(NULL, 'Juliana Ribeiro', '67.890.123-44', '89.012.345', 64, 3, 1, '(51) 93456-7890', 2, 3, 1, 78),
(NULL, 'Roberto Souza', '78.901.234-55', '90.123.456', 101, 1, 2, '(61) 94567-8901', 3, 4, 2, 62),
(NULL, 'Gabriela Costa', '89.012.345-66', '01.234.567', 19, 2, 1, '(71) 95678-9012', 1, 2, 3, 50),
(NULL, 'Vitor Pereira', '90.123.456-77', '12.345.678', 82, 1, 2, '(81) 96789-0123', 2, 5, 4, 11),
(NULL, 'Lúcia Almeida', '01.234.567-88', '23.456.789', 110, 2, 1, '(91) 97890-1234', 3, 6, 1, 23),
(NULL, 'Eduardo Santos', '12.345.678-99', '34.567.890', 36, 3, 2, '(11) 98901-2345', 1, 4, 2, 77),
(NULL, 'Marta Ferreira', '23.456.789-00', '45.678.901', 79, 1, 1, '(21) 99012-3456', 2, 3, 3, 18);

