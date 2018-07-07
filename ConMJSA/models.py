from django.db import models
import pandas as pd
import numpy as np
df_hor = pd.read_csv('realparsing.csv',sep=',')

df_hor_c  = np.array(df_hor.columns)
hor_db =[] 
for x in range(len(df_hor_c)):
   hor_db.append(df_hor_c[x])
print(df_hor_c[x])

class CMS(models.Model):
   class Meta:
      db_table = 'cmssss' 
   i=0   
   for y in range(len(df_hor_c)):
      try:
      
         '%s = models.CharField(max_length=20)'%df_hor_c[i]  
      
      except :
         i +=1        
         if (i == y):
            break

 #'%s = models.CharField(db_column="%s",max_length=20)'%(' '.join(df_hor_c[y].split('.')),df_hor_c[y])



# Create your models here.
