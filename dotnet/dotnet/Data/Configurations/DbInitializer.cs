using System;
using System.Globalization;
using System.IO;
using System.Threading.Tasks;
using dotnet.Models;

namespace dotnet.Data.Configurations
{
    public class FinanceInitializer
    {

        private readonly FinanceContext _dbContext;
        public FinanceInitializer(FinanceContext dbContext)
        {
            _dbContext = dbContext;
        }

        public void InitializeData()
        {
            _dbContext.Database.EnsureDeleted();
            if (_dbContext.Database.EnsureCreated())
            {
                Category category = new Category();
                category.Name = "Main";

                using (var reader = new StreamReader(@"Controllers/searchMovement.csv"))
                {
                    while (!reader.EndOfStream)
                    {
                        var line = reader.ReadLine();
                        var values = line.Split(";");
                        Transaction transaction = new Transaction();
                        transaction.Date = DateTime.ParseExact(values[0], "dd/MM/yyyy", CultureInfo.InvariantCulture);
                        transaction.Amount = Convert.ToDouble(values[1]);
                        transaction.OpponentName = values[3];
                        transaction.OpponentAccount = values[4];
                        transaction.Comment = values[6];
                        transaction.OwnAccount = values[7];
                        category.AddTransaction(transaction);
                    }
                }
                _dbContext.Categories.Add(category);
                _dbContext.SaveChanges();
            }
        }
    }
}
