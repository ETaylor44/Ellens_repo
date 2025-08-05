package com.fdmgroup.SpringProject2.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.fdmgroup.SpringProject2.model.Customer;

public interface CustomerRepository extends JpaRepository<Customer, Long> {	

}
