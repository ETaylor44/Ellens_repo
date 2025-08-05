package com.fdmgroup.SpringProject2.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity(name = "ADDRESS")
public class Address {
	
	@Id @GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "ADDRESS_ID")
	private long addressId;
	@Column(name = "STREET_NUMBER", nullable = false, updatable = false)
	private String streetNumber;
	@Column(name = "CITY", nullable = false)
	private String city;
	@Column(name = "POSTAL_CODE", nullable = false)
	private String postalCode;
	@Column(name = "PROVINCE", nullable = false)
	private String province;
	
	public Address(String streetNumber, String postalCode, String city, String province) {
		this.streetNumber = streetNumber;
		this.postalCode = postalCode;
		this.city = city;
		this.province = province;
	}
	
	Address(){}

	public long getAddressId() {
		return addressId;
	}

	public void setAddressId(long addressId) {
		this.addressId = addressId;
	}

	public String getStreetNumber() {
		return streetNumber;
	}

	public String getPostalCode() {
		return postalCode;
	}

	public void setPostalCode(String postalCode) {
		this.postalCode = postalCode;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getProvince() {
		return province;
	}

	public void setProvince(String province) {
		this.province = province;
	}
	
	
	
	
	
	

}
