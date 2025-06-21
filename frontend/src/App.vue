<script setup lang="ts">
import { RouterView } from 'vue-router';
import TabBar from './components/TabBar.vue';
</script>

<template>
  <div id="app">
    <main class="p-4">
      <RouterView />
    </main>
    <TabBar />
  </div>
</template>

<style scoped>
/* */
</style>
