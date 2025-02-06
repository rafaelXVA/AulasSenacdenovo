create table Disciplina (
	idDisciplina int auto_increment not null primary key,
    disciplinas int not null);
create table Turma (
	idTurma int auto_increment not null primary key,
    turmas int not null);
alter table Turma add foreign key (turmas) references Turma(idTurma);
alter table Disciplina add foreign key (disciplinas) references Disciplina(idDisciplina);
describe Turma;
create table PeriodoLetivo (
	idPeriodo int auto_increment not null primary key,
    turmas int);
alter table PeriodoLetivo add foreign key (turmas) references Turma(idTurma);
alter table Turma add periodo_letivo int not null;
alter table Turma add foreign key (periodo_letivo) references PeriodoLetivo(idPeriodo);
describe PeriodoLetivo;
alter table Curso modify faculdade int not null;
create table Faculdade (
	idFaculdade int auto_increment not null primary key,
    cursos int,
    instituto int);
create table Instituto (
	idInstituto int auto_increment not null primary key,
    faculdades int,
    professores int);
create table Curso (
	idCurso int auto_increment not null primary key,
	alunos int,
    faculdade int);
alter table Faculdade add foreign key (cursos) references Curso(idCurso);
alter table Curso add foreign key (faculdade) references Faculdade(idFaculdade);
alter table Faculdade add foreign key (instituto) references Instituto(idInstituto);
alter table Instituto add foreign key (faculdades) references Faculdade(idFaculdade);
create table Professor (
	idProfessor int auto_increment not null primary key,
    turmas int not null,
    instituto int not null);
alter table Professor add foreign key (turmas) references Turma(idTurma);
alter table Turma add foreign key (professor) references Professor(idProfessor);
describe Instituto;
alter table Professor add foreign key (instituto) references Instituto(idInstituto);
alter table Instituto add foreign key (professores) references Professor(idProfessor);