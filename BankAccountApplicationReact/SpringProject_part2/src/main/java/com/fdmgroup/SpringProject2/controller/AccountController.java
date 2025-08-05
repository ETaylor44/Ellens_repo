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

import com.fdmgroup.SpringProject2.dto.AccountDTO;
import com.fdmgroup.SpringProject2.exception.AccountNotFoundException;
import com.fdmgroup.SpringProject2.model.Account;
import com.fdmgroup.SpringProject2.model.CheckingAccount;
import com.fdmgroup.SpringProject2.model.Customer;
import com.fdmgroup.SpringProject2.model.SavingsAccount;
import com.fdmgroup.SpringProject2.repository.CustomerRepository;
import com.fdmgroup.SpringProject2.service.AccountService;
import com.fdmgroup.SpringProject2.service.CustomerService;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;

@RestController @RequestMapping("/api/v1/accounts")
@CrossOrigin(origins="https://localhost:3000")
public class AccountController {
	
	AccountService accountService;
	
	@Autowired
	public AccountController(AccountService accountService) {
		this.accountService = accountService;
	}
	
	@Operation(summary = "Adds new account")
	@ApiResponses(value = {
			@ApiResponse(responseCode = "409"),
			@ApiResponse(responseCode = "404"),
			//@ApiResponse(responseCode = "201", content = @Content(mediaType = "application/json"))
	})
	@PostMapping("/new/{id}")
    public ResponseEntity<AccountDTO> addNewAccount(@PathVariable long id, @RequestBody AccountDTO dto) {
    	AccountDTO accountToAdd = accountService.addAccount(id, dto);
    	if (accountToAdd != null) {
    		URI location = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(accountToAdd.getAccountId())
    				.toUri();
    		return ResponseEntity.created(location).build();
    	}
    	
    	return ResponseEntity.status(HttpStatus.CONFLICT).build(); 
    }
	
	@Operation(summary = "Gets all stored accounts")
	@ApiResponses(value = {
			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
	})
	@GetMapping
	public ResponseEntity<List<AccountDTO>> getAccounts(){
    	List<AccountDTO> accounts = accountService.listAllAccounts();
    	return ResponseEntity.ok(accounts);
	}
	
//	@Operation(summary = "Updates all account details")
//	@ApiResponses(value = {
//			@ApiResponse(responseCode = "404"),
//			@ApiResponse(responseCode = "409"),
//			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
//	})
//	@PutMapping("update/{id}")
//    public ResponseEntity<AccountDTO> updateAccount(@PathVariable long id, @RequestBody Account updatedAccountDetails) {
//    	Account accountToUpdate = accountService.getAccountById(id);
//    	
//    	if (accountToUpdate == null) {
//    		throw new AccountNotFoundException("id: " + id);
//    	}
//    	
//    	if (accountToUpdate != null) {
//    		accountToUpdate.setBalance(updatedAccountDetails.getBalance());
//    		
//    		if (accountToUpdate.getType().equals("savings")) {
//    			SavingsAccount savingsAccountToUpdate = (SavingsAccount)accountToUpdate;
//    			SavingsAccount updatedSavingsAccountDetails = (SavingsAccount)updatedAccountDetails;
//    			savingsAccountToUpdate.setInterestRate(updatedSavingsAccountDetails.getInterestRate());
//    		}
//    		else if(accountToUpdate.getType().equals("checking")) {
//    			CheckingAccount checkingAccountToUpdate = (CheckingAccount)accountToUpdate;
//    			CheckingAccount updatedCheckingAccountDetails = (CheckingAccount)updatedAccountDetails;
//    			checkingAccountToUpdate.setNextCheckNumber(updatedCheckingAccountDetails.getNextCheckNumber());
//    		}
//    	}
//    	
//    	Account updatedAccount = accountService.updateAccount(accountToUpdate);
//    	
//    	if (updatedAccount != null) {
//    		return ResponseEntity.ok(updatedAccount);
//    	}
//    	else {
//    		return ResponseEntity.status(HttpStatus.CONFLICT).build();
//    	}
//    	
//    }
	
	@Operation(summary = "Deletes account with the id passed in")
	@ApiResponses(value = {
			@ApiResponse(responseCode = "404"),
			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
	})
	@DeleteMapping("delete/{id}")
    public ResponseEntity<Void> deleteAccount(@PathVariable long id) {
    	accountService.deleteAccount(id);
    	return ResponseEntity.status(HttpStatus.OK).build();
    	    	
    }
	
	@Operation(summary = "Finds account with the id passed in")
	@ApiResponses(value = {
			@ApiResponse(responseCode = "404"),
			//@ApiResponse(responseCode = "200", content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE))
	})
	@GetMapping("/{id}")
    public ResponseEntity<AccountDTO> getAccountById(@PathVariable long id) {
    	AccountDTO accountFound = accountService.getAccountById(id); 
    	if (accountFound != null) {
    		return ResponseEntity.status(HttpStatus.OK).body(accountFound);
    	}
    	throw new AccountNotFoundException("id: " + id);
    }
	
	@GetMapping("/search-by-city")
    public ResponseEntity<List<AccountDTO>> findAccountByCity(@RequestParam String city) {
    	List<AccountDTO> accounts = accountService.findAccountByCity(city);
    	
    	return ResponseEntity.ok(accounts);
    	
    }

}
