package com.useraccount.service;

import com.useraccount.model.User;

public interface UserService {
    void save(User user);

    User findByUsername(String username);
}
