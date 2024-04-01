import Link from 'next/link'

export default function NotFound() {
  return <div className=' text-white w-full min-h-screen absolute mx-auto flex flex-col justify-center items-center text-cente text-xl gap-10'>
      <h1 className='text-black dark:text-white'> (: اممم، همچین صفحه ای نداریم</h1>
      <div>
        <Link className='p-4 px-6 rounded  bg-slate-300 text-gray-600 hover:text-black  transition-all dark:bg-slate-800 dark:text-gray-300 dark:hover:text-gray-50 ' href="/">برگشت به صفحه اصلی</Link>
      </div>
  </div>
}