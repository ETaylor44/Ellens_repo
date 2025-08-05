package com.fdmgroup.SpringProject2.model;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonSubTypes;

import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonSubTypes.Type;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Inheritance;
import jakarta.persistence.InheritanceType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Transient;

@JsonTypeInfo( use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "type")
@JsonSubTypes({ 
  @Type(value = SavingsAccount.class, name = "savings"), 
  @Type(value = CheckingAccount.class, name = "checking"), 
})
@Entity(name = "ACCOUNT")
@Inheritance(strategy = InheritanceType.JOINED)
public abstract class Account {
	
	// Attributes
	@Id 
	@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "accountseq")
	@SequenceGenerator(name = "accountseq", sequenceName = "accountseq", allocationSize = 1)
	private long accountId;
	private double balance;
	//private String type;
	
	@ManyToOne
	@JoinColumn(name = "FK_CUST_ID")
	@JsonBackReference
	private Customer customer;
	
	// Constructor
	public Account(double balance, Customer customer) {//, String type) {
		this.balance = balance;
		this.customer = customer;
		//this.type = getType();
	}
	
	Account(){}
	
	// Methods
	public double withdraw(double amount){
		balance -= amount;
		return amount;
	}
	
	public void deposit(double amount) {
		balance += amount;
	}
	
	public void correctBalance(double amount) {
		balance = amount;
	}
	
	// Getters and setters
	public long getAccountId() {
		return accountId;
	}
	
	public double getBalance() {
		return balance;
	}
	
	public void setBalance(double balance) {
		this.balance = balance;
	}
	
	public String getType() {
		if (this.getClass() == SavingsAccount.class)
		{
			return "savings";
		}
		else
		{
			return "checking";
		}
	}

	public Customer getCustomer() {
		return customer;
	}

	public void setCustomer(Customer customer) {
		this.customer = customer;
	}
	
	
	
}