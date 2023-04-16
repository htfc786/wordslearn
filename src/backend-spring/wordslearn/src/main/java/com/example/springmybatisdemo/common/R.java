package com.example.springmybatisdemo.common;

import lombok.Data;

/**
 * 通用返回结果，服务端响应的数据最终都会封装成此对象
 * @param <T>
 * 返回格式：
 *  { 
 *      type: 状态 ok / error
 *      status: 状态码 200-成功 400-参数错误 401-需要登录 500-服务器内部错误,
 *      msg: 返回信息,
 *      //token: 如用户操作登录或登录状态即将到期，才有值，前端发现有值就替换原来的,
 *      data: 数据 {}
 *  }
 */


@Data
public class R<T> {

    private String type; //错误信息

    private Integer status; //编码：1成功，0和其它数字为失败

    private String msg; //信息
    
    //private String token; //token

    private T data; //数据

    // 统一返回
    public static <T> R<T> get(Integer code, String msg, T data) {
        // 1.type判断
        String type = "error"; 
        if (code == 200){
            type = "ok";
        }
        // 2.新建对象，传入参数
        R<T> r = new R<T>();
        r.type = type;
        r.status = code;
        r.msg = msg;
        r.data = data;
        return r;
    }

    // 执行成功
    public static <T> R<T> success(String msg, T data) {
        R<T> r = new R<T>();
        r.type = "ok";
        r.status = 200;
        r.msg = msg;
        r.data = data;
        return r;
    }

    // 执行成功 只有数据
    public static <T> R<T> success( T data) {
        R<T> r = new R<T>();
        r.type = "ok";
        r.status = 200;
        r.msg = "执行成功！";
        r.data = data;
        return r;
    }

    // 执行成功 只有信息
    public static <T> R<T> success(String msg) {
        R<T> r = new R<T>();
        r.type = "ok";
        r.status = 200;
        r.msg = msg;
        return r;
    }

    // 错误
    public static <T> R<T> error(String msg) {
        R<T> r = new R<T>();
        r.type = "error";
        r.status = 400;
        r.msg = msg;
        return r;
    }

    // 未登录返回
    public static <T> R<T> no_login() {
        R<T> r = new R<T>();
        r.type = "error";
        r.status = 401;
        r.msg = "请先登录";
        return r;
    }

    // 服务器内部错误
    public static <T> R<T> server_error() {
        R<T> r = new R<T>();
        r.type = "error";
        r.status = 500;
        r.msg = "服务器内部错误";
        return r;
    }

}