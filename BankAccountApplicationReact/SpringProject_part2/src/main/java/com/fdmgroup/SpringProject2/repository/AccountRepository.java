package com.fdmgroup.SpringProject2.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.fdmgroup.SpringProject2.model.Account;

public interface AccountRepository extends JpaRepository<Account, Long> {

	@Query("SELECT a FROM ACCOUNT a WHERE a.customer.address.city = :city")
	List<Account> findAccountByCity(@Param("city")String city);
}
