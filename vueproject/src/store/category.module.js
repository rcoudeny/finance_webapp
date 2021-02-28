import { CategoryService } from "@api/api.service";
import { FETCH_MAIN_CATEGORY } from "@store/actions.type";

const initialState = {
    transaction: {
        date: new Date(),
        amount: new Number(),
        opponentName: "",
        opponentAccount: "",
        comment: "",
        ownAccount: "",
    },
}

export const state = { ...initialState };

export const actions = {
    async [FETCH_MAIN_CATEGORY](context) {
        const { data } = await CategoryService.get();
        context.commit(SET_MAIN_CATEGORY, data);
        return data;
    }
}

export const mutations = {
    [SET_MAIN_CATEGORY](state, mainCategory) {
        state.mainCategory = mainCategory
    }
}

const getters = {
    mainCategory(state) {
        return state.mainCategory;
    }
}

export default {
    state,
    actions,
    getters
}