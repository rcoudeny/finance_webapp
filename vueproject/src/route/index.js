import Home from '@/pages/Home';
import About from '@/pages/About';
import Transactions from '@/pages/transactionspage/Transactions';
import Login from '@/pages/authentification/Login';
import Register from '@/pages/authentification/Register';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/about",
        name: "About",
        component: About,
    },
    {
        path: "/transactions",
        name: "Transactions",
        component: Transactions,
    },
    {
        path: "/login",
        name: "Log in",
        component: Login,
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
    },
    { path: "/:catchAll(.*)", redirect: '/' }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;