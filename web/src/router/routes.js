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
  { // 单词管理 没有groupid跳转到书管理
    path: '/wordsadmin/word',
    redirect: '/wordsadmin/book',
  },
  { // 单词管理
    path: '/wordsadmin/word/:groupid',
    name: 'wordsadmin_word',
    component: () => import('@/views/wordsadmin/word.vue'),
    meta: { title: '单词表-单词管理', requireAuth:true, },
  },
  { // 添加单词
    path: '/wordsadmin/word/:groupid/add',
    name: 'wordsadmin_word_add',
    component: () => import('@/views/wordsadmin/word_add.vue'),
    meta: { title: '单词表-单词添加', requireAuth:true, },
  },
  { // 音频管理
    path: '/wordsadmin/sound',
    name: 'wordsadmin_sound',
    component: () => import('@/views/wordsadmin/sound.vue'),
    meta: { title: '音频管理', requireAuth:true, },
  },
  {
    path: '/dictation/select',
    name: 'dictation_select',
    component: () => import('@/views/dictation_select.vue'),
    meta: { title: '单词默写选择', mode: 'phone', requireAuth:true, },
  },
  {
    path: '/dictation',
    name: 'dictation',
    component: () => import('@/views/dictation.vue'),
    meta: { title: '单词默写', mode: 'phone', requireAuth:true, },
  },
]
export default routes