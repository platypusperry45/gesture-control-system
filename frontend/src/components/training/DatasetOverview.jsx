import {
    Box,
    Grid,
    Stack,
    Typography,
    LinearProgress,
    Chip,
} from "@mui/material";

import FolderRoundedIcon from "@mui/icons-material/FolderRounded";
import ImageRoundedIcon from "@mui/icons-material/ImageRounded";
import CategoryRoundedIcon from "@mui/icons-material/CategoryRounded";
import StorageRoundedIcon from "@mui/icons-material/StorageRounded";
import UpdateRoundedIcon from "@mui/icons-material/UpdateRounded";

import GlassCard from "../ui/GlassCard";

export default function DatasetOverview({

    dataset = {

        name: "Gesture Dataset",

        images: 2435,

        classes: 6,

        size: "1.82 GB",

        updated: "Today",

        path: "recognition/data/raw/images",

        completion: 100,

    },

}) {

    return (

        <GlassCard

            sx={{

                p: 3,

                height: "100%",

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

                    spacing={2}

                    alignItems="center"

                >

                    <Box

                        sx={{

                            width: 58,

                            height: 58,

                            borderRadius: 3,

                            bgcolor: "primary.main",

                            display: "flex",

                            alignItems: "center",

                            justifyContent: "center",

                        }}

                    >

                        <FolderRoundedIcon

                            sx={{

                                color: "white",

                                fontSize: 30,

                            }}

                        />

                    </Box>

                    <Box>

                        <Typography

                            variant="h6"

                            fontWeight={700}

                        >

                            {dataset.name}

                        </Typography>

                        <Typography color="text.secondary">

                            Dataset Information

                        </Typography>

                    </Box>

                </Stack>

                <Chip

                    color="success"

                    label="READY"

                />

            </Stack>

            <Grid

                container

                spacing={3}

            >

                <Grid item xs={6}>

                    <InfoCard

                        icon={<ImageRoundedIcon color="primary" />}

                        title="Images"

                        value={dataset.images}

                    />

                </Grid>

                <Grid item xs={6}>

                    <InfoCard

                        icon={<CategoryRoundedIcon color="primary" />}

                        title="Classes"

                        value={dataset.classes}

                    />

                </Grid>

                <Grid item xs={6}>

                    <InfoCard

                        icon={<StorageRoundedIcon color="primary" />}

                        title="Dataset Size"

                        value={dataset.size}

                    />

                </Grid>

                <Grid item xs={6}>

                    <InfoCard

                        icon={<UpdateRoundedIcon color="primary" />}

                        title="Updated"

                        value={dataset.updated}

                    />

                </Grid>

            </Grid>

            <Box mt={4}>

                <Typography

                    variant="body2"

                    color="text.secondary"

                >

                    Dataset Path

                </Typography>

                <Typography

                    sx={{

                        mt: 1,

                        fontFamily: "monospace",

                        fontSize: 13,

                        wordBreak: "break-all",

                    }}

                >

                    {dataset.path}

                </Typography>

            </Box>

            <Box mt={4}>

                <Stack

                    direction="row"

                    justifyContent="space-between"

                    mb={1}

                >

                    <Typography color="text.secondary">

                        Dataset Completion

                    </Typography>

                    <Typography fontWeight={700}>

                        {dataset.completion}%

                    </Typography>

                </Stack>

                <LinearProgress

                    variant="determinate"

                    value={dataset.completion}

                    sx={{

                        height: 10,

                        borderRadius: 10,

                    }}

                />

            </Box>

        </GlassCard>

    );

}

function InfoCard({

    icon,

    title,

    value,

}) {

    return (

        <Box

            sx={{

                p: 2,

                borderRadius: 3,

                bgcolor: "rgba(255,255,255,.03)",

                border: "1px solid rgba(255,255,255,.06)",

            }}

        >

            <Stack

                direction="row"

                spacing={1}

                alignItems="center"

                mb={1}

            >

                {icon}

                <Typography

                    color="text.secondary"

                    variant="body2"

                >

                    {title}

                </Typography>

            </Stack>

            <Typography

                variant="h6"

                fontWeight={700}

            >

                {value}

            </Typography>

        </Box>

    );

}