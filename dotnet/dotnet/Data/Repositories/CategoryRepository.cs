using System;
using System.Collections.Generic;
using System.Linq;
using dotnet.Data.Repositories.Interfaces;
using dotnet.Models;
using Microsoft.EntityFrameworkCore;

namespace dotnet.Data.Repositories
{
    public class CategoryRepository : ICategoryRepository
    {

        private readonly FinanceContext _dbContext;
        private readonly DbSet<Category> _categories;
        public CategoryRepository(FinanceContext dbContext)
        {
            _dbContext = dbContext;
            _categories = dbContext.Categories;
        }

        public Category GetById(Guid id)
        {
            return _categories.SingleOrDefault(t => t.Id == id);
        }

        public void Add(Category Category)
        {
            _categories.Add(Category);
        }

        public void Delete(Category Category)
        {
            _categories.Remove(Category);
        }

        public IEnumerable<Category> GetAll()
        {
            return _categories.Include(c => c.Transactions.OrderBy(t => t.Date));
        }


        public void SaveChanges()
        {
            _dbContext.SaveChanges();
        }

        public void Update(Category Category)
        {
            _dbContext.Update(Category);
        }
    }
}
