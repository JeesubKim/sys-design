import './App.css'

import { BrowserRouter, Routes, Route } from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import ProblemListPage from './pages/ProblemDetailPage'
import LeaderboardPage from './pages/LeaderboardPage'
import LeaderboardDetailPage from './pages/LeaderboardDetailPage'
import ProblemDetailPage from './pages/ProblemDetailPage'

import {
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'

const queryClient = new QueryClient()

function App() {
  

  return (
    <QueryClientProvider client={queryClient}>
    <BrowserRouter>

      <Routes>
        <Route path='/' element={<LandingPage />} />
        <Route path='/problems' element={<ProblemListPage />} />
        <Route path='/problems/:id' element={<ProblemDetailPage />} />
        <Route path='/leaderboards' element={<LeaderboardPage />} />
        <Route path='/leaderboards/:id' element={<LeaderboardDetailPage />} />
      </Routes>
    </BrowserRouter>
    </QueryClientProvider>
  )
}

export default App
