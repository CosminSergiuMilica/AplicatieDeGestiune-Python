--testare constrangere NUME(insert, update) client cu cifre in el
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('D23iaconu Andrei', 0721508542,64, 43, to_date('2022/12/20','yyyy/mm/dd'), to_date('2023/01/20','yyyy/mm/dd'));

update client
set name_client = 'D23iaconu Andrei'
where id_client=50;

--testare introducerea unei date de expirare a abonamentului mai mica decat data abonarii(insert, update)
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('Diaconu Andrei', 0721508542, 64, 43, to_date('2022/12/20','yyyy/mm/dd'), to_date('2022/09/20','yyyy/mm/dd'));

update client
set end_time=to_date('2022/09/20','yyyy/mm/dd')
where id_client=64;
--testare numar de telefon eronat
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('Diaconu Andrei', 02, 64, 43, to_date('2022/12/20','yyyy/mm/dd'), to_date('2023/01/20','yyyy/mm/dd'));

update client
set telefon=02
where id_client=64;


--update unui tip de client eronat
update tip_client
set name_tclient = 'caine'
where id_tclient=65;

--testarea introducerii unui tip de antrenament eronat
insert into tip_antrenament( name_antrenament, cost_abonament) 
values( 'Sah', 180);

update tip_antrenament
set name_antrenament = 'sah'
where id_type=44;


--verificare programare mai mica decat data curenta
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 65, 37,to_date('2002/11/21 12:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2002/11/21 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));

update programari
set programare_start = to_date('2002/11/21 12:00:00', 'yyyy/mm/dd hh24:mi:ss')
where id_programare = 43;

--testare constrangere NUME ANTRENOR cu cifre in el
insert into antrenor( name_antrenor, id_type, start_program, end_program)
values('Crist33ea Andrei', 39,to_date('07:00','hh24:mi'),to_date('15:00','hh24:mi'));

update antrenor
set name_antrenor = 'D23iaconu Andrei'
where id_antrenor=43;

--testare sfarsitul programului este mai mic decat inceputul
insert into antrenor( name_antrenor,id_type, start_program, end_program)
values('Popescu Daniel', 43,to_date('8:00','hh24:mi'),to_date('7:00','hh24:mi'));

--testare introducere REDUCERE diferita de valorile predefinite
insert into reduceri(reducere) values(0.8);
update reduceri 
set reducere = 0.9
where id_reducere = 70;


--update Antrenor in programari
update programari
set id_antrenor = 37
where id_programare = 43;

--testare programare identica
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 67, 39,to_date('2022/12/21 12:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2022/12/21 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));

update programari
set id_antrenor = 36
where client=66 and
programare_start = to_date('2022/12/21 12:00:00', 'yyyy/mm/dd hh24:mi:ss');

--Vizualizare cost abonamente dupa reducere
select c.name_client ,a.cost_abonament - r.reducere*a.cost_abonament
from client c, tip_antrenament a, reduceri r, tip_client cc
where c.id_tclient = cc.id_tclient and
cc.id_reducere = r.id_reducere and
c.id_type = a.id_type;

--vizualizare program antrenori
select name_antrenor ,to_char(start_program,'hh24:mi'),to_char(end_program,'hh24:mi')from antrenor;

--EVIDENTA ACTIVITATII DIN SALA

--Evidenta clinetilor care au antrenamente de Cardio programate
select c.name_client 
from client c, programari p
where c.id_client= p.client and
c.id_type = 42;

--Evidenta clinetilor care au antrenamente de Fitness programate
select c.name_client 
from client c, programari p
where c.id_client= p.client and
c.id_type = 43;

--Numarul de clienti care au antrenament in ziua 2022/12/21
select count(*) 
from programari
where to_char(programare_start,'yyyy/mm/dd ') ='2022/12/21';

--Numarul de programari ale antrenorului cu id-ul 36
select count(*) 
from programari
where id_antrenor=36;

select a.name_antrenament from programari p, antrenament ant, tip_antrenament abonamente
where p.id_antrenor = ant.id_antrenament and ant.id_type = a.id_type;



