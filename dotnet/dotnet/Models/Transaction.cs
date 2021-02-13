using System;
using System.ComponentModel.DataAnnotations;

namespace dotnet.Models
{
    public class Transaction
    {
        [Key]
        public Guid Id { get; set; }
        public DateTime Date { get; set; }

        [Required]
        public Double Amount { get; set; }
        public String OpponentName { get; set; }
        public String OpponentAccount { get; set; }
        public String Comment { get; set; }
        public String OwnAccount { get; set; }
    }
}
