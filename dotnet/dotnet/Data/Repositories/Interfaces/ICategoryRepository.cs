using System;
using System.Collections.Generic;
using dotnet.Models;

namespace dotnet.Data.Repositories.Interfaces
{
    public interface ICategoryRepository
    {
        Category GetById(Guid id);
        IEnumerable<Category> GetAll();
        void Add(Category category);
        void Delete(Category category);
        void Update(Category category);
        void SaveChanges();
    }
}
