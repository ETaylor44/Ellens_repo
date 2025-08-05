package com.fdmgroup.SpringProject2.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;

@Entity
public class SavingsAccount extends Account{
	
	@Column(name = "INTEREST_RATE", nullable = false)
	private double interestRate;
	
	public SavingsAccount(){}
	
	public SavingsAccount(double balance, Customer customer, double interestRate){//, String type) {
		super(balance, customer);//, type);
		this.interestRate = interestRate;
	}
	
	
	// Method
	public void addInterest() {
		setBalance(getBalance() * (interestRate / 100));
	}
	
	@Override 
	public double withdraw(double amount) {
		if (amount <= getBalance()) {
			setBalance(getBalance() - amount);
			return getBalance();
		}
		else {
			System.out.println("You cannot withdraw a value greater than your balance.");
			return 0;
		}
	}
	
	// Getter and setter
	public double getInterestRate() {
		return interestRate;
	}
	
	public void setInterestRate(double rate) {
		interestRate = rate;
	}

}
