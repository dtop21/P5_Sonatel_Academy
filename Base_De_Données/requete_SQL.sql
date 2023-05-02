1.Donner le nom et l’adresse des contribuables qui ont fait des déclarations publicitaires
   select c.nom,c.adr
   from contribuable c,declaration d
   where c.ncont = d.ncont
   and d.libelle = "publicit";

2.Donner le numéro et le nom du premier contribuable qui a payé une amende
   select c.nom,c.tel
   from contribuable c,payer_amende p
   where c.ncont = p.ncont
   and date = (select min(date) from payer_amende);
OU BIEN
   select c.nom,c.tel
   from contribuable c,payer_amende p
   where c.ncont = p.ncont
   and date <= all(select date from payer_amende);

3.Donner le numéro, le nom, le libellé et le montant totale de l’amande payé pour chaque contribuable selon le type(libellé) d’amande 
   select c.nom,c.tel,a.libelle,sum(a.montant) as total
   from contribuable c,amende a,payer_amende p
   where c.ncont = p.ncont
   and a.namende = p.namende
   group by c.nom,c.tel,a.libelle;

4.Donner le numéro, le nom et le montant moyen des taxes payées par chaque contribuable
   select c.nom,c.tel,avg(t.montant) as montant_moyen
   from contribuable c,taxes t,payer_taxe p
   where c.ncont = p.ncont
   and t.ntaxe = p.ntaxe
   group by c.nom,c.tel;

5.Donner le numéro, le nom le libellé et le montant des contribuables ayant payé l’amande minimale
   select c.nom,c.tel,a.libelle,a.montant
   from contribuable c,amende a,payer_amende p
   where c.ncont = p.ncont
   and a.namende = p.namende
   and a.montant = (select min(montant) from amende);

6.Donner le numéro, le nom le libellé et le montant des contribuables ayant payé la taxe maximale
   select c.nom,c.tel,t.type,t.montant
   from contribuable c,taxes t,payer_taxe p
   where c.ncont = p.ncont
   and t.ntaxe = p.ntaxe
   and t.montant = (select max(montant) from taxes);

7.Donner le numéro, le nom le libellé et le montant des 5(cinq) premiers contribuables ayant payé la taxe maximale 
   select c.nom,c.tel,t.type,t.montant,p.date
   from contribuable c,taxes t,payer_taxe p
   where c.ncont = p.ncont
   and t.ntaxe = p.ntaxe
   and t.montant = (select max(montant) from taxes)
   order by p.date
   limit 5;

8.Donner le libelle de la déclaration, le montant de la taxe et le nom du contribuable des taxes payées le 2020-06-05
   select c.nom,t.type,sum(t.montant)
   from contribuable c,taxes t,payer_taxe p
   where c.ncont = p.ncont
   and t.ntaxe = p.ntaxe
   and p.date = '2020-06-05'
   group by c.nom,t.type;

9.Donner le numéro et le nom des contribuables qui ont individuellement payé au total plus de 500000 F d’amende pour des déclarations de spectacles.
   select c.nom,c.tel,sum(a.montant) as total
   from contribuable c,amende a,payer_amende p,declaration d
   where c.ncont = p.ncont
   and c.ncont = d.ncont
   and a.namende = p.namende
   and d.libelle = 'spectacle'
   group by c.nom,c.tel
   having total > 500000;

10.Donner séparément les montants totaux des taxes de spectacles ou de publicités (une seule instruction SQL).
   select type,sum(montant) as Totaux
   from taxes
   where type = 'spectacle'
   union
   select type,sum(montant)
   from taxes
   where type = 'publicit';

11.Donner le numéro et le nom des contribuables qui ont individuellement payé au total plus de 500000 F d’amende pour des déclarations de spectacles.

12.Donner le numéro et le nom des contribuables qui n’ont jamais payé d’amende
   select distinct c.nom,c.tel
   from contribuable c
   where c.ncont != all(select ncont from payer_amende);

13.Donner le numéro et le nom des contribuables qui ont individuellement payé au total plus de quatre (4) amendes
   select c.nom,c.tel,count(c.ncont) as Nombre_Amendes
   from contribuable c,payer_amende p
   where c.ncont = p.ncont
   group by c.nom,c.tel
   having Nombre_Amendes > 4;

14.Donner le numéro et le nom du contribuable qui a payé plus de taxe
   select c.nom,c.tel,sum(t.montant) as Montant_Taxes
   from contribuable c,taxes t,payer_taxe p
   where c.ncont = p.ncont
   and t.ntaxe = p.ntaxe
   group by c.nom,c.tel
   order by Montant_Taxes desc
   limit 1;

15.Donner les informations des contribuables qui habitent paris
   select *
   from contribuable
   where adr like '%Paris%';

16.Donner le numéro et le nom des contribuables qui n’ont jamais payé d’amende
   select c.nom,c.tel
   from contribuable c
   where c.ncont not in (select ncont from payer_amende);

17.Donner le numéro et le nom des contribuables qui ont fait des déclarations entre le 4 avril 2020 et le 15 ou entre le 19 Mai et le 25 mai
   select distinct c.nom,c.tel
   from contribuable c,declaration d
   where c.ncont = d.ncont
   and ((d.date between '2020-04-04' and '2020-04-15') or (d.date between '2020-05-19' and '2020-05-25'));

18.Donner le numéro et le nom, le mois et la taxe total payée par chaque contribuable par mois
   select c.nom,c.tel,extract(month from p.date) as Mois,sum(t.montant) as total
   from contribuable c,taxes t,payer_taxe p
   where c.ncont = p.ncont
   and t.ntaxe = p.ntaxe
   group by c.nom,c.tel,Mois
   order by c.nom;

19.Donnez les informations des contribuables dont le nom contient entre 4 et 6 caractères
   select *
   from contribuable
   having length(nom) between 4 and 6;