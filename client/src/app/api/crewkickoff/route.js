import { NextResponse } from 'next/server'

export async function POST(req) {
  try {
    const { input } = await req.json()

    const response = await fetch('http://0.0.0.0:3001/crewkickoff', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input }),
    })

    if (!response.ok) {
      throw new Error('Backend API response was not ok')
    }

    const data = await response.json()

    return NextResponse.json(data)
  } catch (error) {
    console.error('Error in /api/crewkickoff:', error)
    return NextResponse.json({ error: 'An error occurred while processing your request.' }, { status: 500 })
  }
}
