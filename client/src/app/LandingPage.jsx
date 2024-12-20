'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { Footer } from './components/Footer'
import {response} from './data.js'

export default function LandingPage() {
  const [selectedItem, setSelectedItem] = useState(null)
  const words = "Welcome to my app".split(" ")

  const handleSubmit = () => {
    setSelectedItem(response[0])
  }

  return (
    <div className="min-h-screen flex flex-col">
      <main className="flex-grow flex items-center justify-center overflow-auto">
        <div className="w-full max-w-4xl mx-auto px-4 py-8">
          {!selectedItem ? (
            <div className="text-center">
              {words.map((word, index) => (
                <motion.span
                  key={index}
                  className="inline-block text-4xl sm:text-6xl md:text-7xl font-bold text-gray-800 mr-2 sm:mr-4"
                  initial={{ opacity: 0, y: 50 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{
                    duration: 0.5,
                    delay: index * 0.1,
                    ease: [0.6, -0.05, 0.01, 0.99],
                  }}
                >
                  {word}
                </motion.span>
              ))}
            </div>
          ) : (
            <div className="bg-white p-8 rounded-lg shadow-md w-full">
              <h2 className="text-2xl font-bold mb-4">{selectedItem}</h2>
            </div>
          )}
        </div>
      </main>
      <Footer onSubmit={handleSubmit} />
    </div>
  )
}

