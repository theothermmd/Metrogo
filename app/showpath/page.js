



// or only core styles

import axios from 'axios';



async function getText (source, dist) {
    try {
    const response = await axios.post('https://mohamadreza.pythonanywhere.com/getbestpath', {
        source: source,
        dist: dist,
        lang : 'FARSI'
    } , {headers: {'Content-Type': 'application/json'}});

    console.log(response.data);
    return response.data

    } 

    catch (error) 

    {

    console.error(error);

    }

}

export default async function Show({ searchParams }) {


    var dataArray;
    
    try {
        const datas = await getText(searchParams.source,searchParams.dist);
        dataArray = datas
        if (datas == "error-source") {
            return (
                <div className=' text-white flex flex-col justify-center items-center gap-5  h-dvh w-full text-2xl'>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-32 h-32 text-red-600">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z" />
                    </svg>
                    <p className=' rounded bg-red-950 py-4 px-8'>ایستگاه مبدا را به درستی وارد نکردید :(</p>
                    <a href='/' className=' rounded b bg-slate-800 text-slate-300  hover:text-white py-4 px-8'>تلاش دوباره</a>
                </div>
            )
        }
        else if (datas == "error-dist") {
            return (
                <div className=' text-white flex flex-col justify-center items-center gap-5  h-dvh w-full text-2xl'>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-32 h-32 text-red-600">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z" />
                    </svg>

                    <p className=' rounded bg-slate-900 py-4 px-8'>ایستگاه مقصد را به درستی وارد نکردید :(</p>
                    <a href='/' className=' rounded b bg-slate-800 text-slate-300  hover:text-white py-4 px-8'>تلاش دوباره</a>
                </div>
            )
        }
        else if (datas == "error-dist-source") {
            return (
                <div className=' text-white flex flex-col justify-center items-center gap-5  h-dvh w-full text-2xl'>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-32 h-32 text-red-600">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z" />
                    </svg>
                    <p className=' text-xl rounded bg-red-950 py-4 px-4'>ایستگاه مبدا و مقصد را به درستی وارد نکردید :(</p>
                    <a href='/' className=' rounded b bg-slate-800 text-slate-300  hover:text-white py-4 px-8'>تلاش دوباره</a>
                </div>
            )
        }


    } catch {
        return (
            <div className=' text-white flex flex-col justify-center items-center gap-5  h-dvh w-full text-2xl'>
                <p className=' rounded bg-red-950 py-4 px-8'> :( مشکلی پیش اومده دوباره امتحان کنید </p>
                <a href='/' className=' rounded b bg-slate-800 text-slate-300  hover:text-white py-4 px-8'>تلاش دوباره</a>
            </div>
        )


    }

    


    return (
        <div className=" container w-full h-dvh text-white flex flex-col justify-center items-center mx-auto px-8  lg:flex-row-reverse lg:gap-20">
            <p className=' text-xl mb-12 text-gray-600 dark:text-gray-300'>زمان رسیدن شما 
            <span className=' text-gray-800 dark:text-white bg-gray-300 text-3xl mx-2 dark:bg-slate-800 rounded-md px-2'>{dataArray['time']}</span> 
              دقیقه میباشد</p>
            <div className=' w-full text-center overflow-scroll h-[60%] no-scrollbar snap-center select-none px-4 rounded-2xl md:w-[400px] ring-2 ring-gray-200 dark:ring-slate-800' >
            
            {dataArray['stations'].map(item => (
                                <div className='bg-gray-300 text-black dark:bg-slate-900 py-8 text-2xl dark:ring-2 dark:ring-slate-600 dark:text-white rounded-2xl  my-8' key={1}>{item}</div>
                            ))}

            </div>
        </div>
    );
} 