'use client'

import {  useState } from 'react'

import Link from "next/link";

export default function Inputs() {

  const [source, setsource] = useState('');
  const [destination, setdestination] = useState('');
  const sourcefun = event => {
    setsource(event.target.value)
  }
  const destinationfun = events => {
    setdestination(events.target.value)
  }
  return (

    <div className=" w-full min-h-screen absolute mx-auto flex flex-col justify-center items-center text-center text-black dark:text-white text-xl gap-4 -z-10">
      <p className=''>:ایستگاه مبدا </p>
      <input placeholder="مثلا تجریش" onChange={sourcefun} className='p-2 py-4 rounded-md text-center focus:outline-none focus-visible:ring-2  focus-visible:ring-slate-600 border-none bg-gray-300  text-black dark:text-white dark:bg-gray-800 placeholder-gray-500 dark:placeholder-gray-400 '/>
      <p>:ایستگاه مقصد  </p>
      <input placeholder="مثلا تئاتر شهر" onChange={destinationfun} className='p-2 py-4 rounded-md text-center focus:outline-none focus-visible:ring-2  focus-visible:ring-slate-600 border-none bg-gray-300  text-black dark:text-white dark:bg-gray-800 placeholder-gray-500 dark:placeholder-gray-400' />
      <Link className='p-3 mt-4 px-6 bg-gray-600 text-white rounded-md dark:bg-gray-700  dark:text-white '
          href={{
              pathname: '/showpath',
              query: { source: `${source}`, dist: `${destination}` } 
          }}
      >
          جستجوی مسیر
      </Link>
    </div>
  )
}
