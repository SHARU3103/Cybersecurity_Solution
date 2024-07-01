package com.useraccount.validator;

import com.useraccount.model.User;
import com.useraccount.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.apache.commons.lang.StringUtils;
import org.springframework.validation.Validator;

@Component
public class UserValidator implements Validator {
    @Autowired
    private UserService userService;
    
    private static final String PASSWORD_PATTERN =
            "((?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,})";

    @Override
    public boolean supports(Class<?> aClass) {
        return User.class.equals(aClass);
    }
    
    @Override
    public void validate(Object o, Errors errors) {
        User user = (User) o;

        ValidationUtils.rejectIfEmptyOrWhitespace(errors, "username", "NotEmpty");
        if (user.getUsername().length() < 5) {
            errors.rejectValue("username", "Size.userForm.username");
        }
        if(!(StringUtils.isAlphanumeric(user.getUsername()))) {
        	errors.rejectValue("username", "Alphanumeric.userForm.username");
        }
        if (userService.findByUsername(user.getUsername()) != null) {
            errors.rejectValue("username", "Duplicate.userForm.username");
        }

        ValidationUtils.rejectIfEmptyOrWhitespace(errors, "password", "NotEmpty");

        if((!(user.getPassword().toString().matches(PASSWORD_PATTERN))) || (!(StringUtils.isAlphanumeric(user.getPassword())))) {
        	errors.rejectValue("password", "Pattern.userForm.password");
        }
        
        if(!(user.getPasswordConfirm().toString().matches(PASSWORD_PATTERN)) || (!(StringUtils.isAlphanumeric(user.getPasswordConfirm())))) {
        	errors.rejectValue("passwordConfirm", "Pattern.userForm.password");
        }
        
        if (!user.getPasswordConfirm().equals(user.getPassword())) {
            errors.rejectValue("passwordConfirm", "Diff.userForm.passwordConfirm");
        }
    }
}
