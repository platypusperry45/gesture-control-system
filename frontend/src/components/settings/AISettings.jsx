import { useState } from "react";

import {
    Stack,
    Typography,
    FormControl,
    InputLabel,
    Select,
    MenuItem,
    Slider,
    Switch,
    Divider,
    Button,
    Chip,
} from "@mui/material";

import PsychologyRoundedIcon from "@mui/icons-material/PsychologyRounded";
import MemoryRoundedIcon from "@mui/icons-material/MemoryRounded";
import TuneRoundedIcon from "@mui/icons-material/TuneRounded";
import RefreshRoundedIcon from "@mui/icons-material/RefreshRounded";

import GlassCard from "../ui/GlassCard";

export default function AISettings() {

    const [model, setModel] = useState("gesture_recognition.weights.h5");

    const [threshold, setThreshold] = useState(0.85);

    const [gpu, setGpu] = useState(true);

    const [smoothing, setSmoothing] = useState(true);

    const [autoReload, setAutoReload] = useState(true);

    return (

        <GlassCard
            sx={{
                p:3,
                height:"100%",
            }}
        >

            <Stack

                direction="row"

                justifyContent="space-between"

                alignItems="center"

                mb={3}

            >

                <Stack
                    direction="row"
                    spacing={1}
                    alignItems="center"
                >

                    <PsychologyRoundedIcon color="primary"/>

                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        AI Settings
                    </Typography>

                </Stack>

                <Chip

                    label="Model Loaded"

                    color="success"

                />

            </Stack>

            <Stack spacing={3}>

                <FormControl fullWidth>

                    <InputLabel>

                        Active Model

                    </InputLabel>

                    <Select

                        value={model}

                        label="Active Model"

                        onChange={(e)=>setModel(e.target.value)}

                    >

                        <MenuItem value="gesture_recognition.weights.h5">

                            gesture_recognition.weights.h5

                        </MenuItem>

                        <MenuItem value="best.weights.h5">

                            best.weights.h5

                        </MenuItem>

                        <MenuItem value="experimental.weights.h5">

                            experimental.weights.h5

                        </MenuItem>

                    </Select>

                </FormControl>

                <Divider/>

                <Stack
                    spacing={1}
                >

                    <Typography
                        fontWeight={600}
                    >
                        Confidence Threshold
                    </Typography>

                    <Slider

                        value={threshold}

                        min={0.50}

                        max={1}

                        step={0.01}

                        valueLabelDisplay="auto"

                        valueLabelFormat={(v)=>`${Math.round(v*100)}%`}

                        onChange={(e,v)=>setThreshold(v)}

                    />

                    <Typography
                        color="text.secondary"
                    >

                        Current Threshold: <b>{Math.round(threshold*100)}%</b>

                    </Typography>

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

                        <MemoryRoundedIcon/>

                        <Typography>

                            GPU Acceleration

                        </Typography>

                    </Stack>

                    <Switch

                        checked={gpu}

                        onChange={(e)=>setGpu(e.target.checked)}

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

                        <TuneRoundedIcon/>

                        <Typography>

                            Prediction Smoothing

                        </Typography>

                    </Stack>

                    <Switch

                        checked={smoothing}

                        onChange={(e)=>setSmoothing(e.target.checked)}

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

                        <RefreshRoundedIcon/>

                        <Typography>

                            Auto Reload Model

                        </Typography>

                    </Stack>

                    <Switch

                        checked={autoReload}

                        onChange={(e)=>setAutoReload(e.target.checked)}

                    />

                </Stack>

                <Divider/>

                <Button

                    variant="contained"

                    fullWidth

                >

                    Reload AI Model

                </Button>

            </Stack>

        </GlassCard>

    );

}