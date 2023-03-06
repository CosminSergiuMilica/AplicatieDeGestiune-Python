

---insert in tabelul REDUCERI
insert into reduceri(reducere, observatii) values(0.1,'Se acorda doar cu prezentarea cuponului de pensie');
insert into reduceri(reducere,observatii) values(0.2,'Se acorda doar daca se prezinta carnetul de student');
insert into reduceri(reducere,observatii) values(0.3,'Se acorda doar daca se prezinta carnetul de elev');
insert into reduceri(reducere) values(0);



--inserari in tabelul TIP_CLIENT
insert into tip_client( name_tclient, id_reducere) 
values('Student',68);
insert into tip_client( name_tclient, id_reducere) 
values('Minor',69);
insert into tip_client( name_tclient, id_reducere) 
values('Pensionar',67);
insert into tip_client( name_tclient, id_reducere) 
values('Adult',70);


--inserari in tabelul TIP_ANTRENAMENT
insert into tip_antrenament( name_antrenament, cost_abonament) 
values( 'Cardio', 120);
insert into tip_antrenament( name_antrenament, cost_abonament) 
values( 'Fitness', 150);
insert into tip_antrenament( name_antrenament, cost_abonament) 
values( 'Crossfit', 180);
insert into tip_antrenament( name_antrenament, cost_abonament) 
values( 'Pilates', 280);



--inserari in tabelul Antrenor
insert into antrenor( name_antrenor,id_type, start_program, end_program)
values('Popescu Daniel', 42,to_date('8:00','hh24:mi'),to_date('22:00','hh24:mi'));
insert into antrenor( name_antrenor, id_type, start_program, end_program)
values('Ionescu Vlad', 43,to_date('10:00','hh24:mi'),to_date('23:00','hh24:mi'));
insert into antrenor( name_antrenor, id_type, start_program, end_program)
values('Popa Codrin', 43,to_date('11:00','hh24:mi'),to_date('23:00','hh24:mi'));
insert into antrenor( name_antrenor, id_type, start_program, end_program)
values('Cristea Andrei', 44,to_date('07:00','hh24:mi'),to_date('15:00','hh24:mi'));
insert into antrenor( name_antrenor, id_type, start_program, end_program)
values('Popovici George', 42,to_date('12:00','hh24:mi'),to_date('22:00','hh24:mi'));



--inserari in tabelul CLIENT
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('Diaconu Andrei', 0721708542, 64, 42, to_date('2022/11/20','yyyy/mm/dd'), to_date('2022/12/20','yyyy/mm/dd'));
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('Leonte Rares', 0721908542, 64, 43, to_date('2022/11/10','yyyy/mm/dd'), to_date('2022/12/10','yyyy/mm/dd'));
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('Ganea Irina', 0721988542, 65, 42, to_date('2022/12/10','yyyy/mm/dd'), to_date('2023/01/10','yyyy/mm/dd'));
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('Sandu Gigi', 0751988542, 67, 43, to_date('2022/12/15','yyyy/mm/dd'), to_date('2023/01/15','yyyy/mm/dd'));
insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)
values('Leonte Bianca', 0751088512, 65, 42, to_date('2022/12/05','yyyy/mm/dd'), to_date('2023/01/05','yyyy/mm/dd'));



--inserare in tabelul PROGRAMARI
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 64, 36,to_date('2022/12/21 12:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2022/12/21 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 63, 37,to_date('2022/12/21 12:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2022/12/21 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 64, 38,to_date('2022/12/21 09:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2022/12/21 10:00:00', 'yyyy/mm/dd hh24:mi:ss'));
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 66, 39,to_date('2022/12/21 12:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2022/12/21 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 67,36,to_date('2022/12/20 12:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2022/12/20 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));
insert into programari(client,id_antrenor,programare_start, programare_end)
values( 65, 40,to_date('2022/12/25 12:00:00', 'yyyy/mm/dd hh24:mi:ss'),
to_date('2022/12/25 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));

