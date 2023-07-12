//https://blog.csdn.net/xjtarzan/article/details/119736309
// 导入router所需的方法
import { createRouter, createWebHistory } from 'vue-router'

// 导入路由页面的配置
import routes from './routes'

// 路由参数配置
const router = createRouter({
    // 使用hash(createWebHashHistory)模式，(createWebHistory是HTML5历史模式，支持SEO)
    history: createWebHistory(),
    routes: routes,
})

// 全局前置守卫，这里可以加入用户登录判断
// https://blog.csdn.net/zhuzhucaicai/article/details/111932980
router.beforeEach((to, from, next) => {
    // 继续前进 next()
    // 返回 false 以取消导航
    if (to.meta.requireAuth) {  // 判断该路由是否需要登录权限
        if (localStorage.getItem("access_token") != null) {  // 获取用户登录信息
            next();
        } else {
            next({
                path: '/login',
                query: {redirect: from.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
            })
        }
    } else {
        next();
    }
})

// 全局后置钩子，这里可以加入改变页面标题等操作
router.afterEach((to, from) => {
    const _title = to.meta.title
    if (_title) {
        window.document.title = _title
    }
})

// 导出默认值
export default router