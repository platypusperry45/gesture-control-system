import { useEffect, useState } from "react";

import {
    Stack,
    Typography,
    Chip,
    LinearProgress,
    Divider,
} from "@mui/material";

import PsychologyRoundedIcon from "@mui/icons-material/PsychologyRounded";
import ModelTrainingRoundedIcon from "@mui/icons-material/ModelTrainingRounded";
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded";
import TimelineRoundedIcon from "@mui/icons-material/TimelineRounded";

import GlassCard from "../ui/GlassCard";

import api from "../../services/api";

export default function AISettings() {

    const [model, setModel] = useState({
        loaded:false,
        checkpoint:"",
    });

    const [training, setTraining] = useState({
        running:false,
        completed:false,
        epoch:0,
        total_epochs:0,
        progress:0,
        val_accuracy:0,
    });

    useEffect(() => {

        const load = async () => {

            try {

                const [modelRes, trainingRes] = await Promise.all([
                    api.get("/model/status"),
                    api.get("/training/status"),
                ]);

                setModel(modelRes.data);
                setTraining(trainingRes.data);

            } catch (err) {

                console.error(err);

            }

        };

        load();

        const interval = setInterval(load,1000);

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

                <PsychologyRoundedIcon color="primary"/>

                <Typography
                    variant="h6"
                    fontWeight={700}
                >
                    AI Settings
                </Typography>

            </Stack>

            <Stack spacing={3}>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                >

                    <Typography>

                        Model Status

                    </Typography>

                    <Chip

                        color={model.loaded ? "success":"error"}

                        label={model.loaded ? "Loaded":"Not Loaded"}

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

                        <ModelTrainingRoundedIcon/>

                        <Typography>

                            Training

                        </Typography>

                    </Stack>

                    <Chip

                        color={
                            training.running
                                ? "warning"
                                : training.completed
                                ? "success"
                                : "default"
                        }

                        label={
                            training.running
                                ? "Running"
                                : training.completed
                                ? "Completed"
                                : "Idle"
                        }

                    />

                </Stack>

                <Divider/>

                <Stack spacing={1}>

                    <Stack
                        direction="row"
                        justifyContent="space-between"
                    >

                        <Typography>

                            Progress

                        </Typography>

                        <Typography fontWeight={700}>

                            {training.progress}%

                        </Typography>

                    </Stack>

                    <LinearProgress

                        variant="determinate"

                        value={training.progress}

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

                        <TimelineRoundedIcon/>

                        <Typography>

                            Epoch

                        </Typography>

                    </Stack>

                    <Typography fontWeight={700}>

                        {training.epoch}/{training.total_epochs}

                    </Typography>

                </Stack>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <CheckCircleRoundedIcon/>

                        <Typography>

                            Validation Accuracy

                        </Typography>

                    </Stack>

                    <Typography fontWeight={700}>

                        {(training.val_accuracy*100).toFixed(2)}%

                    </Typography>

                </Stack>

            </Stack>

        </GlassCard>

    );

}