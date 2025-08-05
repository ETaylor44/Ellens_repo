package com.fdmgroup.SpringProject2;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.fdmgroup.SpringProject2.model.Address;
import com.fdmgroup.SpringProject2.model.CheckingAccount;
import com.fdmgroup.SpringProject2.model.Company;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.model.Person;
import com.fdmgroup.SpringProject2.model.SavingsAccount;
import com.fdmgroup.SpringProject2.repository.AccountRepository;
import com.fdmgroup.SpringProject2.repository.AddressRepository;
import com.fdmgroup.SpringProject2.repository.CustomerRepository;

@Configuration
public class LoadDatabase {
	
	@Bean
	CommandLineRunner initDatabase(CustomerRepository customerRepo, AddressRepository addressRepo, AccountRepository accountRepo) {
		return args -> {
	
			Address address1 = new Address("13 Kenworth Street", "TR3 3E3", "Toronto",  "Ontario");
			Address address2 = new Address("2 Queen Street", "R43 6Y6", "Caledon" , "Ontario");

			Customer customer1 = new Company("FDM", address1);
			Customer customer2 = new Person("John", address2);
			
			SavingsAccount account1 = new SavingsAccount(2300.0, customer1, 4.5);//, "savings");
			SavingsAccount account2 = new SavingsAccount(45000.0, customer2, 5);//, "savings");
			CheckingAccount account3 = new CheckingAccount(120.0, customer1, 1);//, "checking");

			customerRepo.save(customer1);
			customerRepo.save(customer2);

//			accountRepo.save(account1);
//			accountRepo.save(account2);
//			accountRepo.save(account3);
		};
	}

}
