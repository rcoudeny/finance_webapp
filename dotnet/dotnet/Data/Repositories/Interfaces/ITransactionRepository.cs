using System;
using System.Collections.Generic;
using dotnet.Models;

namespace dotnet.Data.Repositories.Interfaces
{
    public interface ITransactionRepository
    {
        Transaction GetById(Guid id);
        IEnumerable<Transaction> GetAll();
        void Add(Transaction transaction);
        void Delete(Transaction transaction);
        void Update(Transaction transaction);
        void SaveChanges();
    }
}
