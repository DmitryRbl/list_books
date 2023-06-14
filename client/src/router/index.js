import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/HomeViews.vue";
import About from "@/views/AboutViews.vue";

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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;