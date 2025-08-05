package com.fdmgroup.SpringProject2.model;

import jakarta.persistence.Entity;

@Entity
public class Company extends Customer{

	public Company(String name, Address address) {
		super(name, address);
	}
	
	public Company(){}
	
	public void chargeAllAccounts(double amount) {
		for (Account account : getAccounts()) {
			if (account instanceof CheckingAccount) {
				double newCheckingAccountBalance = account.getBalance() - amount;
				account.setBalance(newCheckingAccountBalance);	
			}
			else {
				double newSavingsAccountBalance = account.getBalance() - (amount * 2);
				account.setBalance(newSavingsAccountBalance);
			}
		}

	}
}
