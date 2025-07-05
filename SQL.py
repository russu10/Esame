
# SEELEZIONA N TRAMITE UNA SUBQUERY, RICORDATI Y
"""SELECT  *
from
(SELECT COUNT(DISTINCT s1.Date) as N
FROM go_daily_sales s1, go_daily_sales s2
WHERE s1.Date = s2.Date
AND s1.Retailer_code = s2.Retailer_code
AND s1.Product_Number = 1215
AND s2.Product_Number = 86113
AND YEAR(s1.Date) = 2015) y
where N > 0"""

#SELEZIONA 4 TABELLE, QUANTI PRODOTTI VENDUTI DA DUE RETAILER DIVERSI
#NELLO STESSO ANNO E STESSO PRODOTTO E STESSA NAZIONE
"""SELECTT

    s1.Retailer_code AS r1, 
    s2.Retailer_code AS r2, 
    COUNT(DISTINCT s1.Product_number) AS peso
FROM 
    go_daily_sales s1, 
    go_daily_sales s2, 
    go_retailers r1, 
    go_retailers r2
WHERE 
    s1.Product_number = s2.Product_number
    AND s1.Retailer_code < s2.Retailer_code
    AND YEAR(s1.Date) = YEAR(s2.Date)
    AND YEAR(s1.Date) = 2015
    AND r1.Country = r2.Country
    AND r1.Country = "United States"
    AND r1.Retailer_code = s1.Retailer_code
    AND r2.Retailer_code = s2.Retailer_code
GROUP BY 
    s1.Retailer_code, s2.Retailer_code
HAVING 
    COUNT(DISTINCT s1.Product_number) > 0"""

#seleziona quante volte il pilota 1 ha vinto sul pilota 2
#vincolo posizione non nulla
#vincolo anno
"""selectt r1.driverId as d1, r2.driverId as d2, count(*) as cnt
				from results as r1, results as r2, races
				where r1.raceId = r2.raceId
				and races.raceId = r1.raceId
				and races.year = %s
				and r1.position is not null
				and r2.position is not null 
				and r1.position < r2.position 
				group by d1, d2"""

#seleziona ordini effettuati in un massimo di k giorni di distanza
#collega 4 tabelle 2 a 2
#le seconde due le collega una per una, non le unisce, una rappresenta un articolo e l altra un altro
#conta la somma tra due quantità
"""Selectt DISTINCT o1.order_id as id1, o2.order_id as id2, count(oi.quantity+ oi2.quantity) as cnt
                from orders o1, orders o2, order_items oi, order_items oi2 
                where o1.store_id=%s
                and o1.store_id=o2.store_id 
                and o1.order_date > o2.order_date
                and oi.order_id = o1.order_id
                and oi2.order_id  = o2.order_id
                and DATEDIFF(o1.order_Date, o2.order_date) < %s
                group by o1.order_id, o2.order_id"""


"""SELECTt DISTINCT i.GeneID1 as id1, i.GeneID2 as id2, t.somma as peso
FROM genes g1, genes g2, classification c1, classification c2, interactions i,
     (SELECT g1.GeneID AS id1, g2.GeneID AS id2,
             CASE 
                 WHEN g1.Chromosome = g2.Chromosome THEN g1.Chromosome
                 ELSE g1.Chromosome + g2.Chromosome
             END AS somma
      FROM genes g1, genes g2
      WHERE g1.Chromosome <= g2.Chromosome
      GROUP BY g1.GeneID, g2.GeneID) AS t
WHERE g1.GeneID <> g2.GeneID
  AND c1.GeneID = g1.GeneID
  AND g2.GeneID = c2.GeneID
  AND c1.Localization = %s
  AND c2.Localization = c1.Localization
  AND i.GeneID1 = g1.GeneID
  AND i.GeneID2 = g2.GeneID
  AND t.id1 = g1.GeneID
  AND t.id2 = g2.GeneID"""
#c e un if all interno della query
