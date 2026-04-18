# Importation des fonctions

import pandas as pd
import numpy as np
import time as t

# Importation du fichier csv

df_initial = pd.read_csv('nba.games.stats.csv')
df_initial

# Suppression des variables non pertinentes

df_drop = df_initial.drop(columns=['Unnamed: 0','Game','Opponent','OpponentPoints','FieldGoals','FieldGoalsAttempted','FieldGoals.','FreeThrows','FreeThrowsAttempted','FreeThrows.','OffRebounds','TotalRebounds','Assists','Steals','Blocks','Turnovers','TotalFouls','Opp.FieldGoals','Opp.FieldGoalsAttempted','Opp.FieldGoals.','Opp.3PointShots','Opp.3PointShotsAttempted','Opp.3PointShots.','Opp.FreeThrows','Opp.FreeThrowsAttempted','Opp.FreeThrows.','Opp.OffRebounds','Opp.TotalRebounds','Opp.Assists','Opp.Steals','Opp.Blocks','Opp.Turnovers','Opp.TotalFouls']) 
df_drop

# Renommer les colonnes

df_rename = df_drop.rename(index=str, columns={"Home": "Location",'WINorLOSS': 'Result','X3PointShots': '3PTS_M','X3PointShotsAttempted' : '3PTS_A','X3PointShots.' : '3PTS_P'})
df_rename

# Création d'une nouvelle variable (3PTS_Percentage à partir de 3PTS_P)

df_rename['3PTS_Percentage']=Var1['3PTS_P']*100
df_rename

# Suppression de la variable 3PTS_P

df_final = df_rename.drop(columns=['3PTS_P'])
df_final

# Création de la variable Season

"""Notre base de données nous renseigne uniquement sur la date présice des matchs. Or, la saison NBA débutant en octobre et se terminant en avril, s'étend sur deux années. Il convient donc pour notre étude de créer une nouvelle variable que nous appelerons "Season". Cette variable nous permettra de classer les statistiques par saison et ainsi d'analyser leurs évolutions par saison."""

df_final['Season']=1
df_final

df_final.Date=pd.to_datetime(df_final['Date'], format='%Y-%m-%d')
df_final.Season.loc[df_final.Date>'2015-10-01']=2

df_final.Season.loc[df_final.Date>'2016-10-01']=3

df_final.Season.loc[df_final.Date>'2017-10-01']=4

df_final.Season.value_counts()

df_final

"""Nous venons ainsi d'affecter les valeurs :
- 1 à la saison 2014-2015
- 2 à la saison 2015-2016
- 3 à la saison 2016-2017
- 4 à la saison 2017-2018
"""

# Création de variables pour chacune des 30 franchises par saison

### Statistiques par équipe

#### Saison 2014-2015

# ATLANTA HAWKS

atl = df_rename[df_rename.Team == 'ATL']
atl_1415=atl[atl.Date < '2015-04-16']
atl_1415

### Moyenne des points marqués sur la saison 2014-2015¶

TPatl = atl_1415.loc[:,['TeamPoints']]
MoyTPatl = np.mean(TPatl)
MoyTPatl

### Moyenne 3 points marqués

X_3PTSatl = atl_1415.loc[:,['3PTS_M']]
Moy3PTSMatl = np.mean(X_3PTSatl)
Moy3PTSMatl

### Moyenne 3 points tentés

X_3PTSAatl = atl_1415.loc[:,['3PTS_A']]
Moy3PTSAatl = np.mean(X_3PTSAatl)
Moy3PTSAatl

### Afficher le total de victoires et défaites (à partir de la variable 'Résult')

Winatl = list(atl_1415['Result'])
W_atl = Winatl.count('W')
W_atl

Loseatl = list(atl_1415['Result'])
L_atl = Win.count('L')
L_atl

# Résumé saison 2014-2015

df2 = pd.DataFrame({'PTS': [102.5, 101.4, 98.0, 94.2, 100.8, 103.1, 105.2, 101.5, 98.5, 110.0, 103.9, 97.3, 106.7, 98.5, 98.3, 94.7, 97.8, 97.8, 99.4, 91.9, 104.8, 95.7, 92.0, 102.4, 102.8, 101.3, 103.2, 104.0, 95.1, 98.5], '3PTS_M': [10.0,8.0, 6.6, 6.1, 7.9, 10.1, 8.9, 8.0,  8.6, 10.8, 11.4,7.5, 10.1, 6.5, 5.2, 6.8, 6.6, 5.0, 7.1, 6.8, 7.7,  6.8, 8.4, 8.5, 9.8, 5.6, 8.3, 8.9, 7.4, 6.1], '3PTS_A': [26.2, 24.6, 19.9, 19.1, 22.3, 27.5, 25.4, 24.8, 24.9, 27.0, 32.7, 21.2, 26.9, 18.9, 15.2, 20.2, 18.3, 14.9, 19.3, 19.7, 22.7, 19.5, 26.3, 25.0, 27.2, 16.5, 22.5, 25.1, 21.7, 16.8]}, index = ['ATL','BOS','BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']) 
df2

# Exportation du fichier en csv

df_final.to_csv('DF_nba_stats.csv')












