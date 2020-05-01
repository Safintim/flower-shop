export const actions = {
  nuxtServerInit ({ dispatch }, context) {
    return Promise.all([
      dispatch('cities/nuxtServerInit', context)
    ])
  }
}
