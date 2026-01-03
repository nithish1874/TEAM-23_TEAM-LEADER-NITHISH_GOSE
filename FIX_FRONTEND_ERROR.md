# Fix Frontend Error - Path with Spaces Issue

## Problem

The error occurs because the folder name has spaces:
- `"Agentic AI to Manage Digital & AI Fatigue"`

This causes npm/node to have path resolution issues.

## Error Messages:
1. `'AI' is not recognized as an internal or external command` - Path being split incorrectly
2. `Error: Cannot find module 'C:\Users\krupa\Desktop\vite\bin\vite.js'` - Looking in wrong location

## Solutions

### Solution 1: Reinstall Dependencies (Recommended)

```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
Remove-Item node_modules -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item package-lock.json -Force -ErrorAction SilentlyContinue
npm install
npm run dev
```

### Solution 2: Use npx vite directly

```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npx vite
```

### Solution 3: Use full path in quotes

Make sure you're always using quotes around the path:
```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npm run dev
```

### Solution 4: Use short path (if needed)

If the above don't work, you can use the 8.3 short path format:
```powershell
# Get short path
cd "C:\Users\krupa\Desktop"
cmd /c for %I in ("Agentic AI to Manage Digital & AI Fatigue") do @echo %~sI
```

---

## Quick Fix Commands

Run these commands in order:

```powershell
# 1. Navigate to frontend (with quotes!)
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"

# 2. Clean up
Remove-Item node_modules -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item package-lock.json -Force -ErrorAction SilentlyContinue

# 3. Reinstall
npm install

# 4. Run
npm run dev
```

---

## Alternative: Use npx

If npm run dev still doesn't work, try:

```powershell
cd "C:\Users\krupa\Desktop\Agentic AI to Manage Digital & AI Fatigue\frontend"
npx vite
```

This should work even with the path issues.

---

## Why This Happens

Windows path handling with spaces can cause issues when:
- npm scripts try to resolve paths
- Node modules use PATH resolution
- The folder name contains multiple spaces and special characters

Always use quotes around paths with spaces in PowerShell!

