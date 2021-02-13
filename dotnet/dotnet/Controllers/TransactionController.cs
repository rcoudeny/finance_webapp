using System;
using System.Collections.Generic;
using dotnet.Data.Repositories.Interfaces;
using dotnet.Models;
using Microsoft.AspNetCore.Mvc;

namespace dotnet.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TransactionController : ControllerBase
    {
        private readonly ITransactionRepository transactionRepository;
        public TransactionController(ITransactionRepository context)
        {
            transactionRepository = context;
        }

        [HttpGet]
        public IEnumerable<Transaction> Index()
        {
            return transactionRepository.GetAll();
        }
    }
}
