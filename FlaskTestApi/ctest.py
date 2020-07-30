# %%
import smarts as SM
import datetime

def result():
    order_template = """
    SELECT date, time, timestamp, globaltransid, transtype, securitycode, 
           orderid, isbid, price, volume, value, uvolume, housecode,  
           tagbistorderid, taggeniumuser, tagmember_accountid, taginvestorid_cra_bist_, taginvestorname_investorid_
      FROM bistorderlog
     WHERE date BETWEEN '{v_itr1}'  AND '{v_itr2}' 
       AND securitycode = '{v_menkul}' 
       AND amfof = false AND amfcx = false
       AND transtype <> 'TRADE'
    ORDER BY globaltransid    
    """
    #'   AND taginvestorid_cra_bist_ IN {sql_yatgrup} 
    trade_template = """
      SELECT date, time, timestamp, globaltransid, transtype, securitycode, 
           tradeid, price, volume, value,
           tradetagbisttradeid, 
           bidtagbistorderid, bidtaggeniumuser, bidtagmember_accountid, bidtaginvestorid_cra_bist_, bidtaginvestorname_investorid_,  
           asktagbistorderid, asktaggeniumuser, asktagmember_accountid, asktaginvestorid_cra_bist_, asktaginvestorname_investorid_ 
      FROM bisttrade
     WHERE date BETWEEN '{v_itr1}'  AND '{v_itr2}' 
       AND transtype = 'TRADE'
       AND securitycode = '{v_menkul}' 
       AND tradeamfof = false AND tradeamfcx = false
    ORDER BY globaltransid    
    """

    #'   AND (bidtaginvestorname_investorid_ IN {sql_yatgrup} OR asktaginvestorname_investorid_ IN {sql_yatgrup}  )
   
    v_menkul = "POLHO.E"
    v_itr1 = '2018-12-07'
    v_itr2 = '2018-12-07'

    v_yatgrup = '13845214 MTY-18846 13971039 31403231 13865877 28669287 GDK-141209 12573707 12747049 12353196 '
    list_yatgrup = list(v_yatgrup.split())
    sql_yatgrup = "('" + "', '".join(list_yatgrup) + "')"            
                        
    sql_format = {'v_menkul'    :   v_menkul, 
                  'v_itr1'      :   v_itr1, 
                  'v_itr2'      :   v_itr2, 
                  'sql_yatgrup' :   sql_yatgrup
                 }
    #ME.sql_clipb(order_template, sql_format)
    df = SM.get_df(order_template, sql_format)

    #dfJson = df.head().to_json()

    dfJson = df.head().to_json(orient='records')

    return dfJson

# %%