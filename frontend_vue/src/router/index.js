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
import AdminNews from '../views/AdminNews.vue'
import AddNews from '../views/AddNews.vue'
import EditNews from '../views/EditNews.vue'
import ManagerAccount from '../views/ManagerAccount.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,

  },
   {
        path: '/log-in',
        name: 'LogIn',
        component: LogIn
      },
      {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
      },
      {
        path: '/news',
        name: 'News',
        component: News
      },
      {
        path: '/category',
        name: 'Category',
        component: Category,

      },
      {
        path: '/category/:id',
        name: "Subcategory",
        component: Subcategory,
      },
      {
        path: '/category/:id/subcategory/:id',
        name: "Questions",
        component: Questions,
      },

      {
        path: '/my-account',
        name: 'MyAccount',
        component: MyAccount,
        meta: {
          requireLogin: true,
        }
      },
   {
    path: '/admin-account',
    name: 'AdminAccount',
    component: AdminAccount,
    meta: {
      requireLogin: true,
    },
     children: [
        {
        path: 'admin-news',
        name: 'AdminNews',
        component: AdminNews
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
    path: '/manager-account',
    name: 'ManagerAccount',
    component: ManagerAccount,
    meta: {
      requireLogin: true,
    },
    children: [
 
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router


