const routes = [
  {
      path: '/',
      name: 'index',
      title: '首页',
      component: () => import('@/views/index.vue'),
      meta: { requireAuth:true, },
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
      meta: { requireAuth:true, },
  },
  {
    path: '/dictation/select',
    name: 'dictation_select',
    title: '单词默写选择',
    component: () => import('@/views/dictation_select.vue'),
    meta: { requireAuth:true, },
  },
]
export default routes