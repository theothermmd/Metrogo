
import Image from "next/image";
import tehran from './tehran.jpg'
import esfehan from './esfehan.webp'
import tabriz from './tabriz.png'
import mashhad from './mashhad.webp'
function Maps() {
    return ( 
        <div className="container w-full h-dvh flex flex-col justify-center items-center  md:mx-auto select-none">
            <div className="grid md:grid-cols-2 grid-cols-1 gap-2 h-[500px] overflow-scroll md:overflow-auto">

                <div className="relative flex justify-center items-center">
                    <Image src={tehran} alt="Metrogo Logo" width={200} height={200} className="brightness-50 blur-[2px]"/>
                    <p className=" text-white absolute text-4xl">تهران</p>
                </div>
                <div className="relative flex justify-center items-center">
                    <Image src={esfehan} alt="Metrogo Logo" width={200} height={200} className="brightness-50 blur-[2px]"/>
                    <p className=" text-white absolute text-4xl">اصفهان</p>
                </div>
                <div className="relative flex justify-center items-center">
                    <Image src={tabriz} alt="Metrogo Logo" width={200} height={200} className="brightness-50 blur-[2px]"/>
                    <p className=" text-white absolute text-4xl">تبریز</p>
                </div>
                <div className="relative flex justify-center items-center">
                    <Image src={mashhad} alt="Metrogo Logo" width={200} height={200} className="brightness-50 blur-[2px]"/>
                    <p className=" text-white absolute text-4xl">مشهد</p>
                </div>

            </div>


        </div>
     );
}

export default Maps;