export const actions = {
  async nuxtServerInit ({ dispatch }) {
    await dispatch('categories/fetch')
    await dispatch('cities/fetch')
  }
}
