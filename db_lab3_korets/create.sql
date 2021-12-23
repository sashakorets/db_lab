--цей файл не змінився
create table wines (
  wine_id int not null,
  wine_name char(256) not null,
  wine_points int,
  wine_price int,
  region char(50),
);

create table province(
  region char(50) primary key not null,
  province char(50) not null,
);

create table country(
  province char(50) primary key not null,  
  country char(50) not null,
);

alter table  wines add constraint FK_region_province foreign key (region) references province (region);
alter table  province add constraint FK_province_country foreign key (province) references country (province);--create
