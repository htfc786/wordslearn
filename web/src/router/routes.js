const routes = [
  {
      path: '/',
      name: 'index',
      title: '首页',
      component: () => import('@/views/index.vue'),
  },
  {
      path: '/login',
      name: 'login',
      title: '登录',
      component: () => import('@/views/login.vue'),
  },
  {
      path: '/register',
      name: 'register',
      title: '注册',
      component: () => import('@/views/register.vue'),
  },
  {
      path: '/vocabulary',
      name: 'vocabulary',
      title: '单词表',
      component: () => import('@/views/vocabulary.vue'),
  },
]
export default routes