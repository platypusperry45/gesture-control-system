import { useState } from "react";

import {
    Stack,
    Typography,
    TextField,
    Switch,
    Divider,
    Button,
    Chip,
} from "@mui/material";

import CloudRoundedIcon from "@mui/icons-material/CloudRounded";
import LinkRoundedIcon from "@mui/icons-material/LinkRounded";
import WifiRoundedIcon from "@mui/icons-material/WifiRounded";
import SyncRoundedIcon from "@mui/icons-material/SyncRounded";

import GlassCard from "../ui/GlassCard";

export default function BackendSettings() {

    const [backendUrl, setBackendUrl] = useState(
        "http://127.0.0.1:8000"
    );

    const [socketUrl, setSocketUrl] = useState(
        `${import.meta.env.VITE_WS_URL}/ws/status`
    );

    const [autoReconnect, setAutoReconnect] = useState(true);

    const [connected] = useState(true);

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

                    <CloudRoundedIcon color="primary"/>

                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        Backend Settings
                    </Typography>

                </Stack>

                <Chip

                    label={connected ? "Connected" : "Disconnected"}

                    color={connected ? "success" : "error"}

                />

            </Stack>

            <Stack spacing={3}>

                <TextField

                    label="Backend API URL"

                    fullWidth

                    value={backendUrl}

                    onChange={(e)=>setBackendUrl(e.target.value)}

                />

                <TextField

                    label="WebSocket URL"

                    fullWidth

                    value={socketUrl}

                    onChange={(e)=>setSocketUrl(e.target.value)}

                />

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

                        <SyncRoundedIcon/>

                        <Typography>

                            Auto Reconnect

                        </Typography>

                    </Stack>

                    <Switch

                        checked={autoReconnect}

                        onChange={(e)=>setAutoReconnect(e.target.checked)}

                    />

                </Stack>

                <Divider/>

                <Stack spacing={1}>

                    <Typography
                        color="text.secondary"
                    >
                        API Status
                    </Typography>

                    <Typography
                        fontWeight={700}
                    >
                        {connected ? "Online" : "Offline"}
                    </Typography>

                </Stack>

                <Stack spacing={1}>

                    <Typography
                        color="text.secondary"
                    >
                        WebSocket
                    </Typography>

                    <Typography
                        fontWeight={700}
                    >
                        Connected
                    </Typography>

                </Stack>

                <Divider/>

                <Button

                    variant="contained"

                    startIcon={<WifiRoundedIcon/>}

                    fullWidth

                >

                    Test Connection

                </Button>

                <Button

                    variant="outlined"

                    startIcon={<LinkRoundedIcon/>}

                    fullWidth

                >

                    Save Connection Settings

                </Button>

            </Stack>

        </GlassCard>

    );

}