<template>
    <nav class="fixed bottom-0 py-4 flex dark:bg-gray-950 bg-white justify-around w-full text-center">
        <RouterLink
        v-for="(item, index) in links" 
        :key="index" 
        :to="item.link"
        class="flex flex-col items-center justify-center text-xl transition"
        :class="{
        'text-emerald-500': route.path === item.link,
        'text-gray-400 dark:text-gray-500': route.path !== item.link
        }"
        >
            <faicon :icon=item.icon />
            <p class="text-[10px]">{{ item.title }}</p>
        </RouterLink>
    </nav>
</template>

<script setup lang="ts">
import { faPlusSquare, faMoneyBill, faCalendarWeek, faChartSimple, faGear } from '@fortawesome/free-solid-svg-icons';
import { useRoute } from 'vue-router';

const route = useRoute();

const links = [
    { title: "Добавить", icon: faPlusSquare, link: "/" },
    { title: "Баланс", icon: faMoneyBill, link: "/balance" },
    { title: "Бюджет", icon: faCalendarWeek, link: "/budget" },
    { title: "Аналитика", icon: faChartSimple, link: "/analytics" },
    { title: "Настройки", icon: faGear, link: "/settings" },
];
</script>