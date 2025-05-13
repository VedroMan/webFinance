<script setup lang="ts">
import { RouterView } from 'vue-router';
import Header from './components/Header.vue';
import TabBar from './components/TabBar.vue';
</script>

<template>
  <div id="app">
    <Header />
    <main class="p-4">
      <RouterView />
    </main>
    <TabBar />
  </div>
</template>

<style scoped>
/* */
</style>
