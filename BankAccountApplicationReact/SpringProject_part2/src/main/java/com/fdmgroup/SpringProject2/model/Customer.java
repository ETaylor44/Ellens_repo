package com.fdmgroup.SpringProject2.model;

import java.util.ArrayList;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonSubTypes.Type;
import com.fasterxml.jackson.annotation.JsonTypeInfo;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.DiscriminatorColumn;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Inheritance;
import jakarta.persistence.InheritanceType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Transient;

@JsonTypeInfo( use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "type")
@JsonSubTypes({ 
  @Type(value = Person.class, name = "person"), 
  @Type(value = Company.class, name = "company"), 
})
@Entity(name = "CUSTOMER")
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "CUSTOMER_TYPE")
public abstract class Customer {
	
	// Attributes
	@Id 
	@SequenceGenerator(name = "customerIdSeq", initialValue = 1001)
    @GeneratedValue(generator = "customerIdSeq")
	@Column(name = "CUSTOMER_ID")
	private long customerId;
	
	@Column(name = "CUSTOMER_NAME", nullable = false)
	private String name;
	
	@OneToOne(cascade = {CascadeType.PERSIST, CascadeType.MERGE})
	@JoinColumn(name = "FK_ADDRESS_ID")
	private Address address;
	
	@OneToMany(mappedBy = "customer", cascade = {CascadeType.MERGE, CascadeType.PERSIST})
	private List<Account> accounts;
		
	// Constructor
	public Customer(String name, Address address) {
		this.name = name;
		this.address = address;
		accounts = new ArrayList<Account>();
	}
	
	// Database constructor
	Customer(){}
		
	// Methods
	public void addAccount(Account account) {
		accounts.add(account);
	}
	
	public void removeAccount(Account account) {
		accounts.remove(account);
	}
	
	public abstract void chargeAllAccounts(double amount);
	
	// Getters and setters
	public List<Account> getAccounts(){
		return accounts;
	}
	
	public long getCustomerId() {
		return customerId;
	}
	
	public String getName() {
		return name;
	}
	
	public Address getAddress() {
		return address;
	}
		
	public void setName(String name) {
		this.name = name;
	}

	public void setAddress(Address address) {
		this.address = address;
		
	}
	
	public void setCustomerId(long customerId) {
		this.customerId = customerId;
	}

	public String getType() {
		if (this.getClass() == Person.class)
		{
			return "person";
		}
		else
		{
			return "company";
		}
	}

	public void setAccounts(List<Account> accounts) {
		this.accounts = accounts;
	}

}

