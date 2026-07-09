import { useState } from "react";

import {
    Stack,
    Typography,
    TextField,
    MenuItem,
    Slider,
    Switch,
    FormControlLabel,
    Divider,
    Button,
    Chip,
    Box,
} from "@mui/material";

import PlayArrowRoundedIcon from "@mui/icons-material/PlayArrowRounded";
import StopRoundedIcon from "@mui/icons-material/StopRounded";
import RestartAltRoundedIcon from "@mui/icons-material/RestartAltRounded";
import MemoryRoundedIcon from "@mui/icons-material/MemoryRounded";

import GlassCard from "../ui/GlassCard";

export default function TrainingControls({

    onStart,

    onStop,

    onResume,

    running = false,

}) {

    const [model, setModel] = useState("CNN");

    const [epochs, setEpochs] = useState(20);

    const [batch, setBatch] = useState(32);

    const [learningRate, setLearningRate] = useState(0.001);

    const [augmentation, setAugmentation] = useState(true);

    const [gpu, setGpu] = useState(true);

    function handleStart() {

        onStart?.({

            model,

            epochs,

            batch,

            learning_rate: learningRate,

            augmentation,

            gpu,

        });

    }

    return (

        <GlassCard
            sx={{
                p: 3,
            }}
        >

            <Stack
                direction="row"
                spacing={1.5}
                alignItems="center"
                mb={3}
            >

                <MemoryRoundedIcon color="primary" />

                <Typography
                    variant="h6"
                    fontWeight={700}
                >
                    Training Configuration
                </Typography>

            </Stack>

            <Stack spacing={3}>

                <TextField
                    select
                    label="Model"
                    value={model}
                    onChange={(e) => setModel(e.target.value)}
                    fullWidth
                >

                    <MenuItem value="CNN">
                        CNN
                    </MenuItem>

                    <MenuItem value="CNN + LSTM">
                        CNN + LSTM
                    </MenuItem>

                    <MenuItem value="Transformer">
                        Transformer
                    </MenuItem>

                </TextField>

                <Box>

                    <Typography gutterBottom>

                        Epochs

                    </Typography>

                    <Slider
                        value={epochs}
                        min={5}
                        max={100}
                        step={5}
                        valueLabelDisplay="auto"
                        onChange={(e, value) => setEpochs(value)}
                    />

                </Box>

                <TextField
                    label="Batch Size"
                    type="number"
                    value={batch}
                    onChange={(e) =>
                        setBatch(Number(e.target.value))
                    }
                    fullWidth
                />

                <TextField
                    label="Learning Rate"
                    type="number"
                    value={learningRate}
                    inputProps={{
                        step: 0.0001,
                    }}
                    onChange={(e) =>
                        setLearningRate(Number(e.target.value))
                    }
                    fullWidth
                />

                <Divider />

                <FormControlLabel
                    control={
                        <Switch
                            checked={augmentation}
                            onChange={(e) =>
                                setAugmentation(e.target.checked)
                            }
                        />
                    }
                    label="Enable Data Augmentation"
                />

                <FormControlLabel
                    control={
                        <Switch
                            checked={gpu}
                            onChange={(e) =>
                                setGpu(e.target.checked)
                            }
                        />
                    }
                    label="Use GPU"
                />

                <Divider />

                <Stack
                    direction="row"
                    spacing={1}
                    flexWrap="wrap"
                    useFlexGap
                >

                    <Chip
                        label={running ? "Training" : "Ready"}
                        color={running ? "warning" : "success"}
                    />

                    <Chip
                        label={`${epochs} Epochs`}
                        color="primary"
                    />

                    <Chip
                        label={`Batch ${batch}`}
                        color="secondary"
                    />

                </Stack>

                <Divider />

                <Button
                    variant="contained"
                    fullWidth
                    size="large"
                    startIcon={<PlayArrowRoundedIcon />}
                    onClick={handleStart}
                    disabled={running}
                >
                    Start Training
                </Button>

                <Button
                    variant="outlined"
                    color="warning"
                    fullWidth
                    startIcon={<RestartAltRoundedIcon />}
                    onClick={onResume}
                    disabled={running}
                >
                    Resume Training
                </Button>

                <Button
                    variant="outlined"
                    color="error"
                    fullWidth
                    startIcon={<StopRoundedIcon />}
                    onClick={onStop}
                    disabled={!running}
                >
                    Stop Training
                </Button>

            </Stack>

        </GlassCard>

    );

}