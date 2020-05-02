export const state = () => ({
  bouquets: [],
  mainBouquets: []
})

export const mutations = {
  setBouquets (state, bouquets) {
    state.bouquets = bouquets
  },
  setMainBouquets (state, bouquets) {
    state.mainBouquets = bouquets
  }
}

const bouquetsUrl = 'http://127.0.0.1:8000/api/bouquets/'
const bouquetsFilterPriceUrl = 'http://127.0.0.1:8000/api/bouquets/?price='
const bouquetsFilterColorUrl = 'http://127.0.0.1:8000/api/bouquets/?color='
const mainBouquetsUrl = 'http://127.0.0.1:8000/api/bouquets/?is_show_on_main_page=true'

export const actions = {
  async fetch ({ commit }) {
    const bouquets = await this.$axios.$get(bouquetsUrl)
    commit('setBouquets', bouquets)
  },
  async fetchMainBouquets ({ commit }) {
    const bouquets = await this.$axios.$get(mainBouquetsUrl)
    commit('setMainBouquets', bouquets)
  },
  async filterByPrice ({ commit }, params) {
    const bouquets = await this.$axios.$get(bouquetsFilterPriceUrl + params)
    commit('setBouquets', bouquets)
  },
  async filterByColor ({ commit }, params) {
    const bouquets = await this.$axios.$get(bouquetsFilterColorUrl + params)
    console.log(bouquets)
    commit('setBouquets', bouquets)
  }
}

export const getters = {
  bouquets: state => state.bouquets,
  mainBouquets: state => state.mainBouquets
}
