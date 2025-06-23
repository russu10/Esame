
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
