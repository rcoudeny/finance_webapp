import { CategoryService } from "../api/api.service";
import { SET_MAIN_CATEGORY } from "./actions.type";

const state = {
    name: "",
    transactions: {
        date: new Date(),
        amount: new Number(),
        opponentName: "",
        opponentAccount: "",
        comment: "",
        ownAccount: "",
    },
}

const getters = {
    mainCategory(state) {
        return state.mainCategory;
    }
}

export const actions = {
    async [SET_MAIN_CATEGORY](context) {
        const { data } = await CategoryService.get();
        console.log(data[0]);
        console.log("fetch");
        context.commit(SET_MAIN_CATEGORY, data[0]);
        return data;
    }
}

export const mutations = {
    [SET_MAIN_CATEGORY](state, mainCategory) {
        state.mainCategory = mainCategory
    }
}



export default {
    state,
    actions,
    getters,
    mutations
}