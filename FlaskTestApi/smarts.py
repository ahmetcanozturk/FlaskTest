# %%
import numpy as np
import pandas as pd
import sqlalchemy as sa
import os

"""
    DataFrame listesini excel dosyasına farklı sayfalar şeklinde kaydeder
"""

def open_excel(filename, df_list=[]):
#    filename = filename.str.strip().str.lower().str.replace(' ', '_')
    
    mysh_name = filename.split('.')[0]
    with pd.ExcelWriter(filename) as pdx:
        for i, df in enumerate(df_list):
            if df.shape[0] * df.shape[1] > 1000000:
                raise SystemExit
            df.to_excel(pdx, sheet_name=mysh_name+'_'+str(i+1))
    os.startfile(filename)
    
def to_clipb(df):
    df.to_clipboard()

        
        
def get_df(sql_template, sql_format):
    engine = sa.create_engine('postgresql://kckaraagac:1+kC12kA14rA30!716aG3018aC104640120@10.10.20.162:8032/mplsql')
    sqlstring = sql_template.format(**sql_format)
    
    df = pd.read_sql(sqlstring, engine)
    return df

def sql_clipb(sql_template, sql_format):
    sqlstring = sql_template.format(**sql_format)
    
#    str_array = pd.Series(sqlstring.split("\n"))
    df = pd.DataFrame({" ":sqlstring}, index=[" "] )
#    print (str_array)
    
    to_clipb(df)

# %%