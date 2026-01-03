import './MentalLoadMeter.css'

function MentalLoadMeter({ score }) {
  const getScoreColor = (score) => {
    if (score === null || score === undefined) return '#95a5a6'
    if (score <= 30) return '#27ae60' // Green - Low
    if (score <= 60) return '#f39c12' // Orange - Medium
    return '#e74c3c' // Red - High
  }

  const getScoreLabel = (score) => {
    if (score === null || score === undefined) return 'No data'
    if (score <= 30) return 'Low'
    if (score <= 60) return 'Medium'
    return 'High'
  }

  const normalizedScore = score !== null && score !== undefined ? Math.min(100, Math.max(0, score)) : 0

  return (
    <div className="mental-load-meter">
      <h3>Mental Load Score</h3>
      <div className="meter-container">
        <div className="meter-bar">
          <div
            className="meter-fill"
            style={{
              width: `${normalizedScore}%`,
              backgroundColor: getScoreColor(score),
            }}
          />
        </div>
        <div className="meter-info">
          <span className="meter-score">
            {score !== null && score !== undefined ? score.toFixed(0) : 'N/A'}
          </span>
          <span className="meter-label" style={{ color: getScoreColor(score) }}>
            {getScoreLabel(score)}
          </span>
        </div>
      </div>
      <p className="meter-description">
        Lower is better. This score reflects your digital burden based on message volume and filtering effectiveness.
      </p>
    </div>
  )
}

export default MentalLoadMeter

