import { createRouter, createWebHistory } from 'vue-router'
import GameView from '@/views/GameView.vue'
import FinanceView from '@/views/FinanceView.vue'
import ConfigView from '@/views/ConfigView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/index.html',
      name: 'home',
      component: FinanceView,
    },
    {
      path: '/',
      name: 'home',
      component: GameView,
    },
    {
      path: '/config',
      name: 'config',
      component: ConfigView,
    },
    {
      path: '/game',
      name: 'Game',
      component: GameView,
    },
    {
      path: '/:pathMatch(.*)*', // 匹配所有未知路径
      component: GameView // 默认加载的 404 页面
    }
  ],
})

export default router
