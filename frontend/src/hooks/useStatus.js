import { useEffect, useState } from "react";

import api from "../services/api";


export default function useStatus(){

    const [status,setStatus] = useState({

        camera:false,

        model_loaded:false,

        inference_running:false,

        fps:0,

        uptime:"--",

    });


    async function fetchStatus(){

        try{

            const response =
                await api.get("/status");


            setStatus(response.data);


        }
        catch(error){

            console.error(
                "Status fetch failed",
                error
            );

        }

    }



    useEffect(()=>{


        fetchStatus();


        const interval =
            setInterval(
                fetchStatus,
                2000
            );


        return ()=>clearInterval(interval);


    },[]);



    return status;

}