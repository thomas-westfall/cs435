create table places (name varchar(75) not null, borough varchar(1) not null, editdate datetime not null, latitude decimal(17,15) not null, longitude decimal(17,15) not null, status varchar(25) not null, closuretype varchar(40) not null);

load data local infile '~/Desktop/435/output/places.csv' into table places fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

alter table places ADD id int primary key auto_increment first;

create table playgrounds(place_id int not null, location varchar(100), accesslvl int not null, rules varchar(50), primary key (place_id),foreign key (place_id) references places(id));

load data local infile '~/Desktop/435/output/playgroundnew.csv' into table playgrounds fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

create table skateparks(place_id int not null, propname varchar(50), subpropname varchar(50), primary key (place_id),foreign key (place_id) references places(id));

load data local infile '~/Desktop/435/output/skateparknew.csv' into table skateparks fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

create table exerciseequipment(place_id int not null, propname varchar(50), subpropname varchar(50), primary key (place_id),foreign key (place_id) references places(id));

load data local infile '~/Desktop/435/output/exercisenew.csv' into table exerciseequipment fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

create table dogruns(place_id int not null, propname varchar(50), subpropname varchar(50), primary key (place_id),foreign key (place_id) references places(id));

load data local infile '~/Desktop/435/output/dogrunnew.csv' into table dogruns fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

create table athleticfacilities(place_id int not null, propname varchar(50), subpropname varchar(50), primarysport varchar(25), fieldnumber int, netsremoved boolean, surfacetype varchar(15), primary key (place_id),foreign key (place_id) references places(id));

load data local infile '~/Desktop/435/output/athfacnew.csv' into table athleticfacilities fields terminated by ',' optionally enclosed by '"' ignore 1 lines;