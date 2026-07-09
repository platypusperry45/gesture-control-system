import { useEffect, useState } from "react";
import api from "../services/api";

export default function useTraining(){

    const [status,setStatus]=useState({});

    const [logs,setLogs]=useState([]);

    async function load(){

        const s=await api.get("/training/status");

        setStatus(s.data);

        const l=await api.get("/training/logs");

        setLogs(l.data);

    }

    useEffect(()=>{

        load();

        const id=setInterval(load,1000);

        return()=>clearInterval(id);

    },[]);

    return{

        status,

        logs,

        refresh:load,

    };

}