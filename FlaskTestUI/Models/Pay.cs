using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace FlaskTestUI.Models
{
    public class Pay
    {
        public object date { get; set; }
        public string time { get; set; }
        public object timestamp { get; set; }
        public int globaltransid { get; set; }
        public string transtype { get; set; }
        public string securitycode { get; set; }
        public int orderid { get; set; }
        public bool isbid { get; set; }
        public double price { get; set; }
        public int volume { get; set; }
        public double value { get; set; }
        public int uvolume { get; set; }
        public string housecode { get; set; }
        public string tagbistorderid { get; set; }
        public string taggeniumuser { get; set; }
        public string tagmember_accountid { get; set; }
        public string taginvestorid_cra_bist_ { get; set; }
        public string taginvestorname_investorid_ { get; set; }
    }

    public class Root
    {
        public List<Pay> Pay { get; set; }

    }
}
