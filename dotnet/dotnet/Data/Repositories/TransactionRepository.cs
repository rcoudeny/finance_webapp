using System;
using System.Collections.Generic;
using System.Linq;
using dotnet.Data.Repositories.Interfaces;
using dotnet.Models;
using Microsoft.EntityFrameworkCore;

namespace dotnet.Data.Repositories
{
    public class TransactionRepository : ITransactionRepository
    {

        private readonly FinanceContext _dbContext;
        private readonly DbSet<Transaction> _transactions;
        public TransactionRepository(FinanceContext dbContext)
        {
            _dbContext = dbContext;
            _transactions = dbContext.Transactions;
        }

        public Transaction GetById(Guid id)
        {
            return _transactions.SingleOrDefault(t => t.Id == id);
        }

        public void Add(Transaction transaction)
        {
            _transactions.Add(transaction);
        }

        public void Delete(Transaction transaction)
        {
            _transactions.Remove(transaction);
        }

        public IEnumerable<Transaction> GetAll()
        {
            return _transactions;
        }


        public void SaveChanges()
        {
            _dbContext.SaveChanges();
        }

        public void Update(Transaction transaction)
        {
            _dbContext.Update(transaction);
        }
    }
}
