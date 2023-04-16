package com.example.springmybatisdemo.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.springmybatisdemo.entity.User;
import com.example.springmybatisdemo.mapper.UserMapper;
import com.example.springmybatisdemo.service.UserService;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl extends ServiceImpl<UserMapper,User> implements UserService {
}
