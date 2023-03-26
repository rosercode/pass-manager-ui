import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/email',
    name: 'Email',
    meta: { title: '邮件管理' },
    component: () => import('@/components/Email.vue')
  },
  {
    path: '/phone',
    name: 'Phone',
    meta: { title: '手机号管理' },
    component: () => import('@/components/Phone.vue')
  },
  {
    path: '*',
    component: () => import('@/components/HelloWorld.vue')
  }
]

const createRouter = () => new VueRouter({
  mode: 'hash',
  scrollBehavior: () => ({ y: 0 }),
  base: process.env.BASE_URL,
  routes
})

const router = createRouter()

// 重置路由
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher
}

export default router
