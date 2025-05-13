<template>
    <nav class="fixed bottom-0 py-3 flex dark:bg-gray-900 bg-emerald-50 justify-around w-full text-emerald-500 text-center">
        <RouterLink
        v-for="(item, index) in links" 
        :key="index" 
        :to="item.link"
        class="flex flex-col items-center justify-center text-xl">
            <faicon :icon=item.icon />
            <p class="text-[10px]">{{ item.title }}</p>
        </RouterLink>
    </nav>
</template>

<script setup lang="ts">
import { faPlusSquare, faMoneyBill, faCalendarWeek, faChartSimple, faGear } from '@fortawesome/free-solid-svg-icons';

const links = [
    { title: "Добавить", icon: faPlusSquare, link: "/" },
    { title: "Баланс", icon: faMoneyBill, link: "/balance" },
    { title: "Бюджет", icon: faCalendarWeek, link: "/budget" },
    { title: "Аналитика", icon: faChartSimple, link: "/analytics" },
    { title: "Настройки", icon: faGear, link: "/settings" },
];
</script>