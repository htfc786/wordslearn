package com.example.springmybatisdemo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@SpringBootApplication
@ServletComponentScan
public class SpringmybatisdemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringmybatisdemoApplication.class, args);
	}

}
