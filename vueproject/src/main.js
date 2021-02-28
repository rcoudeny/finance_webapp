import { createApp } from 'vue'
import App from './App.vue';
import router from './route';
import store from './store/store';

import ApiService from './api/api.service';

ApiService.init();

createApp(App).use(store).use(router).mount('#app')
