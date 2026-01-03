import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8001/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Dashboard API
export const getDashboard = () => api.get('/dashboard')

// Messages API
export const getMessages = (params = {}) => api.get('/messages', { params })
export const getMessage = (id) => api.get(`/messages/${id}`)
export const ingestMessage = (data) => api.post('/messages/ingest', data)

// Gmail API
export const getGmailMessages = (params = {}) => api.get('/gmail/messages', { params })
export const getGmailAuthStatus = () => api.get('/gmail/auth/status')

// Settings API
export const getSettings = () => api.get('/settings')
export const updateFocusMode = (mode) =>
  api.post('/settings/focus-mode', { focus_mode: mode })

// Logs API
export const getAgentDecisions = (params = {}) =>
  api.get('/logs/decisions', { params })

export default api
