using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using FlaskTestUI.Models;
using System.Net.Http;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace FlaskTestUI.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public async Task<IActionResult> Test()
        {
            var list = new List<Pay>();
            using (var httpClient = new HttpClient())
            {
                using (var response = await httpClient.GetAsync("http://localhost:5555/test"))
                {
                    string apiResponse = await response.Content.ReadAsStringAsync();
                    int first = apiResponse.IndexOf("[");
                    int last = apiResponse.LastIndexOf("]");
                    var sonuc = apiResponse.Substring(first, last);
                    sonuc = sonuc.Replace("\\\"", "'");

                    list = JsonConvert.DeserializeObject<List<Pay>>(sonuc);
                }
            }
            return View(list);
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
