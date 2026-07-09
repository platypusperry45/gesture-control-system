import {
    Card,
    CardContent,
    Stack,
    Typography,
    Chip,
    Button,
    LinearProgress,
    Avatar,
    Divider,
    Box,
} from "@mui/material";

import {
    motion,
} from "framer-motion";

import PanToolAltRoundedIcon from "@mui/icons-material/PanToolAltRounded";
import EditRoundedIcon from "@mui/icons-material/EditRounded";
import DeleteRoundedIcon from "@mui/icons-material/DeleteRounded";
import PlayArrowRoundedIcon from "@mui/icons-material/PlayArrowRounded";
import BoltRoundedIcon from "@mui/icons-material/BoltRounded";
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded";
import PhotoLibraryRoundedIcon from "@mui/icons-material/PhotoLibraryRounded";

const MotionCard = motion.create(Card);

export default function GestureCard({

    gesture,

    mapping,

    onRename,

    onDelete,

    onTest,

    isActive = false,

    samples = 0,

    confidence = 0,

    accuracy = 97,

}) {

    return (

        <MotionCard

            layout

            whileHover={{

                y: -8,

                scale: 1.015,

            }}

            transition={{

                duration: .25,

            }}

            sx={{

                height: "100%",

                borderRadius: 5,

                overflow: "auto",

                position: "relative",

                background:
                    "linear-gradient(180deg,#141B2D,#0F172A)",

                border: isActive
                    ? "2px solid #6366F1"
                    : "1px solid rgba(255,255,255,.06)",

                boxShadow: isActive

                    ? "0 0 40px rgba(99,102,241,.45)"

                    : "0 20px 45px rgba(0,0,0,.30)",

            }}

        >

            {isActive && (

                <Chip

                    label="LIVE"

                    color="success"

                    size="small"

                    sx={{

                        position: "absolute",

                        right: 16,

                        top: 16,

                        fontWeight: 700,

                    }}

                />

            )}

            <CardContent>

                <Stack spacing={3}>

                    {/* Header */}

                    <Stack

                        direction="row"

                        spacing={2}

                        alignItems="center"

                    >

                        <Avatar

                            sx={{

                                width: 58,

                                height: 58,

                                bgcolor: "primary.main",

                            }}

                        >

                            <PanToolAltRoundedIcon />

                        </Avatar>

                        <Box>

                            <Typography

                                variant="h5"

                                fontWeight={700}

                                textTransform="capitalize"

                            >

                                {gesture}

                            </Typography>

                            <Typography

                                color="text.secondary"

                                variant="body2"

                            >

                                Gesture Recognition

                            </Typography>

                        </Box>

                    </Stack>

                    {/* Status */}

                    <Stack

                        direction="row"

                        spacing={1}

                        flexWrap="wrap"

                    >

                        <Chip

                            icon={<CheckCircleRoundedIcon />}

                            color={
                                mapping.enabled
                                    ? "success"
                                    : "default"
                            }

                            label={
                                mapping.enabled
                                    ? "Enabled"
                                    : "Disabled"
                            }

                        />

                        <Chip

                            icon={<BoltRoundedIcon />}

                            color="primary"

                            label={mapping.type}

                        />

                    </Stack>

                    {/* Confidence */}

                    <Box>

                        <Stack

                            direction="row"

                            justifyContent="space-between"

                            mb={1}

                        >

                            <Typography variant="body2">

                                Confidence

                            </Typography>

                            <Typography
                                fontWeight={700}
                            >

                                {confidence}%

                            </Typography>

                        </Stack>

                        <LinearProgress

                            variant="determinate"

                            value={confidence}

                            sx={{

                                height: 10,

                                borderRadius: 5,

                            }}

                        />

                    </Box>

                    {/* Dataset */}

                    <Stack

                        direction="row"

                        justifyContent="space-between"

                    >

                        <Stack>

                            <Typography

                                color="text.secondary"

                                variant="caption"

                            >

                                Dataset

                            </Typography>

                            <Stack

                                direction="row"

                                spacing={1}

                                alignItems="center"

                            >

                                <PhotoLibraryRoundedIcon

                                    fontSize="small"

                                />

                                <Typography
                                    fontWeight={700}
                                >

                                    {samples}

                                </Typography>

                            </Stack>

                        </Stack>

                        <Stack>

                            <Typography

                                color="text.secondary"

                                variant="caption"

                            >

                                Accuracy

                            </Typography>

                            <Typography

                                fontWeight={700}

                            >

                                {accuracy}%

                            </Typography>

                        </Stack>

                    </Stack>

                    <Divider />

                    {/* Action */}

                    <Box

                        sx={{

                            p:2,

                            borderRadius:3,

                            bgcolor:
                                "rgba(99,102,241,.08)",

                            border:
                                "1px solid rgba(99,102,241,.15)",

                        }}

                    >

                        <Typography

                            variant="caption"

                            color="text.secondary"

                        >

                            Assigned Action

                        </Typography>

                        <Typography

                            variant="h6"

                            fontWeight={700}

                        >

                            {mapping.action}

                        </Typography>

                    </Box>

                    {/* Buttons */}

                    <Stack

                        direction="row"

                        spacing={1}

                    >

                        <Button

                            fullWidth

                            variant="outlined"

                            startIcon={<EditRoundedIcon />}

                            onClick={() =>
                                onRename(
                                    gesture,
                                    mapping
                                )
                            }

                        >

                            Rename

                        </Button>

                        <Button

                            fullWidth

                            color="error"

                            variant="outlined"

                            startIcon={<DeleteRoundedIcon />}

                            onClick={() =>
                                onDelete(
                                    gesture,
                                    mapping
                                )
                            }

                        >

                            Delete

                        </Button>

                    </Stack>

                    <Button

                        fullWidth

                        variant="contained"

                        size="large"

                        startIcon={<PlayArrowRoundedIcon />}

                        onClick={() =>
                            onTest(gesture)
                        }

                    >

                        Test Gesture

                    </Button>

                </Stack>

            </CardContent>

        </MotionCard>

    );

}