Create database Apolo;
Use Apolo;
Create table registro(
id int (10) primary key auto_increment, nom varchar(45),
apellido varchar(45),
edad varchar(45),
correo varchar(45),
tel varchar(45),
direc varchar(45)
);
Create table perros(
id int (10) primary key auto_increment,
nomb varchar(45),
raza varchar(45),
sexo varchar(45),
tam varchar(45),
vac varchar(45),
ed varchar(45)
);