import { Outlet, NavLink } from 'react-router-dom'

export default function Layout() {
  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      
      {/* Sidebar */}
      <aside style={{
        width: '220px',
        background: '#6b6bd6',
        color: 'white',
        padding: '20px'
      }}>
        <h2>Fatigue Manager</h2>

        <nav style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          <NavLink to="/dashboard" style={{ color: 'white' }}>
            Dashboard
          </NavLink>
          <NavLink to="/settings" style={{ color: 'white' }}>
            Settings
          </NavLink>
          <NavLink to="/analytics" style={{ color: 'white' }}>
            Analytics
          </NavLink>
        </nav>
      </aside>

      {/* Main content */}
      <main style={{ flex: 1, padding: '30px' }}>
        <Outlet />
      </main>
    </div>
  )
}
