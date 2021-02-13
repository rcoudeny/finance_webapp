using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using dotnet.Data.Repositories.Interfaces;
using dotnet.Models;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace dotnet.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CategoryController : ControllerBase
    {

        private readonly ICategoryRepository categoryRepository;

        public CategoryController(ICategoryRepository context)
        {
            categoryRepository = context;
        }

        [HttpGet]
        public IEnumerable<Category> Index()
        {
            return categoryRepository.GetAll().ToList();
        }
    }
}
