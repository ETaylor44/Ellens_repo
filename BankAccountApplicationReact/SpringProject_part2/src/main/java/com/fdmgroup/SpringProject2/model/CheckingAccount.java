package com.fdmgroup.SpringProject2.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;

@Entity(name = "CHECKING_ACCOUNT")
public class CheckingAccount extends Account{
	
	@Column(name = "NEXT_CHECK_NUMBER", nullable = false)
	private int nextCheckNumber;
	
	// Constructor
	public CheckingAccount(double balance, Customer customer, int nextCheckNumber) {//, String type) {
		super(balance, customer);//, type);
		this.nextCheckNumber = nextCheckNumber;
	}
	
	public CheckingAccount(){}
	
	// Getter and setter
	public int getNextCheckNumber() {
		return nextCheckNumber;
	}
	
	public void setNextCheckNumber(int nextCheckNumber) {
		this.nextCheckNumber = nextCheckNumber;
	}
}
