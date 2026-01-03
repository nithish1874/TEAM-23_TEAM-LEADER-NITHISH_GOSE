import { useState } from 'react'
import { getMessageReasoning } from '../services/api'
import './MessageCard.css'

function MessageCard({ message, onAction }) {
  const [showReasoning, setShowReasoning] = useState(false)
  const [reasoning, setReasoning] = useState(null)
  const [loadingReasoning, setLoadingReasoning] = useState(false)

  const getDecisionColor = (decision) => {
    switch (decision) {
      case 'SHOW':
        return '#e74c3c'
      case 'HIDE':
        return '#95a5a6'
      case 'POSTPONE':
        return '#f39c12'
      case 'SUMMARIZE':
        return '#3498db'
      default:
        return '#95a5a6'
    }
  }

  const handleShowReasoning = async () => {
    if (reasoning) {
      setShowReasoning(!showReasoning)
      return
    }

    try {
      setLoadingReasoning(true)
      const response = await getMessageReasoning(message.id)
      setReasoning(response.data)
      setShowReasoning(true)
    } catch (err) {
      console.error('Error fetching reasoning:', err)
    } finally {
      setLoadingReasoning(false)
    }
  }

  return (
    <div className="message-card">
      <div className="message-header">
        <div className="message-source">{message.source.toUpperCase()}</div>
        <div
          className="message-decision"
          style={{ backgroundColor: getDecisionColor(message.final_decision) }}
        >
          {message.final_decision}
        </div>
      </div>

      <div className="message-content">
        <div className="message-sender">
          <strong>From:</strong> {message.sender}
        </div>
        <div className="message-text">
          {message.content.substring(0, 200)}
          {message.content.length > 200 && '...'}
        </div>
        {message.priority_score && (
          <div className="message-metrics">
            <span className="metric">
              Priority: <strong>{message.priority_score.toFixed(1)}/10</strong>
            </span>
            {message.urgency_level && (
              <span className="metric">
                Urgency: <strong>{message.urgency_level}</strong>
              </span>
            )}
            {message.confidence_score && (
              <span className="metric">
                Confidence: <strong>{(message.confidence_score * 100).toFixed(0)}%</strong>
              </span>
            )}
          </div>
        )}
      </div>

      <div className="message-actions">
        <button
          onClick={handleShowReasoning}
          className="btn-secondary"
          disabled={loadingReasoning}
        >
          {loadingReasoning ? 'Loading...' : showReasoning ? 'Hide Reasoning' : 'Show Reasoning'}
        </button>
        {message.shown_to_user && (
          <>
            <button
              onClick={() => onAction(message.id, 'responded')}
              className="btn-success"
            >
              ✓ Responded
            </button>
            <button
              onClick={() => onAction(message.id, 'dismissed')}
              className="btn-secondary"
            >
              Dismiss
            </button>
          </>
        )}
      </div>

      {showReasoning && reasoning && (
        <div className="message-reasoning">
          <h4>AI Reasoning:</h4>
          <div className="reasoning-section">
            <p><strong>Priority Reasoning:</strong> {reasoning.priority_reasoning}</p>
            <p><strong>Context Explanation:</strong> {reasoning.context_explanation}</p>
            <p><strong>Focus Justification:</strong> {reasoning.focus_justification}</p>
            <p><strong>Final Decision:</strong> {reasoning.final_decision}</p>
            <p><strong>Supervisor Explanation:</strong> {reasoning.supervisor_explanation}</p>
          </div>
        </div>
      )}
    </div>
  )
}

export default MessageCard

