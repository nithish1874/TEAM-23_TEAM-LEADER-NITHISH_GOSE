import { useState, useEffect } from 'react'
import { getSettings, updateSettings } from '../services/api'
import './Settings.css'

function Settings() {
  const [settings, setSettings] = useState(null)
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [formData, setFormData] = useState({
    working_hours_start: '09:00',
    working_hours_end: '17:00',
    working_days: 'mon,tue,wed,thu,fri',
    important_contacts: [],
    priority_keywords: ['urgent', 'deadline', 'asap', 'important'],
    notification_enabled: true,
    daily_summary_enabled: true,
    summary_time: '18:00',
  })
  const [newContact, setNewContact] = useState('')
  const [newKeyword, setNewKeyword] = useState('')

  useEffect(() => {
    loadSettings()
  }, [])

  const loadSettings = async () => {
    try {
      setLoading(true)
      const response = await getSettings()
      const data = response.data
      setSettings(data)
      setFormData({
        working_hours_start: data.working_hours_start || '09:00',
        working_hours_end: data.working_hours_end || '17:00',
        working_days: data.working_days || 'mon,tue,wed,thu,fri',
        important_contacts: data.important_contacts || [],
        priority_keywords: data.priority_keywords || ['urgent', 'deadline', 'asap', 'important'],
        notification_enabled: data.notification_enabled !== false,
        daily_summary_enabled: data.daily_summary_enabled !== false,
        summary_time: data.summary_time || '18:00',
      })
    } catch (err) {
      console.error('Error loading settings:', err)
      alert('Error loading settings')
    } finally {
      setLoading(false)
    }
  }

  const handleSave = async () => {
    try {
      setSaving(true)
      await updateSettings(formData)
      alert('Settings saved successfully!')
      loadSettings()
    } catch (err) {
      console.error('Error saving settings:', err)
      alert('Error saving settings')
    } finally {
      setSaving(false)
    }
  }

  const handleAddContact = () => {
    if (newContact.trim()) {
      setFormData({
        ...formData,
        important_contacts: [...formData.important_contacts, newContact.trim()],
      })
      setNewContact('')
    }
  }

  const handleRemoveContact = (index) => {
    setFormData({
      ...formData,
      important_contacts: formData.important_contacts.filter((_, i) => i !== index),
    })
  }

  const handleAddKeyword = () => {
    if (newKeyword.trim() && !formData.priority_keywords.includes(newKeyword.trim().toLowerCase())) {
      setFormData({
        ...formData,
        priority_keywords: [...formData.priority_keywords, newKeyword.trim().toLowerCase()],
      })
      setNewKeyword('')
    }
  }

  const handleRemoveKeyword = (index) => {
    setFormData({
      ...formData,
      priority_keywords: formData.priority_keywords.filter((_, i) => i !== index),
    })
  }

  if (loading) {
    return <div className="settings-loading">Loading settings...</div>
  }

  return (
    <div className="settings">
      <h1>Settings</h1>

      <div className="settings-section">
        <h2>Working Hours</h2>
        <div className="form-group">
          <label>Start Time</label>
          <input
            type="time"
            value={formData.working_hours_start}
            onChange={(e) => setFormData({ ...formData, working_hours_start: e.target.value })}
          />
        </div>
        <div className="form-group">
          <label>End Time</label>
          <input
            type="time"
            value={formData.working_hours_end}
            onChange={(e) => setFormData({ ...formData, working_hours_end: e.target.value })}
          />
        </div>
        <div className="form-group">
          <label>Working Days (comma-separated: mon,tue,wed,thu,fri)</label>
          <input
            type="text"
            value={formData.working_days}
            onChange={(e) => setFormData({ ...formData, working_days: e.target.value })}
          />
        </div>
      </div>

      <div className="settings-section">
        <h2>Important Contacts</h2>
        <div className="form-group">
          <div className="input-with-button">
            <input
              type="text"
              placeholder="Email or name"
              value={newContact}
              onChange={(e) => setNewContact(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleAddContact()}
            />
            <button onClick={handleAddContact}>Add</button>
          </div>
        </div>
        <div className="tag-list">
          {formData.important_contacts.map((contact, index) => (
            <span key={index} className="tag">
              {contact}
              <button onClick={() => handleRemoveContact(index)}>×</button>
            </span>
          ))}
        </div>
      </div>

      <div className="settings-section">
        <h2>Priority Keywords</h2>
        <div className="form-group">
          <div className="input-with-button">
            <input
              type="text"
              placeholder="Keyword"
              value={newKeyword}
              onChange={(e) => setNewKeyword(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleAddKeyword()}
            />
            <button onClick={handleAddKeyword}>Add</button>
          </div>
        </div>
        <div className="tag-list">
          {formData.priority_keywords.map((keyword, index) => (
            <span key={index} className="tag">
              {keyword}
              <button onClick={() => handleRemoveKeyword(index)}>×</button>
            </span>
          ))}
        </div>
      </div>

      <div className="settings-section">
        <h2>Notifications</h2>
        <div className="form-group checkbox-group">
          <label>
            <input
              type="checkbox"
              checked={formData.notification_enabled}
              onChange={(e) => setFormData({ ...formData, notification_enabled: e.target.checked })}
            />
            Enable notifications
          </label>
        </div>
        <div className="form-group checkbox-group">
          <label>
            <input
              type="checkbox"
              checked={formData.daily_summary_enabled}
              onChange={(e) => setFormData({ ...formData, daily_summary_enabled: e.target.checked })}
            />
            Enable daily summary
          </label>
        </div>
        <div className="form-group">
          <label>Daily Summary Time</label>
          <input
            type="time"
            value={formData.summary_time}
            onChange={(e) => setFormData({ ...formData, summary_time: e.target.value })}
          />
        </div>
      </div>

      <div className="settings-actions">
        <button onClick={handleSave} className="btn-primary" disabled={saving}>
          {saving ? 'Saving...' : 'Save Settings'}
        </button>
      </div>
    </div>
  )
}

export default Settings

