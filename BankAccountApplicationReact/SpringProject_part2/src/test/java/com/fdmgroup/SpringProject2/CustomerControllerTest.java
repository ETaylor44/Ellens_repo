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

import com.fdmgroup.SpringProject2.controller.CustomerController;
import com.fdmgroup.SpringProject2.exception.CustomerNotFoundException;
import com.fdmgroup.SpringProject2.model.Account;
import com.fdmgroup.SpringProject2.model.Address;
import com.fdmgroup.SpringProject2.model.Company;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.model.Person;
import com.fdmgroup.SpringProject2.model.SavingsAccount;
import com.fdmgroup.SpringProject2.repository.AccountRepository;
import com.fdmgroup.SpringProject2.repository.CustomerRepository;
import com.fdmgroup.SpringProject2.service.AccountService;
import com.fdmgroup.SpringProject2.service.CustomerService;

@SpringBootTest
class CustomerControllerTest {
	
	@MockitoBean
	CustomerRepository mockRepo;
	
	@MockitoBean
	AccountRepository mockAccRepo;
	
	@Autowired
	AccountService accService;
	
	@Autowired
	CustomerService service;
	
	@Autowired
	CustomerController controller;

	
	@Test
	void test_addNewCustomer_returnsCustomerObject() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");	
		service.addCustomer(newCustomer);
		verify(mockRepo).save(newCustomer);
		when(mockRepo.save(newCustomer)).thenReturn(newCustomer);
		assertTrue(newCustomer instanceof Person);
	}
	
	@Test
	void test_listAllCustomers_returnsListOfLengthTwo_whenTwoCustomersAreSaved() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer customer1 = new Person("Ellen Taylor", newAddress, "person");	
		Customer customer2 = new Person("Father Christmas", newAddress, "person");	
		List<Customer> customerList = new ArrayList<>(Arrays.asList(customer1, customer2));
		when(mockRepo.findAll()).thenReturn(customerList);
		controller.addNewCustomer(customer1);
		controller.addNewCustomer(customer2);
		controller.getCustomers();
		verify(mockRepo).findAll();
		List<Customer> customers = service.listAllCustomers();
		assertEquals(2, customers.size());
	}
	
	@Test 
	void test_listAllCustomers_returnsListOfLengthZero_whenZeroCustomersAreSaved() {
		controller.getCustomers();
		verify(mockRepo).findAll();
		List<Customer> customers = service.listAllCustomers();
		assertEquals(0, customers.size());
	}
	
	@Test
	void test_getCustomerById_throwsCustomerNotFoundException_whenCustomerDoesntExist() {
		Customer foundCustomer = service.getCustomerById(10);
		assertEquals(null, foundCustomer);
		assertThrows(CustomerNotFoundException.class, () -> {controller.getCustomerById(10);});
	}
	
	@Test
	void test_getCustomerById_returnsCorrectCustomerObject() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer expectedCustomer = new Person("Ellen Taylor", newAddress, "person");	
		controller.addNewCustomer(expectedCustomer);
		assertEquals(0, expectedCustomer.getCustomerId());
		when(mockRepo.findById((long) 0)).thenReturn(Optional.of(expectedCustomer));
		Customer retrievedCustomer = service.getCustomerById(expectedCustomer.getCustomerId());
		verify(mockRepo).findById((long) 0);
		assertEquals(retrievedCustomer, expectedCustomer);
	}
	
	@Test
	void test_customerService_deleteCustomer_returnsTrue_when_customerIsDeleted() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer customerToDelete = new Person("Ellen Taylor", newAddress, "person");	
		controller.addNewCustomer(customerToDelete);
		when(mockRepo.existsById(customerToDelete.getCustomerId())).thenReturn(true);
		boolean isDeleted = service.deleteCustomer(customerToDelete.getCustomerId());
		assertTrue(isDeleted);
	}
	
	@Test
	void test_deleteCustomer_throwsCustomerNotFoundException_whenCustomerDoesntExist() {
		Customer foundCustomer = service.getCustomerById(10);
		assertEquals(null, foundCustomer);
		assertThrows(CustomerNotFoundException.class, () -> {controller.deleteCustomer(10);});
	}
	
	@Test
	void test_customerService_updateCustomer_returnsUpdatedCustomer() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer customerToUpdate = new Person("Ellen Taylor", newAddress, "person");
		Customer updatedCustomerDetails = new Person("new name", newAddress, "person");	
		controller.addNewCustomer(customerToUpdate);
		when(mockRepo.findById(customerToUpdate.getCustomerId())).thenReturn(Optional.of(customerToUpdate));
		controller.updateCustomer(customerToUpdate.getCustomerId(), updatedCustomerDetails);
		verify(mockRepo).save(customerToUpdate);
		assertEquals("new name", customerToUpdate.getName());
	}
	
	@Test
	void test_getCustomersByType_returnsListOfPerson_whenPersonIsPassedIn() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer customer1 = new Person("Ellen Taylor", newAddress, "person");	
		Customer customer2 = new Company("Father Christmas", newAddress, "company");	
		controller.addNewCustomer(customer1);
		controller.addNewCustomer(customer2);
		List<Customer> customerList = new ArrayList<>(Arrays.asList(customer1, customer2));
		when(mockRepo.findAll()).thenReturn(customerList);
		List<Customer> persons = service.getCustomersByType("person");
		assertEquals(1, persons.size());
		assertTrue(persons.get(0) instanceof Person);
	}
	
	@Test
	void test_getCustomersByType_returnsListOfCompany_whenCompanyIsPassedIn() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer customer1 = new Person("Ellen Taylor", newAddress, "person");	
		Customer customer2 = new Company("Father Christmas", newAddress, "company");	
		controller.addNewCustomer(customer1);
		controller.addNewCustomer(customer2);
		List<Customer> customerList = new ArrayList<>(Arrays.asList(customer1, customer2));
		when(mockRepo.findAll()).thenReturn(customerList);
		List<Customer> companies = service.getCustomersByType("company");
		assertEquals(1, companies.size());
		assertTrue(companies.get(0) instanceof Company);
	}
	
	@Test
	void test_thatACustomerCanHaveMultipleAccounts() {
		Address newAddress = new Address("3 Sandport Way", "Edinburgh", "EH6 6EA", "Midlothian");
		Customer newCustomer = new Person("Ellen Taylor", newAddress, "person");	
		SavingsAccount account1 = new SavingsAccount(1200, newCustomer, 5);
		SavingsAccount account2 = new SavingsAccount(30000, newCustomer, 1);
		when(mockRepo.save(newCustomer)).thenReturn(newCustomer);
		when(mockAccRepo.save(account1)).thenReturn(account1);
		when(mockAccRepo.save(account2)).thenReturn(account2);
		controller.addNewCustomer(newCustomer);
		when(mockRepo.findById(newCustomer.getCustomerId())).thenReturn(Optional.of(newCustomer));
		accService.addAccount(newCustomer.getCustomerId(), account1);
		accService.addAccount(newCustomer.getCustomerId(), account2);
		List<Account> customerAccounts = newCustomer.getAccounts();
		assertEquals(2, customerAccounts.size());
	}
	

}
