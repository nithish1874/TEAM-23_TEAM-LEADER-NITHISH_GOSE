import { useState } from 'react'
import { updateFocusMode } from '../services/api'
import './FocusModeToggle.css'

function FocusModeToggle({ currentMode, onUpdate }) {
  const [loading, setLoading] = useState(false)

  const modes = [
    { value: 'deep_work', label: 'Deep Work', icon: '🎯', description: 'Only critical messages (priority 9-10)' },
    { value: 'normal', label: 'Normal', icon: '⚡', description: 'Priority 6+ shown immediately' },
    { value: 'relax', label: 'Relax', icon: '😌', description: 'Only emergencies (priority 10)' },
  ]

  const handleModeChange = async (mode) => {
    try {
      setLoading(true)
      await updateFocusMode(mode)
      if (onUpdate) onUpdate()
    } catch (err) {
      console.error('Error updating focus mode:', err)
      alert('Error updating focus mode')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="focus-mode-toggle">
      <h3>Focus Mode</h3>
      <div className="mode-buttons">
        {modes.map((mode) => (
          <button
            key={mode.value}
            onClick={() => handleModeChange(mode.value)}
            disabled={loading}
            className={`mode-btn ${currentMode === mode.value ? 'active' : ''}`}
          >
            <span className="mode-icon">{mode.icon}</span>
            <div className="mode-info">
              <div className="mode-label">{mode.label}</div>
              <div className="mode-description">{mode.description}</div>
            </div>
          </button>
        ))}
      </div>
    </div>
  )
}

export default FocusModeToggle

