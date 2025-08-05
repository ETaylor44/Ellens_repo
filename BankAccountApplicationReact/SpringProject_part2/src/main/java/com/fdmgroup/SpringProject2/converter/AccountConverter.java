package com.fdmgroup.SpringProject2.converter;

import org.springframework.stereotype.Component;

import com.fdmgroup.SpringProject2.dto.AccountDTO;
import com.fdmgroup.SpringProject2.model.Account;
import com.fdmgroup.SpringProject2.model.CheckingAccount;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.model.SavingsAccount;
import com.fdmgroup.SpringProject2.repository.CustomerRepository;

@Component
public class AccountConverter {
	private CustomerRepository customerRepo;
	
	public AccountConverter(CustomerRepository customerRepo) {
		this.customerRepo = customerRepo;
	}
	
	public Account toEntity(AccountDTO dto) {
		Customer foundCustomer = customerRepo.findById(dto.getCustomerId()).get();
		
		if (dto.getType().equals("savings")) {
			SavingsAccount savingsAccount = new SavingsAccount();
			savingsAccount.setBalance(dto.getBalance());
			savingsAccount.setInterestRate(dto.getInterestRate());
			savingsAccount.setCustomer(foundCustomer);
			return savingsAccount;
		}
		else {
			CheckingAccount checkingAccount = new CheckingAccount();
			checkingAccount.setBalance(dto.getBalance());
			checkingAccount.setNextCheckNumber(dto.getNextCheckNumber());
			checkingAccount.setCustomer(foundCustomer);
			return checkingAccount;
		}
	}
	
	public AccountDTO toDTO(Account account) {
		AccountDTO dto = new AccountDTO();
		
		dto.setAccountId(account.getAccountId());
		dto.setBalance(account.getBalance());
		dto.setCustomerId(account.getCustomer().getCustomerId());
		
		if (account.getClass().getSimpleName().equals("SavingsAccount")) {
			dto.setType("savings");
			dto.setInterestRate(((SavingsAccount)account).getInterestRate());
			return dto;
		}
		else {
			dto.setType("checking");
			dto.setNextCheckNumber(((CheckingAccount)account).getNextCheckNumber());
			return dto;
		}
	}

}
