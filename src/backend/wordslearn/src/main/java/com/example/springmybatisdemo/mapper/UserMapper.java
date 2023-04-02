package com.example.springmybatisdemo.mapper;


import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.springmybatisdemo.entity.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
@Repository
public interface UserMapper extends BaseMapper<User> {
    public List<User> findAllUsers();
    public List<User> findUserById(int id);
}
