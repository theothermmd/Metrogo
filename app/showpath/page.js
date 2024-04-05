



// or only core styles

import axios from 'axios';



async function getText (source, dist) {
    try {
    const response = await axios.post('http://127.0.0.1:5000/getbestpath', {
        source: source,
        dist: dist,
        lang : 'FARSI'
    } , {headers: {'Content-Type': 'multipart/form-data'}});

    console.log(response.data);
    return response.data

    } 

    catch (error) 

    {

    console.error(error);

    }

}

export default async function Show({ searchParams }) {



    let sources = searchParams.source;
    let dists = searchParams.dist;
    var dataArray;
    
    try {
        const datas = await getText(searchParams.source,searchParams.dist);
        dataArray = Object.entries(datas).map(([key, value]) => ({
            id: key,
            name: value
          }));

    } catch {
        return (
            <div className=' text-white flex flex-col justify-center items-center gap-5  h-dvh w-full text-2xl'>
                <p className=' rounded bg-red-900 py-4 px-8'> :( مشکلی پیش اومده دوباره امتحان کنید </p>
                <a href='/' className=' rounded b bg-slate-800 text-slate-300  hover:text-white py-4 px-8'>تلاش دوباره</a>
            </div>
        )


    }

    


    return (
        <div className=" container w-full h-dvh text-white flex flex-col justify-center items-center mx-auto px-8">
            <div className=' w-full text-center overflow-scroll h-[500px] no-scrollbar snap-center select-none p-4 rounded-3xl' >

                {dataArray.map(item => (
                                <div className=' bg-slate-900 py-8 text-2xl ring-2 ring-slate-600  rounded-md my-8' key={item.id}>{item.name}</div>
                            ))}

            </div>
        </div>
    );
} 