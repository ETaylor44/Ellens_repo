package com.fdmgroup.SpringProject2.dto;

public class AccountDTO {
	private String type;
	private long accountId;
	private double balance;
	private double interestRate;
	private int nextCheckNumber;
	private long customerId;
	
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public long getAccountId() {
		return accountId;
	}
	public void setAccountId(long accountId) {
		this.accountId = accountId;
	}
	public double getBalance() {
		return balance;
	}
	public void setBalance(double balance) {
		this.balance = balance;
	}
	public double getInterestRate() {
		return interestRate;
	}
	public void setInterestRate(double interestRate) {
		this.interestRate = interestRate;
	}
	public int getNextCheckNumber() {
		return nextCheckNumber;
	}
	public void setNextCheckNumber(int nextCheckNumber) {
		this.nextCheckNumber = nextCheckNumber;
	}
	public long getCustomerId() {
		return customerId;
	}
	public void setCustomerId(long customerId) {
		this.customerId = customerId;
	}
	
	
	

}
