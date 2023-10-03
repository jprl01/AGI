import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/helloWorld/AboutView.vue'
import UserAuctionView from '@/views/Auction/UserAuctionView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/helloWorld/HelloView.vue'),
      children: [
        {
          path: 'list',
          name: 'hello-list',
          component: AboutView,
          meta: {
            title: 'Hello World',
          },
        },
      ]
    },
    {
      path: '/register',
      name: 'register',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/User/RegisterView.vue'),
      
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/User/LoginView.vue'),
      
    },
    {
      path: '/profile',
      name: 'profile',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/User/ProfileView.vue'),
      
    },
    {
      path: '/auction',
      name: 'auction',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Auction/AuctionView.vue'),
      children: [
        {
          path: 'user',
          name: 'my-auction',
          component: UserAuctionView,
          meta: {
            title: 'My Auction',
          },
        },
      ]
      
    },
  ]
})

export default router
