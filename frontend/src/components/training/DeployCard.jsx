import { useState } from "react";

import {
    Box,
    Button,
    Chip,
    Divider,
    Stack,
    Typography,
} from "@mui/material";

import CloudUploadRoundedIcon from "@mui/icons-material/CloudUploadRounded";
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded";
import RocketLaunchRoundedIcon from "@mui/icons-material/RocketLaunchRounded";

import GlassCard from "../ui/GlassCard";

import { deployModel } from "../../services/trainingService";

export default function DeployCard() {

    const [deploying, setDeploying] = useState(false);

    const [deployed, setDeployed] = useState(false);

    async function handleDeploy() {

        try {

            setDeploying(true);

            await deployModel();

            setDeployed(true);

        }

        catch (err) {

            console.error(err);

        }

        finally {

            setDeploying(false);

        }

    }

    return (

        <GlassCard
            sx={{
                p: 3,
                height: "100%",
                display: "flex",
                flexDirection: "column",
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

                    <RocketLaunchRoundedIcon color="primary" />

                    <Typography

                        variant="h6"

                        fontWeight={700}

                    >

                        Model Deployment

                    </Typography>

                </Stack>

                <Chip

                    color={deployed ? "success" : "default"}

                    label={deployed ? "DEPLOYED" : "READY"}

                />

            </Stack>

            <Divider sx={{ mb: 3 }} />

            <Box sx={{ flex: 1 }}>

                <Typography
                    color="text.secondary"
                    mb={2}
                >
                    Deploy the latest trained gesture recognition model to
                    production for real-time inference.
                </Typography>

                <Stack spacing={2}>

                    <InfoRow
                        title="Latest Version"
                        value="v1.0"
                    />

                    <InfoRow
                        title="Framework"
                        value="TensorFlow"
                    />

                    <InfoRow
                        title="Input Size"
                        value="224 × 224"
                    />

                    <InfoRow
                        title="Classes"
                        value="6"
                    />

                </Stack>

            </Box>

            <Divider sx={{ my: 3 }} />

            <Button

                fullWidth

                size="large"

                variant="contained"

                startIcon={
                    deployed
                        ? <CheckCircleRoundedIcon />
                        : <CloudUploadRoundedIcon />
                }

                onClick={handleDeploy}

                disabled={deploying}

            >

                {

                    deploying

                        ? "Deploying..."

                        : deployed

                            ? "Model Deployed"

                            : "Deploy Model"

                }

            </Button>

        </GlassCard>

    );

}

function InfoRow({

    title,

    value,

}) {

    return (

        <Stack

            direction="row"

            justifyContent="space-between"

        >

            <Typography color="text.secondary">

                {title}

            </Typography>

            <Typography fontWeight={600}>

                {value}

            </Typography>

        </Stack>

    );

}