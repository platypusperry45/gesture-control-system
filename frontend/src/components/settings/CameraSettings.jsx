import { useEffect, useState } from "react";

import {
    Stack,
    Typography,
    Chip,
    LinearProgress,
    Divider,
} from "@mui/material";

import CameraAltRoundedIcon from "@mui/icons-material/CameraAltRounded";
import VideocamRoundedIcon from "@mui/icons-material/VideocamRounded";
import SpeedRoundedIcon from "@mui/icons-material/SpeedRounded";
import FrontHandRoundedIcon from "@mui/icons-material/FrontHandRounded";

import GlassCard from "../ui/GlassCard";

import api from "../../services/api";

export default function CameraSettings() {

    const [status, setStatus] = useState({

        camera:false,
        inference_running:false,
        fps:0,
        hand_detected:false,

    });

    useEffect(() => {

        const load = async () => {

            try{

                const res = await api.get("/status");

                setStatus(res.data);

            }

            catch(err){

                console.error(err);

            }

        };

        load();

        const interval = setInterval(load,500);

        return ()=>clearInterval(interval);

    },[]);

    return (

        <GlassCard
            sx={{
                p:3,
                height:"100%",
            }}
        >

            <Stack
                direction="row"
                spacing={1}
                alignItems="center"
                mb={3}
            >

                <CameraAltRoundedIcon color="primary"/>

                <Typography
                    variant="h6"
                    fontWeight={700}
                >
                    Camera Settings
                </Typography>

            </Stack>

            <Stack spacing={3}>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                >

                    <Typography>

                        Camera

                    </Typography>

                    <Chip

                        color={status.camera ? "success":"error"}

                        label={status.camera ? "Connected":"Offline"}

                    />

                </Stack>

                <Divider/>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <VideocamRoundedIcon/>

                        <Typography>

                            Inference

                        </Typography>

                    </Stack>

                    <Chip

                        color={status.inference_running ? "success":"default"}

                        label={status.inference_running ? "Running":"Stopped"}

                    />

                </Stack>

                <Divider/>

                <Stack spacing={1}>

                    <Stack
                        direction="row"
                        justifyContent="space-between"
                    >

                        <Stack
                            direction="row"
                            spacing={1}
                            alignItems="center"
                        >

                            <SpeedRoundedIcon/>

                            <Typography>

                                FPS

                            </Typography>

                        </Stack>

                        <Typography fontWeight={700}>

                            {status.fps.toFixed(1)}

                        </Typography>

                    </Stack>

                    <LinearProgress

                        variant="determinate"

                        value={Math.min(status.fps*3.3,100)}

                    />

                </Stack>

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

                        <FrontHandRoundedIcon/>

                        <Typography>

                            Hand Detection

                        </Typography>

                    </Stack>

                    <Chip

                        color={status.hand_detected ? "success":"warning"}

                        label={status.hand_detected ? "Detected":"Searching"}

                    />

                </Stack>

            </Stack>

        </GlassCard>

    );

}