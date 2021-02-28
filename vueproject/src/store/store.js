import { createStore } from "vuex";

import auth from "./auth.module";
import category from './category.module';


export default createStore({
    modules: {
        auth,
        category
    }
});