import { useEffect, useState } from "react"
import { getMessages } from "../services/api"

export default function Dashboard() {
  const [messages, setMessages] = useState([])

  useEffect(() => {
    getMessages().then(res => setMessages(res.data))
  }, [])

  return (
    <div>
      <h2>Agent Decisions</h2>
      <ul>
        {messages.map(m => (
          <li key={m[0]}>
            <b>{m[2]}</b> → {m[4]} (Priority: {m[5]})
          </li>
        ))}
      </ul>
    </div>
  )
}
