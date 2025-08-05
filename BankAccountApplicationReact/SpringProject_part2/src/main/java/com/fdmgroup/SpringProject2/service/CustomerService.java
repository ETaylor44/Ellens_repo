package com.fdmgroup.SpringProject2.service;

import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.List;

import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.fdmgroup.SpringProject2.converter.CustomerConverter;
import com.fdmgroup.SpringProject2.dto.CustomerDTO;
import com.fdmgroup.SpringProject2.exception.CustomerNotFoundException;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.repository.CustomerRepository;

@Service
public class CustomerService {
	public CustomerRepository customerRepo;
	private final CustomerConverter customerConverter;

	@Autowired
	public CustomerService(CustomerRepository customerRepo, CustomerConverter customerConverter) {
		this.customerRepo = customerRepo;
		this.customerConverter = customerConverter;
	}

	public List<CustomerDTO> listAllCustomers() {
		return customerRepo.findAll()
				.stream()
				.map(customerConverter::toDTO)
				.collect(Collectors.toList());
	}

	public CustomerDTO addCustomer(CustomerDTO dto) {
		Customer customer = customerConverter.toEntity(dto);
		customer = customerRepo.save(customer);
		return customerConverter.toDTO(customer);
	}

	public CustomerDTO getCustomerById(long id) {
		Customer customerFound = customerRepo.findById(id)
				.orElseThrow(() -> new CustomerNotFoundException("id " + id));
		return customerConverter.toDTO(customerFound);
	}

//	public Customer updateCustomer(Customer customerToUpdate) {
//        if (customerRepo.existsById(customerToUpdate.getCustomerId())){
//        	customerRepo.save(customerToUpdate);
//        	return customerToUpdate;
//        }
//        
//        return null;
//	}

	public boolean deleteCustomer(long id) {
		if (customerRepo.existsById(id)) {
			customerRepo.deleteById(id);
			return true;
		}
		return false;
	}
	
	public List<CustomerDTO> getCustomersByType(String type){
    	List<Customer> allCustomers = customerRepo.findAll();
    	List<CustomerDTO> customerDTOsOfType = new ArrayList<CustomerDTO>();
    	for (Customer customer : allCustomers) {
    		if (customer.getType().equals(type)) {
    			CustomerDTO dto = customerConverter.toDTO(customer);
    			customerDTOsOfType.add(dto);
    		}
    	}
    	return customerDTOsOfType;
	}

}
