package com.fdmgroup.SpringProject2.controller;

import java.net.URI;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;

import com.fdmgroup.SpringProject2.dto.CustomerDTO;
import com.fdmgroup.SpringProject2.exception.CustomerNotFoundException;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.service.CustomerService;

@RestController @RequestMapping("/api/v1/customers")
@CrossOrigin(origins="https://localhost:3000")
public class CustomerController {
	
	private CustomerService customerService;

	@Autowired
	public CustomerController(CustomerService customerService) {
		this.customerService = customerService;
	}
	
	@Operation(summary = "Adds new customer")
	@ApiResponses(value = {
			@ApiResponse(responseCode = "409"),
			@ApiResponse(responseCode = "404"),
			//@ApiResponse(responseCode = "201", content = @Content(mediaType = "application/json"))
	})
	@PostMapping("/new")
    public ResponseEntity<CustomerDTO> addNewCustomer(@RequestBody CustomerDTO dto) {
    	CustomerDTO customerToAdd = customerService.addCustomer(dto);
    	if (customerToAdd != null) {
    		URI location = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(customerToAdd.getCustomerId())
    				.toUri();
    		return ResponseEntity.created(location).build();
    	}
    	return ResponseEntity.status(HttpStatus.CONFLICT).build(); 
    }
	
	@Operation(summary = "Finds customer with the id passed in")
	@ApiResponses(value = {
			@ApiResponse(responseCode = "404"),
			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
	})
	@GetMapping("/{id}")
    public ResponseEntity<CustomerDTO> getCustomerById(@PathVariable long id) {
    	CustomerDTO customerFound = customerService.getCustomerById(id); 
    	if (customerFound != null) {
    		return ResponseEntity.status(HttpStatus.OK).body(customerFound);
    	}
    	throw new CustomerNotFoundException("id: " + id);
    }
	
	
	@Operation(summary = "Gets all stored companies or customers")
	@ApiResponses(value = {
			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
	})
	@GetMapping("/search-by-type")
	public ResponseEntity<List<CustomerDTO>> getCustomersByType(@RequestParam String type){
    	List<CustomerDTO> customerDTOsOfType = customerService.getCustomersByType(type);
    	return ResponseEntity.ok(customerDTOsOfType);
	}
	
//	@Operation(summary = "Updates all customer details except streetNumber")
//	@ApiResponses(value = {
//			@ApiResponse(responseCode = "404"),
//			@ApiResponse(responseCode = "409"),
//			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
//	})
//	@PutMapping("/update/{id}")
//    public ResponseEntity<Customer> updateCustomer(@PathVariable long id, @RequestBody Customer updatedCustomerDetails) {
//    	Customer customerToUpdate = customerService.getCustomerById(id);
//    	
//    	if (customerToUpdate == null) {
//    		throw new CustomerNotFoundException("id: " + id);
//    	}
//    	
//    	if (customerToUpdate != null) {
//    		customerToUpdate.setName(updatedCustomerDetails.getName());
//    		customerToUpdate.setAddress(updatedCustomerDetails.getAddress());
//    		customerToUpdate.setType(updatedCustomerDetails.getType());
//    	}
//    	
//    	Customer updatedCustomer = customerService.updateCustomer(customerToUpdate);
//    	
//    	if (updatedCustomer != null) {
//    		return ResponseEntity.ok(updatedCustomer);
//    	}
//    	else {
//    		return ResponseEntity.status(HttpStatus.CONFLICT).build();
//    	}
//    	
//    }
	
	@Operation(summary = "Deletes customer with the id passed in")
	@ApiResponses(value = {
			@ApiResponse(responseCode = "404"),
			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
	})
	@DeleteMapping("/delete/{id}")
    public ResponseEntity<Void> deleteCustomer(@PathVariable long id) {
    	if (customerService.deleteCustomer(id) == true) {
    		return ResponseEntity.status(HttpStatus.OK).build();
    	}
    	
    	throw new CustomerNotFoundException("id: " + id);
    	
    }
	
	
	
	@Operation(summary = "Gets all stored customers")
	@ApiResponses(value = {
			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
	})
	@GetMapping
	public ResponseEntity<List<CustomerDTO>> getCustomers(){
    	List<CustomerDTO> customerDTOs = customerService.listAllCustomers();
    	return ResponseEntity.ok(customerDTOs);
	}
	
	

}
