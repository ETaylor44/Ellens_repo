using System.Security.Cryptography.X509Certificates;

namespace reading_csvs
{
    public class Person
    {
        public string FirstName { get; set; }
        public string Surname { get; set; }
        public int Age { get; set; }
        public string Gender { get; set; }

        public Person(string newFirstName, string newSurname, int newAge, string newGender)
        {
            FirstName = newFirstName;
            Surname = newSurname;
            Age = newAge;
            Gender = newGender;
        }


        public List<string> dataAsList()
        {
            List<string> data = new List<string>();
            data.Add(FirstName);
            data.Add(Surname);
            data.Add(Age.ToString());
            data.Add(Gender);
            return data;
        }

        
   
    }
}
