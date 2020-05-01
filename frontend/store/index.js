export const actions = {
  async nuxtServerInit ({ dispatch }, context) {
    // return Promise.all([
    await dispatch('cities/fetch')
    // ])
  }
}
