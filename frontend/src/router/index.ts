import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import BalanceView from "../views/BalanceView.vue";
import BudgetView from "../views/BudgetView.vue";
import SettingsView from "../views/SettingsView.vue";
import AnalyticsView from "../views/AnalyticsView.vue";

const routes = [
    { path: "/", component: HomeView },
    { path: "/balance", component: BalanceView },
    { path: "/budget", component: BudgetView },
    { path: "/analytics", component: AnalyticsView },
    { path: "/settings", component: SettingsView },

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;