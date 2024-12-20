'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

export default function ChatPage() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (input.trim()) {
      setIsLoading(true)
      const newMessage = { id: Date.now(), content: input, sender: 'user' }
      setMessages(prevMessages => [...prevMessages, newMessage])
      setInput('')

      try {
        const response = await fetch('/api/crewkickoff', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ input }),
        })

        if (!response.ok) {
          throw new Error('Network response was not ok')
        }

        const data = await response.json()
        const responseMessage = { 
          id: Date.now() + 1, 
          content: JSON.stringify(data.end_result, null, 2), 
          sender: 'other' 
        }
        setMessages(prevMessages => [...prevMessages, responseMessage])
      } catch (error) {
        console.error('Error:', error)
        const errorMessage = { 
          id: Date.now() + 1, 
          content: 'An error occurred while processing your request.', 
          sender: 'other' 
        }
        setMessages(prevMessages => [...prevMessages, errorMessage])
      } finally {
        setIsLoading(false)
      }
    }
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100 p-4">
      <Card className="w-full max-w-2xl">
        <CardHeader>
          <CardTitle>Chat</CardTitle>
        </CardHeader>
        <CardContent>
          <ScrollArea className="h-[60vh] pr-4">
            {messages.map((message) => (
              <div key={message.id} className={`mb-4 flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`flex items-start gap-2.5 ${message.sender === 'user' ? 'flex-row-reverse' : ''}`}>
                  <Avatar>
                    <AvatarImage src={message.sender === 'user' ? '/placeholder.svg?height=40&width=40' : '/placeholder.svg?height=40&width=40'} />
                    <AvatarFallback>{message.sender === 'user' ? 'U' : 'O'}</AvatarFallback>
                  </Avatar>
                  <div className={`flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 ${message.sender === 'user' ? 'bg-blue-500 text-white rounded-s-xl rounded-ee-xl' : 'bg-gray-200 rounded-e-xl rounded-es-xl'}`}>
                    <p className="text-sm font-normal whitespace-pre-wrap">{message.content}</p>
                  </div>
                </div>
              </div>
            ))}
          </ScrollArea>
        </CardContent>
        <CardFooter>
          <form onSubmit={handleSubmit} className="flex w-full space-x-2">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your message..."
              className="flex-grow"
              disabled={isLoading}
            />
            <Button type="submit" disabled={isLoading}>
              {isLoading ? 'Sending...' : 'Send'}
            </Button>
          </form>
        </CardFooter>
      </Card>
    </div>
  )
}
