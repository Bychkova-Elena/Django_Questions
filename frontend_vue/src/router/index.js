import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import MyAccount from '../views/MyAccount.vue'
import Category from '../views/Category.vue'
import Subcategory from '../views/Subcategory.vue'
import Questions from '../views/Questions.vue'
import AdminAccount from '../views/AdminAccount.vue'
import News from '../views/News.vue'
import ManagerNews from '../views/ManagerNews.vue'
import AddNews from '../views/AddNews.vue'
import Main from '../views/Main.vue'
import EditNews from '../views/EditNews.vue'
import ManagerAccount from '../views/ManagerAccount.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
   {
        path: 'log-in',
        name: 'LogIn',
        component: LogIn
      },
         {
        path: 'main',
        name: 'Main',
        component: Main
      },
      {
        path: 'sign-up',
        name: 'SignUp',
        component: SignUp
      },
      {
        path: 'news',
        name: 'News',
        component: News
      },
      {
        path: 'category',
        name: 'Category',
        component: Category,

      },
      {
        path: 'category/:id',
        name: "Subcategory",
        component: Subcategory,
      },
      {
        path: 'category/:id/subcategory/:id',
        name: "Questions",
        component: Questions,
      },

      {
        path: 'my-account',
        name: 'MyAccount',
        component: MyAccount,
        meta: {
          requireLogin: true,
        }
      }
]
  },
   {
    path: '/admin-account',
    name: 'AdminAccount',
    component: AdminAccount,
    meta: {
      requireLogin: true,
    },
    children: [
    ]
  },
   
     {
    path: '/manager-account',
    name: 'ManagerAccount',
    component: ManagerAccount,
    meta: {
      requireLogin: true,
    },
    children: [
   {
        path: 'manager-news',
        name: 'ManagerNews',
        component: ManagerNews
      },
       {
        path: '/add-news',
        name: 'AddNews',
        component: AddNews
      },
             {
        path: 'edit-news/:id',
        name: 'EditNews',
        component: EditNews
      },
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router


