import { createApp } from 'vue'
import App from './App.vue';
import router from './route/router';
import store from './store/store';

import ApiService from './api/api.service';
import { CHECK_AUTH } from './store/actions.type';

ApiService.init();

store.dispatch(CHECK_AUTH);

createApp(App).use(store).use(router).mount('#app')
