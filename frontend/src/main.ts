import { createApp } from 'vue'
import './assets/style.css'

import App from './App.vue'
import router from './router';

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const app = createApp(App);

app.component('faicon', FontAwesomeIcon);

app.use(router);

// Монтировка приложения
app.mount('#app');