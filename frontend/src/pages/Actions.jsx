import { useMemo, useState } from "react";

import {
    Box,
    Chip,
    CircularProgress,
    Grid,
    InputAdornment,
    Paper,
    Stack,
    TextField,
    Typography,
} from "@mui/material";

import SearchIcon from "@mui/icons-material/Search";
import AddIcon from "@mui/icons-material/Add";
import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";

import { motion } from "framer-motion";

import DashboardLayout from "../components/layouts/DashboardLayout";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";
import GradientButton from "../components/ui/GradientButton";

import ActionGrid from "../components/actions/ActionGrid";

import AddActionDialog from "../components/actions/AddActionDialog";
import EditActionDialog from "../components/actions/EditActionDialog";
import DeleteActionDialog from "../components/actions/DeleteActionDialog";

import useActions from "../hooks/useActions";

export default function Actions() {

    const {
        actions,
        loading,
        error,
        refresh,
    } = useActions();

    const [open, setOpen] = useState(false);
    const [editing, setEditing] = useState(null);
    const [deleting, setDeleting] = useState(null);

    const [search, setSearch] = useState("");
    const [filter, setFilter] = useState("all");

    function handleTest(gesture) {
        console.log("Testing:", gesture);
    }

    const total = Object.keys(actions).length;

    const enabled = Object.values(actions).filter(
        (a) => a.enabled
    ).length;

    const disabled = total - enabled;

    const filteredActions = useMemo(() => {

        return Object.fromEntries(

            Object.entries(actions).filter(([gesture, mapping]) => {

                const matchesSearch =
                    gesture
                        .toLowerCase()
                        .includes(search.toLowerCase());

                const matchesFilter =
                    filter === "all"
                        ? true
                        : filter === "enabled"
                        ? mapping.enabled
                        : !mapping.enabled;

                return matchesSearch && matchesFilter;

            })

        );

    }, [actions, search, filter]);

    return (

        <DashboardLayout>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.45 }}
            >

                <PageContainer>

                    <SectionHeader
                        title="Gesture Action Mapping"
                        subtitle="Configure AI gestures for desktop automation."
                        action={
                            <GradientButton
                                startIcon={<AddIcon />}
                                onClick={() => setOpen(true)}
                            >
                                New Mapping
                            </GradientButton>
                        }
                    />

                    <Grid
                        container
                        spacing={3}
                        sx={{ mb: 4 }}
                    >

                        <Grid size={{ xs: 12, md: 4 }}>

                            <Paper
                                sx={{
                                    p: 3,
                                    borderRadius: 4,
                                    height: "100%",
                                }}
                            >

                                <Stack spacing={1}>

                                    <AutoAwesomeIcon color="primary" />

                                    <Typography
                                        variant="h3"
                                        fontWeight={700}
                                    >
                                        {total}
                                    </Typography>

                                    <Typography color="text.secondary">
                                        Total Gestures
                                    </Typography>

                                </Stack>

                            </Paper>

                        </Grid>

                        <Grid size={{ xs: 12, md: 4 }}>

                            <Paper
                                sx={{
                                    p: 3,
                                    borderRadius: 4,
                                    height: "100%",
                                }}
                            >

                                <Stack spacing={1}>

                                    <CheckCircleIcon color="success" />

                                    <Typography
                                        variant="h3"
                                        fontWeight={700}
                                    >
                                        {enabled}
                                    </Typography>

                                    <Typography color="text.secondary">
                                        Enabled
                                    </Typography>

                                </Stack>

                            </Paper>

                        </Grid>

                        <Grid size={{ xs: 12, md: 4 }}>

                            <Paper
                                sx={{
                                    p: 3,
                                    borderRadius: 4,
                                    height: "100%",
                                }}
                            >

                                <Stack spacing={1}>

                                    <CancelIcon color="error" />

                                    <Typography
                                        variant="h3"
                                        fontWeight={700}
                                    >
                                        {disabled}
                                    </Typography>

                                    <Typography color="text.secondary">
                                        Disabled
                                    </Typography>

                                </Stack>

                            </Paper>

                        </Grid>

                    </Grid>

                    <Paper
                        sx={{
                            p: 3,
                            mb: 4,
                            borderRadius: 4,
                        }}
                    >

                        <Stack spacing={3}>

                            <TextField
                                fullWidth
                                placeholder="Search gesture..."
                                value={search}
                                onChange={(e) =>
                                    setSearch(e.target.value)
                                }
                                InputProps={{
                                    startAdornment: (
                                        <InputAdornment position="start">
                                            <SearchIcon color="action" />
                                        </InputAdornment>
                                    ),
                                }}
                            />

                            <Stack
                                direction="row"
                                spacing={2}
                                flexWrap="wrap"
                                useFlexGap
                            >

                                <Chip
                                    clickable
                                    label="All"
                                    color={
                                        filter === "all"
                                            ? "primary"
                                            : "default"
                                    }
                                    onClick={() => setFilter("all")}
                                />

                                <Chip
                                    clickable
                                    label="Enabled"
                                    color={
                                        filter === "enabled"
                                            ? "success"
                                            : "default"
                                    }
                                    onClick={() => setFilter("enabled")}
                                />

                                <Chip
                                    clickable
                                    label="Disabled"
                                    color={
                                        filter === "disabled"
                                            ? "error"
                                            : "default"
                                    }
                                    onClick={() => setFilter("disabled")}
                                />

                            </Stack>

                        </Stack>

                    </Paper>
                    

                    {/* Content */}

                    {
                        loading ? (
                            <Stack
                                alignItems="center"
                                justifyContent="center"
                                py={10}
                            >
                                <CircularProgress />
                                <Typography
                                    mt={2}
                                    color="text.secondary"
                                >
                                    Loading gesture mappings...
                                </Typography>
                            </Stack>
                        ) : error ? (
                            <Paper
                                sx={{
                                    p: 6,
                                    borderRadius: 4,
                                    textAlign: "center",
                                }}
                            >
                                <Typography color="error" variant="h6">
                                    {error}
                                </Typography>
                            </Paper>
                        ) : Object.keys(filteredActions).length === 0 ? (
                            <Paper
                                sx={{
                                    p: 8,
                                    borderRadius: 4,
                                    textAlign: "center",
                                }}
                            >
                                <Typography
                                    variant="h2"
                                    mb={2}
                                >
                                    🤖
                                </Typography>

                                <Typography
                                    variant="h5"
                                    fontWeight={700}
                                >
                                    No Gesture Mappings Found
                                </Typography>

                                <Typography
                                    color="text.secondary"
                                    mt={1}
                                    mb={4}
                                >
                                    Create your first desktop automation mapping.
                                </Typography>

                                <GradientButton
                                    startIcon={<AddIcon />}
                                    onClick={() => setOpen(true)}
                                >
                                    Create Mapping
                                </GradientButton>
                            </Paper>
                        ) : (
                            <Box
                                sx={{
                                    pb: 8,
                                }}
                            >
                                <ActionGrid
                                    actions={filteredActions}
                                    onEdit={(gesture, mapping) =>
                                        setEditing({
                                            gesture,
                                            ...mapping,
                                        })
                                    }
                                    onDelete={(gesture, mapping) =>
                                        setDeleting({
                                            gesture,
                                            ...mapping,
                                        })
                                    }
                                    onTest={handleTest}
                                />
                            </Box>
                        )
                    }

                    <AddActionDialog
                        open={open}
                        onClose={() => setOpen(false)}
                        refresh={refresh}
                    />

                    <EditActionDialog
                        action={editing}
                        onClose={() => setEditing(null)}
                        refresh={refresh}
                    />

                    <DeleteActionDialog
                        action={deleting}
                        onClose={() => setDeleting(null)}
                        refresh={refresh}
                    />

                </PageContainer>

            </motion.div>

        </DashboardLayout>

    );

}