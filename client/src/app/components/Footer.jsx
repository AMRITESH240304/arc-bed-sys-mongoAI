'use client'

import { useState } from 'react'
import { Textarea } from "@/components/ui/textarea"
import { Button } from "@/components/ui/button"

export function Footer({ onSubmit }) {
  const [text, setText] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('Submitted text:', text)
    setText('') // Clear the textarea after submission
    onSubmit() // Call the onSubmit function passed from the parent
  }

  return (
    <footer className="w-full py-6 px-4 border-t bg-white">
      <form onSubmit={handleSubmit} className="max-w-4xl mx-auto space-y-4">
        <Textarea
          placeholder="Enter your long text here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="min-h-[150px] w-full"
        />
        <Button type="submit" className="w-full sm:w-auto">Submit</Button>
      </form>
    </footer>
  )
}

