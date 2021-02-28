import { createStore } from "vuex";
import { CategoryService } from '../api/api.service';

const state = {
    count: 0,
    mainCategory: {}
}

const mutations = {
    increment(state) {
        state.count++;
    },
    setMainCategory(state) {
        state.mainCategory = {};
        CategoryService.get().then(response => {
            state.mainCategory = response.data[0]
        });
    }
}

export default createStore({
    state,
    mutations
});