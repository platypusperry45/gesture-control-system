import {
    Stack,
    Typography,
    Button,
    Divider,
    Chip,
    Box,
} from "@mui/material";

import DownloadRoundedIcon from "@mui/icons-material/DownloadRounded";
import UploadRoundedIcon from "@mui/icons-material/UploadRounded";
import DeleteSweepRoundedIcon from "@mui/icons-material/DeleteSweepRounded";
import RestartAltRoundedIcon from "@mui/icons-material/RestartAltRounded";
import SettingsBackupRestoreRoundedIcon from "@mui/icons-material/SettingsBackupRestoreRounded";
import InfoRoundedIcon from "@mui/icons-material/InfoRounded";

import GlassCard from "../ui/GlassCard";

export default function SystemSettings() {

    return (

        <GlassCard
            sx={{
                p: 3,
            }}
        >

            <Stack
                direction="row"
                justifyContent="space-between"
                alignItems="center"
                mb={3}
            >

                <Typography
                    variant="h6"
                    fontWeight={700}
                >
                    System Maintenance
                </Typography>

                <Chip
                    label="Healthy"
                    color="success"
                />

            </Stack>

            <Stack spacing={3}>

                <Typography
                    color="text.secondary"
                >
                    Import or export configuration, manage logs, restart services,
                    and restore application defaults.
                </Typography>

                <Divider/>

                <Stack
                    direction={{
                        xs:"column",
                        md:"row",
                    }}
                    spacing={2}
                >

                    <Button

                        fullWidth

                        variant="contained"

                        startIcon={<DownloadRoundedIcon/>}

                    >
                        Export Configuration
                    </Button>

                    <Button

                        fullWidth

                        variant="outlined"

                        startIcon={<UploadRoundedIcon/>}

                    >
                        Import Configuration
                    </Button>

                </Stack>

                <Stack
                    direction={{
                        xs:"column",
                        md:"row",
                    }}
                    spacing={2}
                >

                    <Button

                        fullWidth

                        variant="outlined"

                        color="warning"

                        startIcon={<DeleteSweepRoundedIcon/>}

                    >
                        Clear Training Logs
                    </Button>

                    <Button

                        fullWidth

                        variant="outlined"

                        color="error"

                        startIcon={<SettingsBackupRestoreRoundedIcon/>}

                    >
                        Reset All Settings
                    </Button>

                </Stack>

                <Button

                    variant="contained"

                    color="warning"

                    fullWidth

                    startIcon={<RestartAltRoundedIcon/>}

                >
                    Restart Backend
                </Button>

                <Divider/>

                <Box>

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                        mb={2}
                    >

                        <InfoRoundedIcon color="primary"/>

                        <Typography
                            variant="h6"
                            fontWeight={700}
                        >
                            Application Information
                        </Typography>

                    </Stack>

                    <Stack spacing={1}>

                        <InfoRow
                            label="Application"
                            value="Gesture Control System"
                        />

                        <InfoRow
                            label="Frontend"
                            value="React + Vite"
                        />

                        <InfoRow
                            label="Backend"
                            value="FastAPI"
                        />

                        <InfoRow
                            label="AI Framework"
                            value="TensorFlow"
                        />

                        <InfoRow
                            label="Current Model"
                            value="gesture_recognition.weights.h5"
                        />

                        <InfoRow
                            label="Version"
                            value="v1.0.0"
                        />

                    </Stack>

                </Box>

            </Stack>

        </GlassCard>

    );

}

function InfoRow({

    label,

    value,

}) {

    return (

        <Stack

            direction="row"

            justifyContent="space-between"

            sx={{

                py:1,

                borderBottom:"1px solid rgba(255,255,255,.06)",

            }}

        >

            <Typography
                color="text.secondary"
            >
                {label}
            </Typography>

            <Typography
                fontWeight={600}
            >
                {value}
            </Typography>

        </Stack>

    );

}