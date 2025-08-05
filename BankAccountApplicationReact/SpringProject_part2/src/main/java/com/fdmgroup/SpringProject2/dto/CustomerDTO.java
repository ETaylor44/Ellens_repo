package com.fdmgroup.SpringProject2.dto;

import java.util.List;
import java.util.ArrayList;


import com.fdmgroup.SpringProject2.model.Address;

public class CustomerDTO {
	
	private String type;
	private long customerId;
	private String name;
	private Address address;
	//private long addressId;
	private List<Long> accounts = new ArrayList<Long>();
	
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	
	public long getCustomerId() {
		return customerId;
	}
	public void setCustomerId(long customerId) {
		this.customerId = customerId;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Address getAddress() {
		return address;
	}
	public void setAddress(Address address) {
		this.address = address;
	}
	public List<Long> getAccounts() {
		return accounts;
	}
//	public long getAddressId() {
//		return addressId;
//	}
//	public void setAddressId(long addressId) {
//		this.addressId = addressId;
//	}
	public void setAccounts(List<Long> accounts) {
		this.accounts = accounts;
	}

}
