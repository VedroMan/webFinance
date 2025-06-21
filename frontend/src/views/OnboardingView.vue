<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const name = ref("");
const currency = ref("BYN");
const error = ref("");

// Псевдо user_id (в будущем получай от Telegram)
const userId = 1;

const createWallet = () => {
  if (!name.value.trim()) {
    error.value = "Введите название кошелька";
    return;
  }

  // ⚠️ Временная генерация ID (заменишь на ответ от бэка)
  const walletId = Math.floor(Math.random() * 100000);

  localStorage.setItem("wallet_id", walletId.toString());
  localStorage.setItem("user_id", userId.toString());
  localStorage.setItem("wallet_name", name.value);
  localStorage.setItem("wallet_currency", currency.value);

  // Перенаправление на основной экран
  router.push("/amount");
};
</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-screen px-4 bg-white dark:bg-gray-900 text-gray-800 dark:text-white">
    <h1 class="text-2xl font-bold mb-6 text-center">Создайте кошелёк 💼</h1>

    <input
      v-model="name"
      type="text"
      placeholder="Название кошелька"
      class="w-full max-w-xs px-4 py-2 mb-3 border border-gray-300 rounded-lg focus:outline-none"
    />

    <select
      v-model="currency"
      class="w-full max-w-xs px-4 py-2 mb-3 border border-gray-300 rounded-lg"
    >
      <option value="BYN">BYN</option>
      <option value="USD">USD</option>
      <option value="EUR">EUR</option>
    </select>

    <button
      @click="createWallet"
      class="bg-emerald-500 text-white px-6 py-2 rounded-lg hover:bg-emerald-600 transition w-full max-w-xs"
    >
      Создать
    </button>

    <p v-if="error" class="text-red-500 mt-4 text-sm">{{ error }}</p>
  </div>
</template>

<style scoped>
input,
select {
  background-color: white;
}
</style>
