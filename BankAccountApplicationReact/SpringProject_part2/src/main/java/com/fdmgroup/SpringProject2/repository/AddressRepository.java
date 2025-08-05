package com.fdmgroup.SpringProject2.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.fdmgroup.SpringProject2.model.Address;

public interface AddressRepository extends JpaRepository<Address, Long> {


}
