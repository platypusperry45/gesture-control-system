import { useEffect, useState } from "react";

import {
    Stack,
    Typography,
    Chip,
    Divider,
    LinearProgress,
} from "@mui/material";

import MemoryRoundedIcon from "@mui/icons-material/MemoryRounded";
import SpeedRoundedIcon from "@mui/icons-material/SpeedRounded";
import CameraAltRoundedIcon from "@mui/icons-material/CameraAltRounded";
import PsychologyRoundedIcon from "@mui/icons-material/PsychologyRounded";
import AccessTimeRoundedIcon from "@mui/icons-material/AccessTimeRounded";

import GlassCard from "../ui/GlassCard";

import api from "../../services/api";

export default function SystemSettings() {

    const [system, setSystem] = useState({

        cpu:0,
        ram:0,
        uptime:"00:00:00",

        camera:false,
        model:false,
        prediction:null,
        confidence:0,
        fps:0,

    });

    useEffect(() => {

        const load = async () => {

            try{

                const res = await api.get("/analytics");

                const data = res.data;

                setSystem({

                    cpu:data.system.cpu,
                    ram:data.system.ram,
                    uptime:data.runtime.uptime,

                    camera:data.runtime.camera,
                    model:data.model.loaded,

                    prediction:data.runtime.prediction,
                    confidence:data.runtime.confidence,
                    fps:data.runtime.fps,

                });

            }
            catch(err){

                console.error(err);

            }

        };

        load();

        const timer = setInterval(load,1000);

        return ()=>clearInterval(timer);

    },[]);

    return(

        <GlassCard
            sx={{
                p:3,
            }}
        >

            <Stack
                direction="row"
                spacing={1}
                alignItems="center"
                mb={3}
            >

                <MemoryRoundedIcon color="primary"/>

                <Typography
                    variant="h6"
                    fontWeight={700}
                >

                    System Status

                </Typography>

            </Stack>

            <Stack spacing={3}>

                <div>

                    <Stack
                        direction="row"
                        justifyContent="space-between"
                        mb={1}
                    >

                        <Typography>

                            CPU Usage

                        </Typography>

                        <Typography fontWeight={700}>

                            {system.cpu}%

                        </Typography>

                    </Stack>

                    <LinearProgress
                        variant="determinate"
                        value={system.cpu}
                    />

                </div>

                <div>

                    <Stack
                        direction="row"
                        justifyContent="space-between"
                        mb={1}
                    >

                        <Typography>

                            RAM Usage

                        </Typography>

                        <Typography fontWeight={700}>

                            {system.ram}%

                        </Typography>

                    </Stack>

                    <LinearProgress
                        variant="determinate"
                        value={system.ram}
                    />

                </div>

                <Divider/>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <AccessTimeRoundedIcon/>

                        <Typography>

                            Uptime

                        </Typography>

                    </Stack>

                    <Typography fontWeight={700}>

                        {system.uptime}

                    </Typography>

                </Stack>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <CameraAltRoundedIcon/>

                        <Typography>

                            Camera

                        </Typography>

                    </Stack>

                    <Chip

                        color={system.camera ? "success":"error"}

                        label={system.camera ? "Active":"Offline"}

                    />

                </Stack>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <PsychologyRoundedIcon/>

                        <Typography>

                            Model

                        </Typography>

                    </Stack>

                    <Chip

                        color={system.model ? "success":"error"}

                        label={system.model ? "Loaded":"Missing"}

                    />

                </Stack>

                <Divider/>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                >

                    <Typography>

                        Live FPS

                    </Typography>

                    <Typography fontWeight={700}>

                        {system.fps}

                    </Typography>

                </Stack>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                >

                    <Typography>

                        Prediction

                    </Typography>

                    <Typography fontWeight={700}>

                        {system.prediction ?? "--"}

                    </Typography>

                </Stack>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                >

                    <Typography>

                        Confidence

                    </Typography>

                    <Typography fontWeight={700}>

                        {system.confidence.toFixed(2)}%

                    </Typography>

                </Stack>

            </Stack>

        </GlassCard>

    );

}