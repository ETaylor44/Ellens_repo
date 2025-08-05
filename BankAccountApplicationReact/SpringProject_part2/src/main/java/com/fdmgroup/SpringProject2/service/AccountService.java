package com.fdmgroup.SpringProject2.service;

import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.fdmgroup.SpringProject2.converter.AccountConverter;
import com.fdmgroup.SpringProject2.dto.AccountDTO;
import com.fdmgroup.SpringProject2.exception.AccountNotFoundException;
import com.fdmgroup.SpringProject2.exception.CustomerNotFoundException;
import com.fdmgroup.SpringProject2.model.Account;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.repository.AccountRepository;
import com.fdmgroup.SpringProject2.repository.CustomerRepository;

@Service
public class AccountService {
	
	private AccountRepository accountRepo;
	private CustomerRepository customerRepo;
	private final AccountConverter accountConverter;
	
	@Autowired
	public AccountService(AccountRepository accountRepo, CustomerRepository customerRepo, AccountConverter accountConverter) {
		this.accountRepo = accountRepo;
		this.customerRepo = customerRepo;
		this.accountConverter = accountConverter;
	}
	
	public AccountDTO addAccount(long id, AccountDTO dto) {
		Optional<Customer> customer = customerRepo.findById(id);
		if (customer.isPresent()) {
			Account account = accountConverter.toEntity(dto);
			account = accountRepo.save(account);
			return accountConverter.toDTO(account);
		}
		else {
			throw new CustomerNotFoundException("id " + id);
		}
	}
	
	public List<AccountDTO> listAllAccounts() {
		return accountRepo.findAll().stream()
				.map(accountConverter::toDTO)
				.collect(Collectors.toList());
	}
	
	public AccountDTO getAccountById(long id) {
		Account accountFound = accountRepo.findById(id)
				.orElseThrow(() -> new AccountNotFoundException("id " + id));
		return accountConverter.toDTO(accountFound);
	}

//	public AccountDTO updateAccount(Account accountToUpdate) {
//        if (accountRepo.existsById(accountToUpdate.getAccountId())){
//        	accountRepo.save(accountToUpdate);
//        	return accountToUpdate;
//        }
//        
//        return null;
//	}

	public void deleteAccount(long id) {
		if (accountRepo.existsById(id)) {
			accountRepo.deleteById(id);
		}
		else {
			throw new AccountNotFoundException("id " + id);
		}
	}


	public List<AccountDTO> findAccountByCity(String city){
		List<AccountDTO> dtos = new ArrayList<AccountDTO>();
		List<Account> accounts = accountRepo.findAccountByCity(city);
		for (Account account : accounts) {
			AccountDTO dto = accountConverter.toDTO(account);
			dtos.add(dto);
		}
		return dtos;
		
	}

}
