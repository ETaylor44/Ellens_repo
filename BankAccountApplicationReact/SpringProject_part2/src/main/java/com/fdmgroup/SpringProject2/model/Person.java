package com.fdmgroup.SpringProject2.model;

import jakarta.persistence.Entity;

@Entity
public class Person extends Customer{
	
	// Constructor
	public Person(String name, Address address) {
		super(name, address);
	}
	
	public Person(){}
	
	// Method
	public void chargeAllAccounts(double amount) {
		for (Account account : getAccounts()) {
			double newBalance = account.getBalance() - amount;
			account.setBalance(newBalance);
		}
	}
}
