<script setup lang="ts">
import { ref } from "vue";
import { faDeleteLeft, faCheck, faMessage } from "@fortawesome/free-solid-svg-icons";

const amount = ref("");
const isSpent = ref(true);
const isModalOpen = ref(false);
const comment = ref("");

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

// Сохранить комментарий и закрыть модалку
const saveComment = () => {
  isModalOpen.value = false;
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
  <div class="flex flex-col items-center justify-start px-2 pt-15">
    <!-- Селектор типа -->
    <div class="flex w-full max-w-xs mb-4 bg-white dark:bg-gray-800 p-1 rounded-full shadow">
      <button
        :class="[
          'flex-1 py-2 rounded-full text-sm font-semibold',
          isSpent ? 'bg-emerald-500 text-white' : 'text-gray-600 dark:text-gray-300'
        ]"
        @click="isSpent = true"
      >
        Расход
      </button>
      <button
        :class="[
          'flex-1 py-2 rounded-full text-sm font-semibold',
          !isSpent ? 'bg-emerald-500 text-white' : 'text-gray-600 dark:text-gray-300'
        ]"
        @click="isSpent = false"
      >
        Приход
      </button>
    </div>

    <!-- Сумма -->
    <h1 class="text-lg font-semibold text-gray-800 dark:text-white">Введите сумму</h1>
    <div class="mt-4 text-3xl font-bold bg-gray-50 dark:bg-gray-800 dark:text-white text-gray-900 px-4 py-3 rounded-lg shadow w-full max-w-xs text-center">
      {{ formattedAmount() }}
    </div>

    <!-- Клавиши -->
    <div class="grid grid-cols-3 gap-2 mt-4 w-full max-w-xs">
      <button
        v-for="n in [1,2,3,4,5,6,7,8,9,0]"
        :key="n"
        @click="pressNumber(n.toString())"
        class="h-12 text-lg font-semibold bg-gray-200 dark:bg-gray-700 dark:text-white text-gray-900 rounded-lg shadow-sm active:scale-95 transition"
      >
        {{ n }}
      </button>

      <!-- Удаление -->
      <button
        @click="deleteLast"
        class="col-span-1 bg-gray-500 text-white py-2 rounded-lg text-lg shadow-sm active:scale-95 transition"
      >
        <faicon :icon="faDeleteLeft" />
      </button>

      <!-- Комментарий (открыть модалку) -->
      <button
        @click="isModalOpen = true"
        class="col-span-1 bg-blue-500 text-white py-2 rounded-lg text-lg shadow-sm active:scale-95 transition"
      >
        <faicon :icon="faMessage" />
      </button>
    </div>

    <!-- Подтвердить -->
    <div class="flex gap-3 mt-6 w-full max-w-xs justify-between">
      <button class="flex-1 bg-emerald-500 text-white py-2 rounded-lg text-lg shadow-sm active:scale-95 transition">
        <faicon :icon="faCheck" />
      </button>
    </div>

    <!-- Модалка комментария -->
    <div
      v-if="isModalOpen"
      class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <div class="bg-white dark:bg-gray-800 rounded-lg p-5 w-11/12 max-w-sm shadow-lg text-gray-800 dark:text-white">
        <h2 class="text-lg font-bold mb-3">Комментарий</h2>
        <textarea
          v-model="comment"
          maxlength="255"
          rows="4"
          placeholder="Введите комментарий к переводу"
          class="w-full p-2 border border-gray-300 rounded resize-none focus:outline-none focus:ring"
        ></textarea>
        <p class="text-sm text-gray-500 mt-1 text-right">{{ comment.length }}/255</p>

        <div class="flex justify-end mt-4 gap-2">
          <button
            @click="isModalOpen = false"
            class="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded hover:bg-gray-300 dark:hover:bg-gray-600"
          >
            Отмена
          </button>
          <button
            @click="saveComment"
            class="px-4 py-2 bg-emerald-500 text-white rounded hover:bg-emerald-600"
          >
            Сохранить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
button {
  transition: all 0.2s ease-in-out;
}
</style>
