package com.example.springmybatisdemo.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.example.springmybatisdemo.common.R;
import com.example.springmybatisdemo.entity.User;
import com.example.springmybatisdemo.service.UserService;
import com.example.springmybatisdemo.util.JWTUtils;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/user")
public class UesrController {

    @Autowired
    private UserService userService;

    //注册
    @RequestMapping("/register")
    public R<String> register(@RequestBody Map<String, String> map){
        // 1 获取各种参数
        String username = map.get("username").toString();
        String password = map.get("password").toString();
        String confirm = map.get("confirm").toString();

        System.out.println(username);
        System.out.println(password);
        System.out.println(confirm);

        // 2 判断验证密码是否相等
        if (!password.equals(confirm)){
            return R.error("两次输入的密码必须相同！");
        }

        // 3 查询数据库，是否已有同用户名
        LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.eq(User::getUsername, username);
        System.out.println("ok0！");
        User user = userService.getOne(queryWrapper);
        if (user != null){
            return R.error("当前已有此用户名！");
        }
        // 4 注册用户
        User newUser = new User();
        newUser.setUsername(username);
        newUser.setPassword(password);
        userService.save(newUser);

        return R.success("注册成功！");
    }

    @RequestMapping("/login")
    public R<Map<String,String>> login(@RequestBody Map<String, String> map){
        // 1 获取各种参数
        String username = map.get("username").toString();
        String password = map.get("password").toString();

        // 2 查询数据库
        LambdaQueryWrapper<User> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.eq(User::getUsername,username);
        queryWrapper.eq(User::getPassword,password);
        User user = userService.getOne(queryWrapper);
        
        if (user == null){
            return R.error("您输入的用户名或密码不正确！");
        }
        
        // 3 生成jwt
        //将userId存入token中
        String userid = user.getId().toString();
        String token = JWTUtils.createToken(userid);
        
        // 4 返回数据
        Map<String, String> data = new HashMap<>();
        data.put("type", "login");
        data.put("userid", userid);
        data.put("username", username);
        data.put("token", token);


        return R.success("登陆成功！", data);
    }

    //test
    @RequestMapping("/test")
    public R<Map<String,String>> test(@RequestHeader Map<String, String> header, @RequestBody Map<String, String> body){
        Map<String, String> data = new HashMap<>();

        System.out.println(header.get("token"));

        return R.success(data);
    }
}
