from django.db import models
import pandas as pd
import numpy as np

class CMS(models.Model):
   class Meta:
      db_table = 'leeu' 
   
   Study_id            =  models.CharField(max_length=200)
   Run_id              =  models.CharField(max_length=200)
   Assay_type          =  models.CharField(max_length=200)
   Genotype            =  models.CharField(max_length=200)
   Treatment           =  models.CharField(max_length=200) 
   Dev                 =  models.CharField(max_length=200) 
   Tissue              =  models.CharField(max_length=200) 
   Layout              =  models.CharField(max_length=200)
   Gene_id             =  models.CharField(max_length=200)
   Tpm                 =  models.CharField(max_length=200)
   Treatment_codenumber=  models.CharField(max_length=200)#id = models.AutoField(primary_key=True)
   #SRP_SRR_A_G_T_S_T_L_GENE_TPM = models.CharField(max_length=200)
   
 #'%s = models.CharField(db_column="%s",max_length=20)'%(' '.join(df_hor_c[y].split('.')),df_hor_c[y])



# Create your models here.
