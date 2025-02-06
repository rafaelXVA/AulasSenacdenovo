create table alunos (
	registro_matricula int auto_increment not null primary key,
    nome varchar(30) not null,
    email varchar(50) not null);
    
insert into alunos values (null, "joão vitor","guaxinim@dbm2.com.br");
drop table estado;
create table estado (
	idEstado int auto_increment primary key,
    nomeEstado varchar(20) not null,
    UF varchar(2) not null);
    
insert into estado  (idEstado, nomeEstado, UF) values
					1(null, "Mato Grosso do Sul", "MS"),
					2(null, "Paraná", "PR"),
					3(null, "Minas Gerais", "MG"),
					4(null, "Santa Catarina", "SC"),
					5(null, "Rio Grande do Sul", "RS"),
					6(null, "São Paulo", "SP"),
					7(null, "Rio Janeiro", "RJ"),
					8(null, "Espirito Santo", "ES"),
					9(null, "Goiás", "GO"),
					10(null, "Mato Grosso", "MT"),
					11(null, "Distrito Federal", "DF"),
					12(null, "Amazonas", "AM"),
					13(null, "Rondônia","RO"),
					14(null, "Acrê","AC"),
					15(null, "Tocantis","TO"),
					16(null, "Amapa","AP"),
					17(null, "Pará","PA"),
					18(null, "Sergipe", "SE"),
					19(null, "Pernambuco", "PE"),
					20(null, "Píaui","PI"),
					21(null, "Paraíba","PB"),
					22(null, "Ceará","CE"),
					23(null, "Bahia","BA"),
					24(null, "Roraima","RR"),
					25(null, "Alagoas","AL"),
					26(null, "Maranhão","MA"),
					27(null, "Rio Grande do Norte","RN");

create table cidade (
	idCidade int primary key auto_increment,
    estado int not null,
    regiao varchar(20) not null,
    nomeCidade varchar(50) not null);

alter table cidade add foreign key (estado) references estado(idEstado);


insert into cidade (idCidade, estado, regiao, nomeCidade) values 
				   (null, 14, "norte","Rio Branco" ),
                   (null, 25, "nordeste", "Maceió"),
                   (null, 12, "norte","Manaus"),
                   (null, 23, "nordeste","),
                   (null, 22, "nordeste"),
                   (null, 8, "sudeste"),
                   (null, 
                    
select * from estado;