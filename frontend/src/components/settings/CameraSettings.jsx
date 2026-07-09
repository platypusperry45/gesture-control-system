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
} from "@mui/material";

import CameraAltRoundedIcon from "@mui/icons-material/CameraAltRounded";
import VideocamRoundedIcon from "@mui/icons-material/VideocamRounded";
import FlipRoundedIcon from "@mui/icons-material/FlipRounded";
import RestartAltRoundedIcon from "@mui/icons-material/RestartAltRounded";

import GlassCard from "../ui/GlassCard";

export default function CameraSettings() {

    const [camera, setCamera] = useState("Default Camera");
    const [resolution, setResolution] = useState("1280x720");
    const [fps, setFps] = useState(30);
    const [mirror, setMirror] = useState(true);
    const [autoExposure, setAutoExposure] = useState(true);

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

                <FormControl fullWidth>

                    <InputLabel>
                        Camera
                    </InputLabel>

                    <Select

                        value={camera}

                        label="Camera"

                        onChange={(e)=>setCamera(e.target.value)}

                    >

                        <MenuItem value="Default Camera">
                            Default Camera
                        </MenuItem>

                        <MenuItem value="USB Camera">
                            USB Camera
                        </MenuItem>

                        <MenuItem value="Virtual Camera">
                            Virtual Camera
                        </MenuItem>

                    </Select>

                </FormControl>

                <FormControl fullWidth>

                    <InputLabel>
                        Resolution
                    </InputLabel>

                    <Select

                        value={resolution}

                        label="Resolution"

                        onChange={(e)=>setResolution(e.target.value)}

                    >

                        <MenuItem value="640x480">
                            640 × 480
                        </MenuItem>

                        <MenuItem value="1280x720">
                            1280 × 720
                        </MenuItem>

                        <MenuItem value="1920x1080">
                            1920 × 1080
                        </MenuItem>

                    </Select>

                </FormControl>

                <Divider/>

                <Typography
                    fontWeight={600}
                >
                    FPS Limit
                </Typography>

                <Slider

                    value={fps}

                    onChange={(e,v)=>setFps(v)}

                    min={10}

                    max={60}

                    step={5}

                    valueLabelDisplay="auto"

                />

                <Typography
                    color="text.secondary"
                >
                    {fps} FPS
                </Typography>

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

                        <FlipRoundedIcon/>

                        <Typography>

                            Mirror Camera

                        </Typography>

                    </Stack>

                    <Switch

                        checked={mirror}

                        onChange={(e)=>setMirror(e.target.checked)}

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

                        <VideocamRoundedIcon/>

                        <Typography>

                            Auto Exposure

                        </Typography>

                    </Stack>

                    <Switch

                        checked={autoExposure}

                        onChange={(e)=>setAutoExposure(e.target.checked)}

                    />

                </Stack>

                <Divider/>

                <Button

                    fullWidth

                    variant="contained"

                    startIcon={<RestartAltRoundedIcon/>}

                >

                    Restart Camera

                </Button>

            </Stack>

        </GlassCard>

    );

}