# se il collegamento di due nodi dipende dall'esistenza di una cosa in un altra tabella
# fare 4 tabelle, collega 1-3 e 2-4
# collega 3-4 in caso
"""datediff(data1,data2)"""
#trova la differenza in giorni

"""year(date)"""
#trova l anno in un datetime

"""SELECT>T g1.GeneID AS id1, g2.GeneID AS id2,
             CASE 
                 WHEN g1.Chromosome = g2.Chromosome THEN g1.Chromosome
                 ELSE g1.Chromosome + g2.Chromosome
             END AS somma
      FROM genes g1, genes g2
      WHERE g1.Chromosome <= g2.Chromosome
      GROUP BY g1.GeneID, g2.GeneID"""
# if
"""CASE
WHEN EVENTO 1 THEN SOLUZIONE 1
ELSE SOLUZIONE 2
END"""
max(s.lat) o min()
# trovano il massimo e minimo dei vaori selezionati

between %s and %s
# tra due valori (compresi)

METODI SQL :
1. Funzioni matematiche
ABS(x) – Valore assoluto

CEIL(x) o CEILING(x) – Arrotonda per eccesso

FLOOR(x) – Arrotonda per difetto

ROUND(x[, d]) – Arrotonda con d decimali

TRUNC(x[, d]) – Tronca decimali (Oracle, PostgreSQL)

POWER(x, y) – x elevato alla y

SQRT(x) – Radice quadrata

MOD(x, y) – Resto della divisione

EXP(x) – e^x

LOG(x) – Logaritmo naturale

LOG10(x) – Logaritmo base 10

RANDOM() / RAND() – Numero casuale

PI() – Costante π

🕒 2. Funzioni per data e ora
NOW() – Data e ora attuali

CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP

DATEPART(unit, date) – Estrae parti (SQL Server)

EXTRACT(field FROM date) – PostgreSQL  SELECT EXTRACT(YEAR FROM CURRENT_DATE);

DATE_ADD(date, INTERVAL x unit) – Somma (MySQL)  SELECT DATE_ADD('2024-01-01', INTERVAL 10 DAY);

DATE_SUB(date, INTERVAL x unit) – Sottrai (MySQL)  SELECT DATE_SUB('2024-01-10', INTERVAL 5 DAY);

DATEDIFF(date1, date2) – Differenza in giorni

TO_CHAR(date, format) – Formatta data (Oracle/PostgreSQL)  SELECT TO_CHAR(NOW(), 'YYYY-MM-DD');

TO_DATE(string, format) – Converte stringa in data

🔤 3. Funzioni per stringhe
CONCAT(s1, s2, ...) – Unisce stringhe

SUBSTRING(s, start, length) – Estrae sottostringa

LEFT(s, n) / RIGHT(s, n)

LENGTH(s) / CHAR_LENGTH(s) – Lunghezza

UPPER(s) / LOWER(s) – Maiuscole/minuscole

TRIM(s) – Rimuove spazi (oppure LTRIM, RTRIM)

REPLACE(s, old, new)

INSTR(s, substring) / POSITION() – Posizione

REVERSE(s) – Inverte stringa

LPAD(s, len, pad) / RPAD(s, len, pad) – Padding

FORMAT(s, ...) – Formattazione (SQL Server, MySQL)

📊 4. Funzioni di aggregazione
COUNT(*), COUNT(col)

SUM(col)

AVG(col)

MIN(col)

MAX(col)

GROUP_CONCAT(col) – Unisce valori in gruppo (MySQL)

STRING_AGG(col, sep) – PostgreSQL, SQL Server

🧠 5. Funzioni logiche e di controllo
CASE WHEN THEN ELSE END

IF(condition, true, false) – MySQL

NULLIF(expr1, expr2)

COALESCE(val1, val2, ...) – Primo valore non nullo

ISNULL(expr) / IFNULL(expr1, expr2)

📐 6. Funzioni analitiche / window functions
(usate con OVER())

ROW_NUMBER()

RANK(), DENSE_RANK()

NTILE(n)

LAG(col, offset)

LEAD(col, offset)

FIRST_VALUE(col)

LAST_VALUE(col)

SUM(col) OVER(...)

AVG(col) OVER(...)

COUNT() OVER(...)

🧱 7. Funzioni di tipo / casting
CAST(expr AS type)

CONVERT(expr, type) – SQL Server/MySQL

::type – PostgreSQL (es. price::integer)

🔐 8. Funzioni specifiche per DBMS
UUID() – Genera un UUID (MySQL, PostgreSQL)

JSON_EXTRACT, JSON_VALUE, ->, ->> – JSON (MySQL/PostgreSQL)

GEOMETRY, ST_Distance, ST_Within – Funzioni spaziali (GIS)

REGEXP, REGEXP_REPLACE, REGEXP_MATCHES – Espressioni regolari

Extra: Stored Procedure & Metodi (esterni alle query)
Questi non sono “funzioni” SQL ma sono concetti correlati:

Stored Procedures – CREATE PROCEDURE, CALL

Triggers

User-defined functions (UDF) – CREATE FUNCTION

Cursors – iterazioni sui risultati


