package com.fdmgroup.SpringProject2.converter;

import com.fdmgroup.SpringProject2.dto.CustomerDTO;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.model.Person;
import com.fdmgroup.SpringProject2.repository.AccountRepository;
import com.fdmgroup.SpringProject2.repository.AddressRepository;
import com.fdmgroup.SpringProject2.model.Account;
import com.fdmgroup.SpringProject2.model.Company;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.boot.autoconfigure.amqp.RabbitConnectionDetails.Address;
import org.springframework.stereotype.Component;

@Component
public class CustomerConverter {

	private final AccountRepository accountRepo;
	private final AddressRepository addressRepo;
	
	public CustomerConverter(AccountRepository accountRepo, AddressRepository addressRepo) {
		this.accountRepo = accountRepo;
		this.addressRepo = addressRepo;
	}
	
	public Customer toEntity(CustomerDTO dto) {
		List<Account> accounts = dto.getAccounts().stream()
				.map(accountId -> accountRepo.findById(accountId).get())
				.collect(Collectors.toList());	
		if (dto.getType().equals("person")) {
			Person person = new Person();
			person.setCustomerId(dto.getCustomerId());
			person.setName(dto.getName());
			person.setAddress(dto.getAddress());
			person.setAccounts(accounts);
			return person;
		}
		else {
			Company company = new Company();
			company.setCustomerId(dto.getCustomerId());
			company.setName(dto.getName());
			company.setAddress(dto.getAddress());
			company.setAccounts(accounts);
			return company;
		}
		
	}
	
	public CustomerDTO toDTO(Customer customer) {
		CustomerDTO customerDTO = new CustomerDTO();
		List<Long> accountsIds = customer
				.getAccounts()
				.stream()
				.map(account -> account.getAccountId())
				.collect(Collectors.toList());
		
		customerDTO.setCustomerId(customer.getCustomerId());
		customerDTO.setName(customer.getName());
		customerDTO.setAddress(customer.getAddress());
		customerDTO.setAccounts(accountsIds);		
		if (customer.getClass().getSimpleName().equals("Person")) {
			customerDTO.setType(customer.getType());
		}
		else {
			customerDTO.setType(customer.getType());
		}
		return customerDTO;
		
	}
}
