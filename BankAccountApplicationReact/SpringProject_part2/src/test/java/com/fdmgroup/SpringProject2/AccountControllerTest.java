package com.fdmgroup.SpringProject2;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.bean.override.mockito.MockitoBean;

import com.fdmgroup.SpringProject2.controller.AccountController;
import com.fdmgroup.SpringProject2.exception.AccountNotFoundException;
import com.fdmgroup.SpringProject2.model.Account;
import com.fdmgroup.SpringProject2.model.Address;
import com.fdmgroup.SpringProject2.model.CheckingAccount;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.model.Person;
import com.fdmgroup.SpringProject2.model.SavingsAccount;
import com.fdmgroup.SpringProject2.repository.AccountRepository;
import com.fdmgroup.SpringProject2.repository.CustomerRepository;
import com.fdmgroup.SpringProject2.service.AccountService;

@SpringBootTest
class AccountControllerTest {
	
	@MockitoBean
	AccountRepository mockRepo;
	
	@MockitoBean
	CustomerRepository mockCustRepo;
	
	@Autowired
	AccountService service;
	
	@Autowired
	AccountController controller;

	@Test
	void test_addNewAccount_returnsAccountObject() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");
		SavingsAccount newAccount = new SavingsAccount(1200, newCustomer, 5);
		when(mockCustRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		service.addAccount(newCustomer.getCustomerId(), newAccount);
		verify(mockRepo).save(newAccount);
		when(mockRepo.save(newAccount)).thenReturn(newAccount);
		assertTrue(newAccount instanceof SavingsAccount);
	}
	
	@Test
	void test_listAllAccount_returnsListOfLengthTwo_whenTwoAccountsAreSaved() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");
		Account account1 = new SavingsAccount(1200, newCustomer, 5);
		Account account2 = new CheckingAccount(1200, newCustomer, 1);
		List<Account> accountList = new ArrayList<>(Arrays.asList(account1, account2));
		when(mockRepo.findAll()).thenReturn(accountList);
		when(mockCustRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		controller.addNewAccount(newCustomer.getCustomerId(), (Account)account1);
		controller.addNewAccount(newCustomer.getCustomerId(), (Account)account2);
		controller.getAccounts();
		verify(mockRepo).findAll();
		List<Account> accounts = service.listAllAccounts();
		assertEquals(2, accounts.size());
	}
	
	@Test 
	void test_listAllAccounts_returnsListOfLengthZero_whenZeroAccountsAreSaved() {
		controller.getAccounts();
		verify(mockRepo).findAll();
		List<Account> accounts = service.listAllAccounts();
		assertEquals(0, accounts.size());
	}
	
	@Test
	void test_getAccountById_throwsAccountNotFoundException_whenAccountDoesntExist() {
		Account foundAccount = service.getAccountById(10);
		assertEquals(null, foundAccount);
		assertThrows(AccountNotFoundException.class, () -> {controller.getAccountById(10);});
	}
	
	@Test
	void test_getAccountById_returnsCorrectAccountObject() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");	
		SavingsAccount expectedAccount = new SavingsAccount(1200, newCustomer, 5);
		when(mockCustRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		controller.addNewAccount(newCustomer.getCustomerId(), expectedAccount);
		assertEquals(0, expectedAccount.getAccountId());
		when(mockRepo.findById((long) 0)).thenReturn(Optional.of(expectedAccount));
		Account retrievedAccount = service.getAccountById(expectedAccount.getAccountId());
		verify(mockRepo).findById((long) 0);
		assertEquals(retrievedAccount, expectedAccount);
	}
	
	@Test
	void test_accountService_deleteAccount_returnsTrue_whenAccountIsDeleted() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");	
		SavingsAccount accountToDelete = new SavingsAccount(1200, newCustomer, 5);
		when(mockCustRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		controller.addNewAccount(newCustomer.getCustomerId(), accountToDelete);
		when(mockRepo.existsById(accountToDelete.getAccountId())).thenReturn(true);
		boolean isDeleted = service.deleteAccount(accountToDelete.getAccountId());
		assertTrue(isDeleted);
	}
	
	@Test
	void test_deleteAccount_throwsAccountNotFoundException_whenAccountDoesntExist() {
		Account foundAccount = service.getAccountById(10);
		assertEquals(null, foundAccount);
		assertThrows(AccountNotFoundException.class, () -> {controller.deleteAccount(10);});
	}
	
	@Test
	void test_accountService_updateAccount_returnsUpdatedAccount_whenInterestRateIsUpdated() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");
		SavingsAccount accountToUpdate = new SavingsAccount(1200, newCustomer, 5);
		SavingsAccount updatedAccountDetails = new SavingsAccount(1200, newCustomer, 4);
		when(mockCustRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		controller.addNewAccount(newCustomer.getCustomerId(), accountToUpdate);
		when(mockRepo.findById(accountToUpdate.getAccountId())).thenReturn(Optional.of(accountToUpdate));
		controller.updateAccount(accountToUpdate.getAccountId(), updatedAccountDetails);
		verify(mockRepo).save(accountToUpdate);
		assertEquals(4, accountToUpdate.getInterestRate());
	}
	
	@Test
	void test_accountService_updateAccount_returnsUpdatedAccount_whenNextCheckNumberIsUpdated() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");
		CheckingAccount accountToUpdate = new CheckingAccount(1200, newCustomer, 1);
		CheckingAccount updatedAccountDetails = new CheckingAccount(1200, newCustomer, 2);
		when(mockCustRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		controller.addNewAccount(newCustomer.getCustomerId(), accountToUpdate);
		when(mockRepo.findById(accountToUpdate.getAccountId())).thenReturn(Optional.of(accountToUpdate));
		controller.updateAccount(accountToUpdate.getAccountId(), updatedAccountDetails);
		verify(mockRepo).save(accountToUpdate);
		assertEquals(2, accountToUpdate.getNextCheckNumber());
	}
	
	@Test
	void test_accountService_findAccounByCity_returnsCorrectListOfAccounts() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");
		SavingsAccount account1 = new SavingsAccount(1200, newCustomer, 5);
		SavingsAccount account2 = new SavingsAccount(10, newCustomer, 4);
		when(mockCustRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		controller.addNewAccount(newCustomer.getCustomerId(), account1);
		controller.addNewAccount(newCustomer.getCustomerId(), account2);
		controller.findAccountByCity("Edinburgh");
		verify(mockRepo).findAccountByCity("Edinburgh");
	}
	


}
