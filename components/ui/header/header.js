"use client";
import { useState } from "react";
import "./header.css";
import logo from "./logo.png";
import Image from "next/image";
export default function Header() {
  const [showNavbar, setShowNavbar] = useState(false);

  const handleShowNavbar = () => {
    setShowNavbar(!showNavbar);
  };



  return (
    <header className="absolute top-0 left-0 right-0 container flex flex-row-reverse items-center justify-between p-12 h-12 mx-auto select-none ">
      <div className="flex items-center gap-10 flex-row-reverse">
        <a
          href="/"
          className="flex gap-2 flex-row-reverse items-center z-30 group"
        >
          <Image src={logo} alt="Metrogo Logo" width={38} height={38} />
          <h1 className="hidden lg:inline-block text-slate-500 group-hover:text-black dark:text-slate-200 dark:group-hover:text-white">
            متروگو
          </h1>
        </a>
        <div className=" hidden lg:inline-block  ">
          <ul className="flex items-center gap-10  flex-row-reverse  text-slate-500 dark:text-slate-300">
            <a
              href="maps"
              className=" hover:text-black dark:hover:text-white  transition-all"
            >
              نقشه های مترو ایران
            </a>
            <a
              href="/about"
              className=" hover:text-black dark:hover:text-white  transition-all"
            >
              درباره متروگو
            </a>
          </ul>
        </div>
      </div>

      <div
        className={`${
          showNavbar &&
          " z-20 fixed right-0 top-0 bottom-0 left-0  flex flex-col items-center justify-center gap-10 shadow dark:bg-slate-950 bg-slate-50 "
        } ${!showNavbar && "hidden"}`}
      >
        <div className="inline-block  ">
          <ul className="flex items-center gap-10  flex-col  text-slate-500 dark:text-slate-300 text-2xl">
            <a
              href="maps"
              className=" hover:text-black dark:hover:text-white  transition-all"
            >
              <p>اعلانی ندارید</p>
            </a>
          </ul>
        </div>
        <p className=" decoratio absolute bottom-8 text-black dark:text-white ">
          {" "}
          <span className=" text-red-600 text-2xl">&#9829;</span> ساخته شده با{" "}
        </p>
      </div>

      <a href="/" className="lg:hidden text-slate-700 dark:text-slate-200 z-30">
        <h1>متروگو</h1>
      </a>


      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"         className="w-8 h-8 lg:hidden dark:invert z-30 hover:cursor-pointer"
        onClick={handleShowNavbar}>
        <path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
      </svg>


      <a href="https://github.com/mohamadrzm/metrogo" className="hidden lg:inline-flex cursor-pointer justify-center gap-2 text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700 me-2 mb-2">
        <svg
          className="dark:invert"
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
        >
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
        </svg>
        <p>مخزن گیت هاب</p>
      </a>
    </header>
  );
}
