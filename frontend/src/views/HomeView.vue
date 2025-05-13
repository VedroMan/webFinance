<script setup lang="ts">
import { ref } from "vue";
import { faDeleteLeft, faCancel } from "@fortawesome/free-solid-svg-icons";

const amount = ref("");

// Ввод цифр
const pressNumber = (num: string) => {
  if (amount.value.length < 9) {
    amount.value += num;
  }
};

// Удаление последней цифры
const deleteLast = () => {
  amount.value = amount.value.slice(0, -1);
};

// Сброс
const resetAmount = () => {
  amount.value = "";
};

// Формат суммы в BYN
const formattedAmount = () => {
  if (!amount.value) return "0,00 BYN";
  const raw = parseFloat(amount.value) / 100;
  return raw.toLocaleString("ru-BY", {
    style: "currency",
    currency: "BYN",
    minimumFractionDigits: 2,
  });
};
</script>

<template>
  <div class="flex flex-col items-center justify-center px-4">
    <!-- Заголовок -->
    <h1 class="text-xl font-bold">Введите сумму</h1>

    <!-- Поле отображения суммы -->
    <div class="mt-15 text-3xl sm:text-4xl font-bold bg-white dark:bg-gray-800 dark:text-white text-gray-900 px-4 py-3 rounded-lg shadow w-full max-w-xs text-center">
      {{ formattedAmount() }}
    </div>

    <!-- Цифровая клавиатура -->
    <div class="grid grid-cols-3 gap-3 mt-6 w-full max-w-xs">
      <button
        v-for="n in [1,2,3,4,5,6,7,8,9,0]"
        :key="n"
        @click="pressNumber(n.toString())"
        class="h-14 text-xl font-bold bg-gray-200 dark:bg-gray-700 dark:text-white text-gray-900 rounded-lg shadow hover:scale-105 active:scale-95 transition"
      >
        {{ n }}
      </button>
    </div>

    <!-- Управляющие кнопки -->
    <div class="flex gap-4 mt-10 w-full max-w-xs justify-between">
      <button @click="resetAmount" class="flex-1 bg-red-500 text-white py-3 rounded-lg text-xl hover:bg-red-600 transition">
        <faicon :icon="faCancel" />
      </button>
      <button @click="deleteLast" class="flex-1 bg-gray-500 text-white py-3 rounded-lg text-xl hover:bg-gray-600 transition">
        <faicon :icon="faDeleteLeft" />
      </button>
    </div>
  </div>
</template>

<style scoped>
button {
  transition: all 0.2s ease-in-out;
}
</style>
