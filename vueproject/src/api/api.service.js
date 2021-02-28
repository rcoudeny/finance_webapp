import axios from "axios";
import JwtService from "./jwt.service";
import { API_URL } from "@/api/config";

const ApiService = {
    init() {
        axios.defaults.baseURL = API_URL;
    },

    setHeader() {
        axios.defaults.headers.common[
            "Authorization"
        ] = `Token ${JwtService.getToken()}`;
    },

    isLoggedIn() {
        if (JwtService.getToken()) {
            return true;
        }
        return true;
    },

    query(resource, params) {
        return axios.get(resource, params).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    },

    get(resource, id = "") {
        return axios.get(`${resource}/${id}`).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    },

    post(resource, params) {
        return axios.post(`${resource}`, params);
    },

    update(resource, id, params) {
        return axios.put(`${resource}/${id}`, params);
    },

    put(resource, params) {
        return axios.put(`${resource}`, params);
    },

    delete(resource) {
        return axios.delete(resource).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    }
};

export default ApiService;

export const CategoryService = {
    get() {
        return ApiService.get("Category");
    }
}

export const ArticlesService = {
    query(type, params) {
        return ApiService.query("articles" + (type === "feed" ? "/feed" : ""), {
            params: params
        });
    },
    get(slug) {
        return ApiService.get("articles", slug);
    },
    create(params) {
        return ApiService.post("articles", { article: params });
    },
    update(slug, params) {
        return ApiService.update("articles", slug, { article: params });
    },
    destroy(slug) {
        return ApiService.delete(`articles/${slug}`);
    }
};

export const CommentsService = {
    get(slug) {
        if (typeof slug !== "string") {
            throw new Error(
                "[RWV] CommentsService.get() article slug required to fetch comments"
            );
        }
        return ApiService.get("articles", `${slug}/comments`);
    },

    post(slug, payload) {
        return ApiService.post(`articles/${slug}/comments`, {
            comment: { body: payload }
        });
    },

    destroy(slug, commentId) {
        return ApiService.delete(`articles/${slug}/comments/${commentId}`);
    }
};

export const FavoriteService = {
    add(slug) {
        return ApiService.post(`articles/${slug}/favorite`);
    },
    remove(slug) {
        return ApiService.delete(`articles/${slug}/favorite`);
    }
};