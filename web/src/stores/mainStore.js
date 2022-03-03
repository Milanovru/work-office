import { defineStore } from 'pinia'
import axios from 'axios'


export const useMainStore = defineStore({
  id: 'mainStore',
  state: () => (
    {
      html: null,
    }
  ),
  getters: {
    renderHtml: (state) => state.html,
   
  },
  actions: {
    render_templates(id) {
      axios.get(
        `http://localhost:8000/api/v1/files/${id}`
      ).then(response => this.html = response.data).catch(error => console.error(error))
    },
  },
})
