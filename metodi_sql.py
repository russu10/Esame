"""datediff(data1,data2)"""
#trova la differenza in giorni

"""year(date)"""
#trova l anno in un datetime
"""SELECTt g1.GeneID AS id1, g2.GeneID AS id2,
             CASE 
                 WHEN g1.Chromosome = g2.Chromosome THEN g1.Chromosome
                 ELSE g1.Chromosome + g2.Chromosome
             END AS somma
      FROM genes g1, genes g2
      WHERE g1.Chromosome <= g2.Chromosome
      GROUP BY g1.GeneID, g2.GeneID"""
#per inserire un if all interno fare:
"""CASE
WHEN EVENTO1 THEN SOLUZIONE 1
ELSE SOLUZIONE 2
END"""