const routes = [
  { //首页
    path: '/',
    name: 'index',
    component: () => import('@/views/index.vue'),
    meta: { title: '首页', mode: 'phone', requireAuth:true, },
  },
  { // 登录
    path: '/login',
    name: 'login',
    component: () => import('@/views/login.vue'),
    meta: { title: '登录', mode: 'phone', },
  },
  { // 注册
    path: '/register',
    name: 'register',
    component: () => import('@/views/register.vue'),
    meta: { title: '注册', mode: 'phone', },
  },
  { // 单词管理 默认跳转到书管理
    path: '/wordsadmin',
    name: 'wordsadmin',
    redirect: '/wordsadmin/book',
  },
  { // 书管理
    path: '/wordsadmin/book',
    name: 'wordsadmin_book',
    component: () => import('@/views/wordsadmin/book.vue'),
    meta: { title: '单词表-书管理', requireAuth:true, },
  },
  { // 组管理 没有bookid跳转到书管理
    path: '/wordsadmin/group',
    redirect: '/wordsadmin/book',
  },
  { // 组管理
    path: '/wordsadmin/group/:bookid',
    name: 'wordsadmin_group',
    component: () => import('@/views/wordsadmin/group.vue'),
    meta: { title: '单词表-组管理', requireAuth:true, },
  },
  {
    path: '/dictation/select',
    name: 'dictation_select',
    component: () => import('@/views/dictation_select.vue'),
    meta: { title: '单词默写选择', mode: 'phone', requireAuth:true, },
  },
]
export default routes