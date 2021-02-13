using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace dotnet.Models
{
    public class Category
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public String Name { get; set; }
        public List<Category> SubCategories { get; set; }
        public List<Transaction> Transactions { get; set; }

        public Category()
        {
            SubCategories = new List<Category>();
            Transactions = new List<Transaction>();
        }


        public void AddTransaction(Transaction transaction)
        {
            Transactions.Add(transaction);
        }
    }
}
