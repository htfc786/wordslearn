const routes = [
  {
      path: '/',
      name: 'index',
      title: '首页',
      component: () => import('@/views/index.vue'),
      meta: { mode: 'phone', requireAuth:true, },
  },
  {
      path: '/login',
      name: 'login',
      title: '登录',
      component: () => import('@/views/login.vue'),
      meta: { mode: 'phone', },
  },
  {
      path: '/register',
      name: 'register',
      title: '注册',
      component: () => import('@/views/register.vue'),
      meta: { mode: 'phone', },
  },
  {
      path: '/wordsadmin',
      name: 'vocabulary',
      title: '单词表-书籍管理',
      component: () => import('@/views/wordsadmin/book.vue'),
      meta: { requireAuth:true, },
  },
  {
    path: '/dictation/select',
    name: 'dictation_select',
    title: '单词默写选择',
    component: () => import('@/views/dictation_select.vue'),
    meta: { mode: 'phone', requireAuth:true, },
  },
]
export default routes