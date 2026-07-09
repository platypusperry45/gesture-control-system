import { Grid, Typography, Box } from "@mui/material";
import { motion, AnimatePresence } from "framer-motion";

import GestureCard from "./GestureCard";

const MotionGrid = motion.create(Grid);

export default function GestureGrid({

    gestures,

    search,

    filter,

    sort,

    currentGesture,

    onRename,

    onDelete,

    onTest,

}) {

    let data = Object.entries(gestures);

    // -------------------------
    // Search
    // -------------------------

    if (search.trim()) {

        data = data.filter(([gesture]) =>

            gesture
                .toLowerCase()
                .includes(search.toLowerCase())

        );

    }

    // -------------------------
    // Filter
    // -------------------------

    if (filter === "Active") {

        data = data.filter(

            ([, mapping]) => mapping.enabled

        );

    }

    if (filter === "Inactive") {

        data = data.filter(

            ([, mapping]) => !mapping.enabled

        );

    }

    // -------------------------
    // Sorting
    // -------------------------

    data.sort((a, b) => {

        if (sort === "name") {

            return a[0].localeCompare(b[0]);

        }

        if (sort === "accuracy") {

            return 0;

        }

        if (sort === "samples") {

            return 0;

        }

        return 0;

    });

    // -------------------------

    if (data.length === 0) {

        return (

            <Box

                sx={{

                    py: 10,

                    textAlign: "center",

                }}

            >

                <Typography

                    variant="h5"

                    fontWeight={700}

                >

                    No gestures found

                </Typography>

                <Typography

                    color="text.secondary"

                    sx={{ mt: 1 }}

                >

                    Try another search or filter.

                </Typography>

            </Box>

        );

    }

    return (

        <MotionGrid

            container

            spacing={3}

            initial="hidden"

            animate="show"

            variants={{

                hidden: {},

                show: {

                    transition: {

                        staggerChildren: .08,

                    },

                },

            }}

        >

            <AnimatePresence>

                {

                    data.map(

                        ([gesture, mapping]) => (

                            <Grid

                                key={gesture}

                                size={{

                                    xs:12,

                                    md:6,

                                    lg:4,

                                }}

                            >

                                <motion.div

                                    layout

                                    variants={{

                                        hidden: {

                                            opacity: 0,

                                            y: 35,

                                        },

                                        show: {

                                            opacity: 1,

                                            y: 0,

                                        },

                                    }}

                                    exit={{

                                        opacity: 0,

                                        scale: .9,

                                    }}

                                    transition={{

                                        duration: .35,

                                    }}

                                >

                                    <GestureCard

                                        gesture={gesture}

                                        mapping={mapping}

                                        isActive={

                                            currentGesture === gesture

                                        }

                                        confidence={98}

                                        accuracy={97}

                                        samples={1325}

                                        onRename={onRename}

                                        onDelete={onDelete}

                                        onTest={onTest}

                                    />

                                </motion.div>

                            </Grid>

                        )

                    )

                }

            </AnimatePresence>

        </MotionGrid>

    );

}