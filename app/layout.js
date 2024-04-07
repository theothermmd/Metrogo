import { SpeedInsights } from "@vercel/speed-insights/next"
import "./globals.css";
import Header from '@/components/ui/header/header'
import Footer from '@/components/ui/footer/footer'
import Head from 'next/head'
export const metadata = {
  title: "متروگو",
  description: "متروگو بهتون کمک میکنه بهترین و سریع ترین مسیر رو برای استفاده از مترو پیدا کنید. کار باهاش آسونه، قشنگه و امنه.",
  icons: {
    icon: "./favicon.ico",
  },
  manifest: "/manifest.json",
};

export default function RootLayout({ children }) {
  return (
    <html className=" dark:bg-slate-950 bg-slate-50 scroll-smooth" lang="en">
      <head>

      <meta property="og:title" content="مکس" />
      <meta property="og:url" content="https://metrogo.vercel.app/" />
      <meta property="og:image" content="./banner.png" />

      </head>

      <body>
        <Header/>
        {children}
        <SpeedInsights />
        <Footer/>
        </body>
    </html>
  );
}
