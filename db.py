# ./db_create.py
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hor_DB.settings'

database_name = settings.DATABASES['default']['NAME']
database_url = 'sqlite:////%s'%database_name
engine = create_engine(database_url, echo=False)
df_django = pd.read_csv('last_option.csv',sep =',')  
df_django.to_sql('leeu', engine,if_exists='append',index=False)  

