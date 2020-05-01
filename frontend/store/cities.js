export const state = () => ({
  cities: [],
  currentCity: null
})

export const mutations = {
  setCities (state, cities) {
    state.cities = cities
  },
  setCurrentCity (state, city) {
    state.currentCity = city
  }
}

const citiesUrl = 'http://127.0.0.1:8000/api/cities'

export const actions = {
  async nuxtServerInit ({ commit }) {
    const cities = await this.$axios.$get(citiesUrl)
    commit('setCities', cities)
    if (cities.length !== 0) {
      commit('setCurrentCity', cities[0])
    }
  },
  async fetch ({ commit }) {
    const cities = await this.$axios.$get(citiesUrl)
    commit('setCities', cities)
  }
}

export const getters = {
  cities: state => state.cities,
  currentCity: state => state.currentCity
}
