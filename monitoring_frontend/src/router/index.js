import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import DroneList from '@/views/DroneList.vue';
import TaskDetails from '@/views/TaskDetails.vue';
import TaskForm from '@/views/TaskForm.vue';
import Login from '@/views/Login.vue';       
import Register from '@/views/Register.vue';  
import Dashboard from '@/views/Dashboard.vue'; 
import TaskList from '../views/TaskList.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/drones',
        name: 'DroneList',
        component: DroneList
    },
    {
        path: '/tasks/new',
        name: 'CreateTask',
        component: TaskForm
    },
    {
        path: '/tasks',
        name: 'TaskList',
        component: TaskList
      },
      {
        path: '/tasks/new',
        name: 'TaskForm',
        component: TaskForm
      },
      {
        path: '/tasks/:id',
        name: 'TaskDetails',
        component: TaskDetails
      },
    {
        path: '/login',
        name: 'LoginPage',
        component: Login  
    },
    {
        path: '/register',
        name: 'RegisterPage',
        component: Register 
    },
    {
        path: '/dashboard',
        name: 'DashboardPage',
        component: Dashboard
      },
];

const router = createRouter({
    history: createWebHistory('/'),
    routes
});

export default router;
