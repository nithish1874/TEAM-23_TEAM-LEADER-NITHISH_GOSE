import { useState, useEffect } from 'react'
import { getMessages } from '../services/api'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'
import './Analytics.css'

function Analytics() {
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(true)
  const [timeRange, setTimeRange] = useState('24h')

  useEffect(() => {
    loadMessages()
  }, [timeRange])

  const loadMessages = async () => {
    try {
      setLoading(true)
      const response = await getMessages({ limit: 1000 })
      setMessages(response.data)
    } catch (err) {
      console.error('Error loading messages:', err)
    } finally {
      setLoading(false)
    }
  }

  const getDecisionStats = () => {
    const stats = {
      SHOW: 0,
      HIDE: 0,
      POSTPONE: 0,
      SUMMARIZE: 0,
    }
    messages.forEach((msg) => {
      if (msg.final_decision && stats.hasOwnProperty(msg.final_decision)) {
        stats[msg.final_decision]++
      }
    })
    return Object.entries(stats).map(([name, value]) => ({ name, value }))
  }

  const getPriorityDistribution = () => {
    const buckets = {
      '1-3': 0,
      '4-6': 0,
      '7-8': 0,
      '9-10': 0,
    }
    messages.forEach((msg) => {
      if (msg.priority_score) {
        const score = msg.priority_score
        if (score <= 3) buckets['1-3']++
        else if (score <= 6) buckets['4-6']++
        else if (score <= 8) buckets['7-8']++
        else buckets['9-10']++
      }
    })
    return Object.entries(buckets).map(([name, value]) => ({ name, value }))
  }

  const getSourceStats = () => {
    const stats = {}
    messages.forEach((msg) => {
      const source = msg.source || 'unknown'
      stats[source] = (stats[source] || 0) + 1
    })
    return Object.entries(stats).map(([name, value]) => ({ name, value }))
  }

  const COLORS = ['#667eea', '#764ba2', '#f39c12', '#3498db', '#e74c3c', '#27ae60']

  if (loading) {
    return <div className="analytics-loading">Loading analytics...</div>
  }

  const decisionStats = getDecisionStats()
  const priorityDistribution = getPriorityDistribution()
  const sourceStats = getSourceStats()

  return (
    <div className="analytics">
      <div className="analytics-header">
        <h1>Analytics</h1>
        <select value={timeRange} onChange={(e) => setTimeRange(e.target.value)}>
          <option value="24h">Last 24 Hours</option>
          <option value="7d">Last 7 Days</option>
          <option value="30d">Last 30 Days</option>
          <option value="all">All Time</option>
        </select>
      </div>

      <div className="analytics-stats">
        <div className="stat-card">
          <div className="stat-value">{messages.length}</div>
          <div className="stat-label">Total Messages</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">
            {messages.filter((m) => m.priority_score).length > 0
              ? (
                  messages
                    .filter((m) => m.priority_score)
                    .reduce((sum, m) => sum + m.priority_score, 0) /
                  messages.filter((m) => m.priority_score).length
                ).toFixed(1)
              : 'N/A'}
          </div>
          <div className="stat-label">Avg Priority</div>
        </div>
      </div>

      <div className="analytics-charts">
        <div className="chart-card">
          <h2>Decision Distribution</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={decisionStats}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="value" fill="#667eea" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h2>Priority Distribution</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={priorityDistribution}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {priorityDistribution.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h2>Source Distribution</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={sourceStats}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {sourceStats.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}

export default Analytics

