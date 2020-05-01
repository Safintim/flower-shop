export const state = () => ({
  categories: []
})

export const mutations = {
  setCategories (state, categories) {
    state.categories = categories
  }
}

const categoriesUrl = 'http://127.0.0.1:8000/api/categories/'

export const actions = {
  async fetch ({ commit }) {
    const categories = await this.$axios.$get(categoriesUrl)
    commit('setCategories', categories)
  }
}

export const getters = {
  categories: s => s.categories
}
