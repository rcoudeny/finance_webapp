using System;
using System.ComponentModel.DataAnnotations;

namespace dotnet.Models.DTOs.Requests
{
    public class UserRegistrationDTO
    {
        [Required]
        [EmailAddress]
        public string Email { get; set; }
        [Required]
        public string UserName { get; set; }
        [Required]
        public string Password { get; set; }


        public UserRegistrationDTO()
        {
        }
    }
}
