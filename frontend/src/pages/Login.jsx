import { useState } from 'react'
import { getGmailAuthStatus } from '../services/api'
import './Login.css'

function Login() {
  const [loading, setLoading] = useState(false)

  const handleGmailAuth = async () => {
    try {
      setLoading(true)
      // In a real implementation, this would redirect to OAuth flow
      // For now, we'll just check status
      const response = await getGmailAuthStatus()
      if (response.data.authenticated) {
        alert('Gmail is already authenticated!')
      } else {
        alert('Gmail authentication not set up. Please configure Gmail OAuth credentials in the backend.')
      }
    } catch (err) {
      console.error('Error checking Gmail auth:', err)
      alert('Error checking Gmail authentication status')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="login">
      <div className="login-container">
        <div className="login-header">
          <h1>🧠 Digital Fatigue Manager</h1>
          <p>Your agentic AI assistant for managing digital overload</p>
        </div>

        <div className="login-content">
          <h2>Get Started</h2>
          <p>Connect your accounts to start managing your digital fatigue</p>

          <div className="auth-buttons">
            <button
              onClick={handleGmailAuth}
              disabled={loading}
              className="auth-btn gmail"
            >
              📧 Connect Gmail
            </button>
            <button
              disabled
              className="auth-btn slack"
              title="Slack integration requires backend configuration"
            >
              💬 Connect Slack (Configure in backend)
            </button>
          </div>

          <div className="login-footer">
            <p>
              <small>
                Note: This is a demo. For production use, configure OAuth credentials in the backend.
              </small>
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Login

