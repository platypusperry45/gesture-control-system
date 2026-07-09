import { useMemo, useState } from "react";

import {
    Box,
    CircularProgress,
    Grid,
    Stack,
    Typography,
} from "@mui/material";

import { motion } from "framer-motion";

import DashboardLayout from "../components/layouts/DashboardLayout";
import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

import GestureToolbar from "../components/gestures/GestureToolbar";
import GestureGrid from "../components/gestures/GestureGrid";
import GestureStats from "../components/gestures/GestureStats";

import RenameGestureDialog from "../components/gestures/RenameGestureDialog";
import DeleteGestureDialog from "../components/gestures/DeleteGestureDialog";

import useGestures from "../hooks/useGestures";
import useStatus from "../hooks/useStatus";

export default function Gestures() {

    const {

        gestures,

        loading,

        error,

        refresh,

    } = useGestures();

    const {

        status,

    } = useStatus();

    const [search, setSearch] = useState("");

    const [filter, setFilter] = useState("All");

    const [sort, setSort] = useState("name");

    const [renameGesture, setRenameGesture] = useState(null);

    const [deleteGesture, setDeleteGesture] = useState(null);

    function handleTest(gesture) {

        console.log("Testing:", gesture);

    }

    const stats = useMemo(() => {

        const values = Object.values(gestures);

        return {

            total: values.length,

            enabled: values.filter(g => g.enabled).length,

            disabled: values.filter(g => !g.enabled).length,

            active: status?.prediction ?? "--",

        };

    }, [gestures, status]);

    return (

        <DashboardLayout>

            <motion.div

                initial={{

                    opacity: 0,

                    y: 25,

                }}

                animate={{

                    opacity: 1,

                    y: 0,

                }}

                transition={{

                    duration: .45,

                }}

            >

                <PageContainer>

                    <SectionHeader

                        title="Gesture Library"

                        subtitle="Manage recognition classes, monitor live predictions and organize your AI gesture dataset."

                    />

                    <GestureStats stats={stats} />

                    <Box mt={4}>

                        <GestureToolbar

                            search={search}

                            setSearch={setSearch}

                            filter={filter}

                            setFilter={setFilter}

                            sort={sort}

                            setSort={setSort}

                            refresh={refresh}

                        />

                    </Box>

                    <Box mt={4}>

                        {

                            loading ?

                                (

                                    <Stack

                                        py={12}

                                        alignItems="center"

                                    >

                                        <CircularProgress />

                                        <Typography

                                            mt={2}

                                            color="text.secondary"

                                        >

                                            Loading gestures...

                                        </Typography>

                                    </Stack>

                                )

                                :

                                error ?

                                    (

                                        <Typography

                                            color="error"

                                        >

                                            {error}

                                        </Typography>

                                    )

                                    :

                                    (

                                        <GestureGrid

                                            gestures={gestures}

                                            search={search}

                                            filter={filter}

                                            sort={sort}

                                            currentGesture={status?.prediction}

                                            onRename={(gesture) =>

                                                setRenameGesture(gesture)

                                            }

                                            onDelete={(gesture) =>

                                                setDeleteGesture(gesture)

                                            }

                                            onTest={handleTest}

                                        />

                                    )

                        }

                    </Box>

                    <RenameGestureDialog

                        gesture={renameGesture}

                        onClose={() =>

                            setRenameGesture(null)

                        }

                        refresh={refresh}

                    />

                    <DeleteGestureDialog

                        gesture={deleteGesture}

                        onClose={() =>

                            setDeleteGesture(null)

                        }

                        refresh={refresh}

                    />

                </PageContainer>

            </motion.div>

        </DashboardLayout>

    );

}